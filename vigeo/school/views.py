from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse

from school.forms import StudentForm
# school views

@login_required
def index(request):
    group = request.user.groups.all()[0].name
    if group == 'teacher':
        return redirect(reverse('school_t_panel'))
    if group == 'student':
        return redirect(reverse('school_s_panel'))

@login_required
def student_panel(request):
    user = request.user
    occup = user.groups.all()[0]
    message = "hello {} you are {}".format(user, occup)
    return HttpResponse(message) 

@login_required(login_url='/auth/login')
@permission_required('school.view_admin', raise_exception=True)
def teacher_panel(request):
    user = request.user
    occup = user.groups.all()[0]
    message = "hello {} you are {}".format(user, occup)
    return HttpResponse(message) 


@permission_required('school.view_admin', raise_exception=True)
@login_required(login_url='/auth/login')
def create_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    tmpl = 'school/register.html'
    return render(request, tmpl, context)

@permission_required('school.view_admin', raise_exception=True)
@login_required(login_url='/auth/login')
def create_lesson(request):
    pass


