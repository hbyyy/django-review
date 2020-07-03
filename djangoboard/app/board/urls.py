from django.urls import path

# from .views import board_list, board_create, board_detail
from .views import board_list, BoardDetail, BoardCreate

app_name = 'board'
urlpatterns = [
    # path('', board_list, name='board-list'),
    # path('create/', board_create, name='board-create'),
    # path('<int:pk>/', board_detail, name='board-detail')
    path('', board_list, name='board-list'),
    path('<int:pk>/', BoardDetail.as_view(), name='board-detail'),
    path('create/', BoardCreate.as_view(), name='board-create'),
]