from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyze/', views.analyze, name='analyze'),
    path('compare/', views.compare_skills, name='compare'),
    path('network/', views.network_map, name='network'),
    path('timeline/', views.skill_timeline, name='timeline'),
    path('optimize/', views.optimize_resume, name='optimize'),
    path('insights/', views.market_insights, name='insights'),
    path('about/', views.methodology, name='about'),
]