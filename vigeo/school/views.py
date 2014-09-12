from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, login_required


def login_view(request):
    context = {'test': 'not logged'}
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                context = {'test': 'test'}
    if request.user.is_authenticated():
        context = {'test': 'logged as %s' % request.user}

    tmpl = 'school/index.html'
    print request.GET
    if ('next' in request.GET) and request.user.is_authenticated():
        return redirect(request.GET['next'])
    return render (request, tmpl, context) 

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/')
@permission_required('school.view_admin', raise_exception=True)
def test_dec(request):
    return HttpResponse('dec op')
