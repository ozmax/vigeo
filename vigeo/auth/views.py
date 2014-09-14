from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/school/index')
    tmpl = 'school/index.html'
    if ('next' in request.GET) and request.user.is_authenticated():
        return redirect(request.GET['next'])
    return render (request, tmpl, {}) 

def logout_view(request):
    logout(request)
    return redirect(reverse('auth_login'))
