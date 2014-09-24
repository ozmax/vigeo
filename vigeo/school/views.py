from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse

from school.forms import StudentForm, LessonForm, CategoryForm, QuestionForm
from school.models import Lesson


@login_required(login_url='/auth/login')
def index(request):
    group = request.user.groups.all()[0].name
    if group == 'teacher':
        return redirect(reverse('school_t_panel'))
    if group == 'student':
        return redirect(reverse('school_s_panel'))

@login_required(login_url='/auth/login')
@permission_required('school.view_admin', raise_exception=True)
def teacher_panel(request):
    tmpl = 'school/t_index.html'
    return render(request, tmpl, {}) 

@login_required(login_url='/auth/login')
@permission_required('school.view_admin', raise_exception=True)
def add_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('school_index'))

    context = {'form': form}
    tmpl = 'school/category.html'
    return render(request, tmpl, context)

@login_required(login_url='/auth/login')
@permission_required('school.view_admin', raise_exception=True)
def create_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    tmpl = 'school/register.html'
    return render(request, tmpl, context)

@login_required(login_url='/auth/login')
@permission_required('school.view_admin', raise_exception=True)
def add_lesson(request):
    form = LessonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('school_index'))
    context = {'form': form}
    tmpl = 'school/lesson.html'
    return render(request, tmpl, context)

@login_required(login_url='/auth/login')
@permission_required('school.view_admin', raise_exception=True)
def add_question(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('school_index'))
    context = {'form': form}
    tmpl = 'school/question.html'
    return render(request, tmpl, context)

@login_required
def student_panel(request):
    tmpl = 'school/s_index.html'
    return render(request, tmpl, {})


@login_required
def lesson_menu(request):
    lessons = Lesson.objects.all()
    context = {'lessons': lessons}
    tmpl = 'school/lesson_menu.html'
    return render(request, tmpl, context)

@login_required
def lesson_detail(request):
    pass

@login_required
def detailed_lesson(request):
    pass

@login_required
def take_test(request):
    pass
