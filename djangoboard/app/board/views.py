from django.shortcuts import render, redirect

# Create your views here.
from board.decorators import login_required
from board.forms import BoardForm
from board.models import Board
from users.models import TestUser


def board_list(request):
    boards = Board.objects.order_by('-id')
    return render(request, 'board/board_list.html', {'boards': boards})


@login_required
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            Board.objects.create(title=form.cleaned_data.get('title'), contents=form.cleaned_data.get('contents'),
                                 writer=TestUser.objects.get(pk=request.session['user']))
            return redirect('board:board-list')
    elif request.method == 'GET':
        form = BoardForm()
    return render(request, 'board/board_create.html', {'form': form})
