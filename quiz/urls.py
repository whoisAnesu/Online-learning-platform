from django.urls import path 
from .views import (QuizListView, quiz_view, quiz_data_view, save_quiz_view)
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz_view'),
    path('<pk>/data/', quiz_data_view, name='quiz_data_view'),
    path('<pk>/save/', save_quiz_view, name='save_quiz_view'),
    path('create_quiz/', views.createQuiz, name='create_quiz'),
]
