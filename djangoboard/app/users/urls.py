from django.urls import path

from users.views import Register

app_name = 'testusers'
urlpatterns = [
    path('register/', Register.as_view(), name='register'),
]
