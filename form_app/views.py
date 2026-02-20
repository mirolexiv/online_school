from django.shortcuts import render
from .form import TeacherForm, StudentForm, SubjectForm, LessonForm
from lessons.models import Lessons, Subjects, Teachers, Students
from lessons import views
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

menu = views.menu

sidebar = [{'title': "Додати урок", 'url_name': 'add:add_lessons'},
           {'title': "Додати вчителя", 'url_name': 'add:add_teacher'},
           {'title': "Додати учня", 'url_name': 'add:add_student'},
           {'title': "Додати предмет", 'url_name': 'add:add_subject'},
]

@login_required
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            try:
                Teachers.objects.create(**form.cleaned_data)
                messages.success(request, "Вчителя додано ✅")
                return redirect('lessons:teachers')
            except:
                form.add_error(None, "Помилка введення даних")
                messages.error(request, "Помилка при збереженні ❌")
        else:
            messages.error(request, "Форма заповнена неправильно ❌")
    else:
        form = TeacherForm()
    context = {'form': form,'menu': menu,'sidebar': sidebar}
    return render(request, 'form_app/add_teacher.html', context)

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                Students.objects.create(**form.cleaned_data)
                messages.success(request, "Учня додано ✅")
                return redirect('lessons:students')   # список учнів
            except:
                form.add_error(None, "Помилка введення даних")
                messages.error(request, "Помилка при збереженні ❌")
        else:
            messages.error(request, "Форма заповнена неправильно ❌")
    else:
        form = StudentForm()
    context = { 'form': form,'menu': menu, 'sidebar': sidebar}
    return render(request, 'form_app/add_student.html', context)

@login_required
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            try:
                Subjects.objects.create(**form.cleaned_data)
                messages.success(request, "Предмет додано ✅")
                return redirect('lessons:subjects')
            except:
                form.add_error(None, "Помилка введення даних")
        else:
            messages.error(request, "Форма заповнена неправильно ❌")
    else:
        form = SubjectForm()
    context = {'form': form, 'menu': menu, 'sidebar': sidebar}
    return render(request, 'form_app/add_subject.html', context)


@login_required
def add_lessons(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            try:
                Lessons.objects.create(**form.cleaned_data)
                messages.success(request, "Заняття додано ✅")
                return redirect('lessons:lessons')  # редірект на список занять
            except:
                form.add_error(None, "Помилка введення даних")
                messages.error(request, "Помилка при збереженні ❌")
        else:
            messages.error(request, "Форма заповнена неправильно ❌")
    else:
        form = LessonForm()
    context = {'form': form,'menu': menu,'sidebar': sidebar    }
    return render(request, 'form_app/add_lessons.html', context)
