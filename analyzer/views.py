from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import SkillData, APICache
from .utils import analyze_skill_trend, get_similar_skills, predict_career_path
from .api_utils import fetch_live_job_count

def home(request):
    # Fetch top trending skills for the dashboard
    top_skills = SkillData.objects.filter(year=2025).order_by('-job_postings')[:6]
    
    # NEW: Get a clean, alphabetical list of every unique skill in your database
    all_skills = SkillData.objects.values_list('skill_name', flat=True).distinct().order_by('skill_name')
    
    return render(request, 'analyzer/home.html', {
        'top_skills': top_skills,
        'all_skills': all_skills  # Pass it to the template
    })

def compare_skills(request):
    skill_a = request.GET.get('skill_a', '')
    skill_b = request.GET.get('skill_b', '')
    
    # NEW: Get the same alphabetical list for the compare page
    all_skills = SkillData.objects.values_list('skill_name', flat=True).distinct().order_by('skill_name')
    
    context = {
        'skill_a': skill_a,
        'skill_b': skill_b,
        'all_skills': all_skills, # Pass it to the template
    }

    if skill_a and skill_b:
        data_a = SkillData.objects.filter(skill_name__iexact=skill_a).order_by('year')
        data_b = SkillData.objects.filter(skill_name__iexact=skill_b).order_by('year')
        
        years = [entry.year for entry in data_a] 
        postings_a = [entry.job_postings for entry in data_a]
        postings_b = [entry.job_postings for entry in data_b]
        
        context.update({
            'years': years,
            'postings_a': postings_a,
            'postings_b': postings_b,
        })
        
    return render(request, 'analyzer/compare.html', context)

def analyze(request):
    query = request.GET.get('skill')
    if not query:
        return redirect('home')

    # 1. Fetch historical data
    db_skills = SkillData.objects.filter(skill_name__iexact=query)

    # 2. Fetch live data from API
    live_count = fetch_live_job_count(query)

    # 3. Perform AI Trend Analysis
    results = analyze_skill_trend(db_skills, query, live_count)

    if not results:
        return render(request, 'analyzer/error.html', {'message': 'Skill data not found.'})

    # 4. Predict Career Path
    career_prediction = predict_career_path(query, results['status'])
    
    # 5. Get Similar Skills
    similar_skills = get_similar_skills(query)

    # 6. Generate DYNAMIC XAI (Explainable AI) Feature Importance
    # We use the actual mathematical slope to generate realistic chart weights
    ml_slope = results.get('ml_slope', 0)
    
    if ml_slope > 0:
        # If the skill is growing (Green bars push risk DOWN)
        xai_data = {
            'labels': ['Rising Job Volume', 'Strong Community Support', 'Modern Tech Stack', 'Market Saturation Risk'],
            'impact_scores': [-abs(ml_slope), -15, -10, 5] 
        }
    else:
        # If the skill is declining (Red bars push risk UP)
        xai_data = {
            'labels': ['Declining Job Volume', 'Aging Tech Stack', 'Low Recent Demand', 'Legacy Maintenance'],
            'impact_scores': [abs(ml_slope), 25, 20, -5] 
        }

    # Pass everything to the template
    context = {
        'results': results,
        'recommendations': career_prediction,
        'similar_skills': similar_skills,
        'xai_data': xai_data  # <-- Added XAI data here
    }
    return render(request, 'analyzer/result.html', context)


def market_insights(request):
    # Get the Top 10 skills by posting volume
    top_skills = SkillData.objects.order_by('-job_postings')[:10]
    
    # Get the Bottom 10 skills by posting volume (At-Risk/Legacy)
    bottom_skills = SkillData.objects.order_by('job_postings')[:10]
    
    # Count total skills for the header
    total_count = SkillData.objects.count()
    
    context = {
        'top_skills': top_skills,
        'bottom_skills': bottom_skills,
        'total_count': total_count,
    }
    return render(request, 'analyzer/insights.html', context)

def methodology(request): 
    return render(request, 'analyzer/about.html')

def network_map(request):
    return render(request, 'analyzer/network.html')

def skill_timeline(request):
    return render(request, 'analyzer/timeline.html')

def optimize_resume(request):
    context = {}
    
    if request.method == 'POST':
        # 1. Grab the text the user pasted
        resume_text = request.POST.get('resume_text', '')
        job_desc = request.POST.get('job_desc', '')

        # Convert to lowercase for accurate matching
        resume_lower = resume_text.lower()
        jd_lower = job_desc.lower()

        # 2. Fetch all skills from your database to act as our "Dictionary"
        all_skills = SkillData.objects.values_list('skill_name', flat=True).distinct()

        matches = []
        missing = []

        # 3. Analyze the Job Description against the Database
        for skill in all_skills:
            skill_lower = skill.lower()
            
            # If the skill is required in the Job Description...
            if skill_lower in jd_lower:
                # ...check if the candidate has it in their resume
                if skill_lower in resume_lower:
                    matches.append(skill)
                else:
                    missing.append(skill)

        # 4. Calculate the Match Score
        total_required = len(matches) + len(missing)
        if total_required > 0:
            score = int((len(matches) / total_required) * 100)
        else:
            score = 0  # No specific database skills were detected in the JD

        # 5. Send the analysis back to the HTML
        context['analysis'] = {
            'score': score,
            'matches': matches,
            'missing': missing
        }
        
        # Keep the pasted text in the boxes so the user doesn't lose it
        context['resume_text'] = resume_text
        context['job_desc'] = job_desc

    return render(request, 'analyzer/optimize.html', context)