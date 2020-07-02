from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
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

# class Register(View):
#     def get(self, request):
#         return render(request, 'users/register.html')
#
#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = TestUser.objects.create(username=username, password=password)
#         return redirect('users:register')

class Register(CreateView):
    model = TestUser
    template_name = 'users/register.html'
    success_url = reverse_lazy('testusers:register')
    fields = ['username', 'password']
