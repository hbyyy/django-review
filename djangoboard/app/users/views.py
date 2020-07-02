from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic.base import View

from users.forms import LoginForm
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
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')
        if password != re_password:
            error = '비밀번호가 다릅니다'
            return render(request, 'users/register.html', context={'error': error})
        TestUser.objects.create(email=email, username=username, password=make_password(password))
        return redirect('testusers:register')


# class Register(CreateView):
#     model = TestUser
#     template_name = 'users/register.html'
#     success_url = reverse_lazy('testusers:register')
#     fields = ['username', 'password']
#
#     def post(self, request, *args, **kwargs):
#         self.context

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.cleaned_data.get('user_id')
            return redirect('/')
    else:
        form = LoginForm()

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def index(request):
    user_id = request.session.get('user')

    if user_id:
        user = TestUser.objects.get(pk=user_id)
        return HttpResponse(f'id : {user.username}, email : {user.email}')
    else:
        return HttpResponse('home')
