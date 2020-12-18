from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rules import views

urlpatterns = [
    path('rules/', views.AdruleList.as_view()),
    path('rules/<int:pk>/', views.AdruleDetail.as_view()),
]