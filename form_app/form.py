from django import forms

from lessons.models import Students, Teachers, Subjects

class TeacherForm(forms.Form):
    last_name = forms.CharField(max_length=100, label="Прізвище")
    first_name = forms.CharField(max_length=100, label="Ім'я")
    patronymic = forms.CharField(max_length=100, label="Побатькові")
    subject = forms.CharField(max_length=100, label="Предмет")

class StudentForm(forms.Form):
    last_name = forms.CharField(max_length=100, label='Прізвище')
    first_name = forms.CharField(max_length=100, label='Ім\'я')
    patronymic = forms.CharField(max_length=100, label='Побатькові')
    birth_date = forms.DateField(label='Дата народження', widget=forms.DateInput(attrs={'type': 'date'}))
    grade = forms.IntegerField(label='Клас')

class SubjectForm(forms.Form):
    name = forms.CharField(max_length=100, label='Предмет')


class LessonForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Students.objects.all(), label="Учень")
    teacher = forms.ModelChoiceField(queryset=Teachers.objects.all(), label="Вчитель")
    data = forms.DateField(label='Дата уроку',widget=forms.DateInput(attrs={'type': 'date'}))
    subject = forms.ModelChoiceField(queryset=Subjects.objects.all(), label="Навчальний предмет")
    duration = forms.IntegerField(label='Тривалість')