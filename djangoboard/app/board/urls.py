from django.urls import path

from .views import board_list, board_create

app_name = 'board'
urlpatterns = [
    path('', board_list, name='board-list'),
    path('create/', board_create, name='board-create'),
]