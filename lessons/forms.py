from django import forms
from .models import Students, Teachers, Subjects, Lessons

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = '__all__'

class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = '__all__'

class LessonsForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = '__all__'