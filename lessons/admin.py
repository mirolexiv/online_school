from django.contrib import admin
from .models import *

class LessonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'student','teacher','data','subject','duration',)
    list_display_links = ('id', 'student')
    list_filter = ('student','teacher','data','subject','duration',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic', 'birth_date', 'grade')
    list_display_links = ('id', 'last_name',)
    list_filter = ('last_name',)

class TeachersAdmin(admin.ModelAdmin):
    list_display = ('id','last_name','first_name', 'patronymic', 'subject')
    list_display_links = ('id', 'last_name',)
    list_filter = ('last_name',)
    ordering = ('last_name',)

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    ordering = ('name',)

# Register your models here.
admin.site.register(Lessons, LessonsAdmin)
admin.site.register(Students, StudentAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Subjects,SubjectsAdmin)




