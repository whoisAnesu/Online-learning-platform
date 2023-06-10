from django.urls import path 
from . import views 


urlpatterns = [
    
    path('course/<str:pk>/', views.course, name='course'),
    path('allcourses/', views.coursesAll, name='allcourses'),

    path('uploadass/', views.uploadAss, name='uploadass'),
    path('submitass/', views.submitAss, name='submitass'),
    path('upload/', views.upload, name='upload'),
    path('uploadbook/', views.upload_book, name='uploadbook'),
    
    path('video/<str:pk>/', views.video, name='video'),
    path('books/<str:pk>/', views.books, name='books'),
    
    path('mycourses/<str:pk>/', views.myCourses, name='mycourses'),
    
    path('register/<str:pk>/', views.registerCourses, name='register'),
]