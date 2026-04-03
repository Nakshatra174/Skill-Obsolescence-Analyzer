import hashlib

# Safely try to import SerpApi so the app doesn't crash if it's not installed
try:
    from serpapi import GoogleSearch
    SERPAPI_AVAILABLE = True
except ImportError:
    SERPAPI_AVAILABLE = False

def fetch_live_job_count(skill_name):
    # Paste your real key here if you have one. 
    # If left as "YOUR_SERP_API_KEY", it safely switches to Presentation Mock Mode.
    API_KEY = "YOUR_SERP_API_KEY" 

    # --- 1. PRESENTATION MOCK MODE (Failsafe for your Seminar) ---
    if API_KEY == "YOUR_SERP_API_KEY" or not SERPAPI_AVAILABLE:
        # We use a hash so the fake number is ALWAYS the same for the same skill.
        # (e.g., Python will always return 245,000, not a random jumping number)
        seed = int(hashlib.md5(skill_name.encode()).hexdigest(), 16) % 5000
        
        # Give a realistic boost to known major technologies
        multiplier = 15
        if skill_name.lower() in ['python', 'java', 'react', 'javascript', 'aws', 'sql']:
            multiplier = 65
        elif skill_name.lower() in ['jquery', 'ruby', 'php', 'angularjs']:
            multiplier = 4 # Legacy tech gets lower numbers
            
        mock_count = (seed + 1500) * multiplier
        return mock_count
    # -------------------------------------------------------------

    # --- 2. REAL API CALL (Runs only if you provide a real key) ---
    params = {
        "engine": "google_jobs",
        "q": f"{skill_name} jobs in India",
        "hl": "en",
        "api_key": API_KEY
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        
        if "jobs_results" in results and len(results["jobs_results"]) > 0:
            # SerpApi returns pages of 10-20 jobs. 
            # We multiply to simulate the broader market volume.
            return len(results["jobs_results"]) * 450 
            
        return None 
    except Exception as e:
        print(f"Live API Error: {e}")
        return None  # Safely returns None, which triggers your ML model fallback!