from django.urls import path

from .views import board_list, board_create, board_detail

app_name = 'board'
urlpatterns = [
    path('', board_list, name='board-list'),
    path('create/', board_create, name='board-create'),
    path('<int:pk>/', board_detail, name='board-detail')
]