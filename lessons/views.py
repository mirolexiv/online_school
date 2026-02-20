from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Students, Teachers, Subjects, Lessons
from .forms import StudentForm, TeachersForm, SubjectsForm, LessonsForm


menu = [{'title': "Про сайт", 'url_name': 'lessons:about'},
        {'title': "Заняття", 'url_name': 'lessons:lessons'},
        {'title': "Додати", 'url_name': 'add:add_lessons'},
]
sidebar = [{'title': "Уроки", 'url_name': 'lessons:lessons'},
           {'title': "Вчителі", 'url_name': 'lessons:teachers'},
           {'title': "Учні", 'url_name': 'lessons:students'},
           {'title': "Предмети", 'url_name': 'lessons:subjects'},
]

# Create your views here.
def web_students(request):
    students = Students.objects.all()
    context = {'students': students, 'menu': menu, 'sidebar': sidebar}
    return render(request, 'lessons/students.html', context)

def web_teachers(request):
    teachers = Teachers.objects.all()
    context = {'teachers': teachers, 'menu': menu, 'sidebar': sidebar}
    return render(request, 'lessons/teachers.html', context)

def web_subjects(request):
    subjects = Subjects.objects.all()
    context = {'subjects': subjects, 'menu': menu, 'sidebar': sidebar}
    return render(request, 'lessons/subjects.html', context)

def web_lessons(request):
    lessons = Lessons.objects.all()
    context = {'lessons': lessons, 'menu': menu, 'sidebar': sidebar}
    return render(request, 'lessons/lessons.html', context)

def web_about(request):
    context = {'menu': menu, 'sidebar': sidebar}
    return render(request, 'lessons/about.html', context)

@login_required
def edit_student(request, pk):
    student = get_object_or_404(Students, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('lessons:students')
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'menu': menu,
        'sidebar': sidebar
    }
    return render(request, 'lessons/edit_student.html', context)

@login_required
def delete_student(request, pk):
    student = get_object_or_404(Students, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('lessons:students')

    context = {
        'student': student,
        'menu': menu,
        'sidebar': sidebar
    }
    return render(request, 'lessons:students', context)

@login_required
def edit_teacher(request, pk):
    teacher = get_object_or_404(Teachers, pk=pk)

    if request.method == 'POST':
        form = TeachersForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('lessons:teachers')
    else:
        form = TeachersForm(instance=teacher)

    context = {
        'form': form,
        'menu': menu,
        'sidebar': sidebar
    }
    return render(request, 'lessons/edit_teacher.html', context)

@login_required
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teachers, pk=pk)

    if request.method == 'POST':
        teacher.delete()
        return redirect('lessons:teachers')

    context = {
        'teacher': teacher,
        'menu': menu,
        'sidebar': sidebar
    }
    return render(request, 'lessons:teachers', context)

@login_required
def edit_subject(request, pk):
    subject = get_object_or_404(Subjects, pk=pk)

    if request.method == 'POST':
        form = SubjectsForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('lessons:subjects')
    else:
        form = SubjectsForm(instance=subject)

    context = {
        'form': form,
        'menu': menu,
        'sidebar': sidebar
    }
    return render(request, 'lessons/edit_subject.html', context)

@login_required
def delete_subject(request, pk):
    subject = get_object_or_404(Subjects, pk=pk)

    if request.method == 'POST':
        subject.delete()
        return redirect('lessons:subjects')

    context = {
        'subject': subject,
        'menu': menu,
        'sidebar': sidebar
    }
    return render(request, 'lessons:subjects', context)

@login_required
def edit_lesson(request, pk):
    lesson = get_object_or_404(Lessons, pk=pk)

    if request.method == 'POST':
        form = LessonsForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lessons:lessons')
    else:
        form = LessonsForm(instance=lesson)

    context = {
        'form': form,
        'menu': menu,
        'sidebar': sidebar
    }
    return render(request, 'lessons/edit_lesson.html', context)

@login_required
def delete_lesson(request, pk):
    lesson = get_object_or_404(Lessons, pk=pk)

    if request.method == 'POST':
        lesson.delete()
        return redirect('lessons:lessons')

    context = {
        'lesson': lesson,
        'menu': menu,
        'sidebar': sidebar
    }
    return render(request, 'lessons:lessons', context)