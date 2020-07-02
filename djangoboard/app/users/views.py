from django.shortcuts import render, redirect

# Create your views here.
from users.models import TestUser


def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = TestUser.objects.create(username=username, password=password)
        return redirect('users:register')
