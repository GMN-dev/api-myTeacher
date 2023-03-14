from django.contrib import admin
from django.urls import path, include
from .views import ProfessorApiView, CadastrarAulaApiView

urlpatterns = [
    path('professores/', ProfessorApiView.as_view()),
    path('Agendamento/<int:id>/', CadastrarAulaApiView.as_view())

]