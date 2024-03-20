from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
from user.models import User

# Create your views here.
def board_list(request):
    # 모든 게시글 가져오기
    boards = Board.objects.all().order_by('-id')
    
    return render(request, 'board_list.html', {'boards': boards})


def board_write(request):
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