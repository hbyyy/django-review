from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from users.models import TestUser


# def register(request):
#     if request.method == 'GET':
#         return render(request, 'users/register.html')
#     else:
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = TestUser.objects.create(username=username, password=password)
#         return redirect('users:register')

class Register(View):
    def get(self, request):
        return render(request, 'users/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = TestUser.objects.create(username=username, password=password)
        return redirect('users:register')