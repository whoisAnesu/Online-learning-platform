from django.urls import path 
from . import views 


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('student_profile/<str:pk>/', views.student_profile, name='student_profile'),
    path('news_page/<str:pk>/', views.news_page, name='news_page'),
    path('delete_comment/<str:pk>/', views.deleteComment, name='deleteComment'),
    path('delete_comment2/<str:pk>/', views.deleteComment2, name='deleteComment2'),
    path('coursework/<str:pk>/', views.save_user_marks , name='coursework'),
    path('create_quiz/', views.createQuiz, name='create_quiz'),
    path('create_question/', views.createQuestion, name='create_question'),
]
