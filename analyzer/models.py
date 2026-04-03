from django.db import models
from django.utils import timezone
import datetime

class SkillData(models.Model):
    skill_name = models.CharField(max_length=100)
    year = models.IntegerField()
    job_postings = models.IntegerField()
    demand_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.skill_name} ({self.year})"

class APICache(models.Model):
    skill_name = models.CharField(max_length=100, unique=True)
    job_count = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def is_valid(self):
        # Check if the data is less than 24 hours old
        return self.last_updated > timezone.now() - datetime.timedelta(hours=24)

    def __str__(self):
        return f"Cache for {self.skill_name} - {self.job_count} jobs"