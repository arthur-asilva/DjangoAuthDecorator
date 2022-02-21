from django.shortcuts import render, redirect
from .models import User
from .authentication import ViewAccessControl



def LoginView(request):

    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['user'], password=request.POST['password'])
        if user.count() > 0:
            request.session['user_id'] = user[0].id
            return redirect('../home/')

    return render(request, 'login.html')


@ViewAccessControl
def HomeView(request):
    return render(request, 'home.html')


@ViewAccessControl
def AdminView(request):
    return render(request, 'admin.html')


def UnauthorizedPageView(request):
    return render(request, 'unauthorized_page.html')