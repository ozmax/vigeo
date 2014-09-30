# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse

from school.forms import StudentForm, LessonForm, CategoryForm, QuestionForm,\
    QuizForm
from school.models import Lesson, Category, Question, Student


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

@login_required(login_url='/auth/login')
@login_required
def student_panel(request):
    tmpl = 'school/student_main.html'
    return render(request, tmpl, {})

@login_required(login_url='/auth/login')
def category_menu(request):
    stud = Student.objects.get(user_id=request.user.id)
    data = stud.test_data
    from ast import literal_eval as lev
    try:
        data = lev(data)
    except SyntaxError:
        data = {}
    categories = Category.objects.all()
    context = {'categories': categories, 'data': data}
    tmpl = 'school/category_menu.html'
    return render(request, tmpl, context)


@login_required(login_url='/auth/login')
def lesson_menu(request):
    cat_id = request.GET.get('cat_id')
    if cat_id:
        lessons = Lesson.objects.filter(category=cat_id)
        category = Category.objects.get(id=cat_id)
    else:
        lessons = None
    context = {'lessons': lessons, 'cat_id': cat_id, 'category': category}
    tmpl = 'school/lesson_menu.html'
    return render(request, tmpl, context)

@login_required(login_url='/auth/login')
def lesson_detail(request):
    lesson_id = request.GET.get('lesson_id')
    cat_id = request.GET.get('cat_id')
    if lesson_id:
        lesson = Lesson.objects.get(id=lesson_id)
    else:
        lesson = None
    context = {'lesson': lesson, 'cat_id': cat_id}
    tmpl = 'school/lesson_detail.html'
    return render(request, tmpl, context)

@login_required(login_url='/auth/login')
def take_test(request):
    if request.method == 'POST':
        q_ids = request.POST['qs']
        q_ids = q_ids[1:-1].split(',')
        q_ids = map(int, q_ids)
        form = QuizForm(request.POST, q_ids=q_ids)
        #if form.is_valid():
        grade_test(request, request.POST, q_ids)
        return redirect(reverse('school_index'))
    if request.method == 'GET':
        form = QuizForm()
    tmpl = 'school/quiz.html'
    context = {'form': form}
    return render(request, tmpl, context)

def grade_test(request, data, ids):
    from ast import literal_eval as lev
    stud = Student.objects.get(user_id=request.user.id)
    try:
        stud_data = lev(stud.test_data)
    except SyntaxError:
        stud_data = {}

    p_data = data.copy()
    result = {}
    for id in ids:
        q = Question.objects.get(id=id)
        result[q.category_id] = 0
    del p_data['csrfmiddlewaretoken']
    del p_data['qs']
    for key in p_data.keys():
        q = Question.objects.get(title=key)
        if q.correct_answer != p_data[key]:
             result[q.category_id] += -1
        else:
            result[q.category_id] += 1
    for key in result:
        if key in stud_data:
            stud_data[key] += result[key]
        else:
            stud_data[key] = result[key]
    stud_data = str(stud_data)
    stud.test_data = stud_data
    stud.save()
