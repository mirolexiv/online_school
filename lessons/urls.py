from django.urls import path
from . import views

app_name = 'lessons'

urlpatterns = [
    path('students/', views.web_students, name='students'),
    path('students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),

    path('subjects/', views.web_subjects, name='subjects'),
    path('subjects/edit/<int:pk>/', views.edit_subject, name='edit_subject'),
    path('subjects/delete/<int:pk>/', views.delete_subject, name='delete_subject'),

    path('teachers/', views.web_teachers, name='teachers'),
    path('teachers/edit/<int:pk>/', views.edit_teacher, name='edit_teacher'),
    path('teachers/delete/<int:pk>/', views.delete_teacher, name='delete_teacher'),

    path('lessons/', views.web_lessons, name='lessons'),
    path('lessons/edit/<int:pk>/', views.edit_lesson, name='edit_lesson'),
    path('lessons/delete/<int:pk>/', views.delete_lesson, name='delete_lesson'),

    path('', views.web_about, name='about'),
]

