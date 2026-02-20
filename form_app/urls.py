from django.urls import path
from . import views

app_name = 'add'

urlpatterns = [
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('add_lessons/', views.add_lessons, name='add_lessons'),
]

