from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
from user.models import User
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.
def board_list(request):
    # 모든 게시글 가져오기
    all_boards = Board.objects.all().order_by('-id')
    
    # GET 방식으로 page를 가져오기, 없으면 기본 1페이지
    page = int(request.GET.get('page', 1))

    # 전체 게시글에서 몇 개의 게시글을 쪼개서 가져올지 설정 (여기서는 1페이지당 5개)
    paginator = Paginator(all_boards, 5)

    # 페이지네이터에서 해당 페이지의 게시글 목록 보여주기
    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/user/login')
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_pk = request.session.get('user')
            user = User.objects.get(pk= user_pk)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user

            board.save()
            return redirect("/board/list/")
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})

def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        ## 오류 처리
        raise Http404('게시글을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board': board})