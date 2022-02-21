from django.shortcuts import render, redirect
from .models import User

def LoginView(request):

    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['user'], password=request.POST['password'])
        if user.count() > 0:
            request.session['user_id'] = user[0].id
            return redirect('../home/')

    return render(request, 'login.html')


def HomeView(request):
    return render(request, 'home.html')

def AdminView(request):
    return render(request, 'admin.html')