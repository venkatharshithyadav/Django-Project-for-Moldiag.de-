from django.urls import path 
from . import views

urlpatterns =[
    path("", views.home, name="home"),
    path('select-hpo-entries/', views.select_hpo_entries, name='select_hpo_entries'),
    path('group-hpo-entries/', views.group_hpo_entries, name='group_hpo_entries'),
    path('translate-results/', views.translate_results, name='translate_results'),
]

