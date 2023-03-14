from django.contrib import admin
from django.urls import path, include
from .views import ProfessorApiView

urlpatterns = [
    path('professores/', ProfessorApiView.as_view())
]