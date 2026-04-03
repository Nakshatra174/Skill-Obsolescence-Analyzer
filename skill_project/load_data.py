import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skill_project.settings')
django.setup()

from analyzer.models import SkillData

# Sample Market Data
data = [
    # Emerging Skill: Python
    {'name': 'Python', 'year': 2023, 'postings': 50000, 'score': 80},
    {'name': 'Python', 'year': 2024, 'postings': 70000, 'score': 90},
    {'name': 'Python', 'year': 2025, 'postings': 95000, 'score': 98},
    
    # Declining Skill: jQuery
    {'name': 'Jquery', 'year': 2023, 'postings': 30000, 'score': 50},
    {'name': 'Jquery', 'year': 2024, 'postings': 15000, 'score': 30},
    {'name': 'Jquery', 'year': 2025, 'postings': 5000, 'score': 10},

    # Stable Skill: Java
    {'name': 'Java', 'year': 2023, 'postings': 60000, 'score': 70},
    {'name': 'Java', 'year': 2024, 'postings': 62000, 'score': 71},
    {'name': 'Java', 'year': 2025, 'postings': 61000, 'score': 70},
]

for entry in data:
    SkillData.objects.get_or_create(
        skill_name=entry['name'],
        year=entry['year'],
        job_postings=entry['postings'],
        demand_score=entry['score']
    )

print("✅ AI Sample Data Loaded Successfully!")