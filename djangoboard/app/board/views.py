# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, FormView

from board.forms import BoardForm
from users.decorators import login_required
from users.models import TestUser
from .models import Board


# def board_list(request):
#     all_boards = Board.objects.order_by('-id')
#     paginator = Paginator(all_boards, 2)
#
#     page_number = request.GET.get('page')
#     boards = paginator.get_page(page_number)
#     return render(request, 'board/board_list.html', {'boards': boards})
#
#
# def board_detail(request, pk):
#     try:
#         board = Board.objects.get(pk=pk)
#     except Board.DoesNotExist:
#         raise Http404('없는 게시글입니다.')
#     return render(request, 'board/board_detail.html', {'board': board})
#
#
# @login_required
# def board_create(request):
#     if request.method == 'POST':
#         form = BoardForm(request.POST)
#         if form.is_valid():
#             Board.objects.create(title=form.cleaned_data.get('title'), contents=form.cleaned_data.get('contents'),
#                                  writer=TestUser.objects.get(pk=request.session['user']))
#             return redirect('board:board-list')
#     elif request.method == 'GET':
#         form = BoardForm()
#     return render(request, 'board/board_create.html', {'form': form})

class BoardList(ListView):
    template_name = 'board/board_list.html'
    model = Board
    paginate_by = 2
    context_object_name = 'boards'


class BoardDetail(DetailView):
    template_name = 'board/board_detail.html'
    model = Board
    context_object_name = 'board'


@method_decorator(login_required, name='dispatch')
class BoardCreate(FormView):
    template_name = 'board/board_create.html'
    model = Board
    form_class = BoardForm
    success_url = reverse_lazy('board:board-list')

    def form_valid(self, form):
        Board.objects.create(title=form.cleaned_data.get('title'), contents=form.cleaned_data.get('contents'),
                             writer=TestUser.objects.get(pk=self.request.session['user']))
        return super().form_valid(form)
