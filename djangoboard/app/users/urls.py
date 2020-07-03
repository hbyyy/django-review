from django.urls import path

from users.views import Register, login, logout

app_name = 'testusers'
urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
