from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404,render
from BoardApp.models import Board, Post

# Create your views here.


def index(request):
    return render(request,'BoardApp/index.html')


def show_boards(request,board_name):
    board = get_object_or_404(Board,name=board_name)
    posts = Post.objects.filter(on_board=board,father_id__isnull=True)
    comments = Post.objects.filter(on_board=board,father_id__isnull=False)
    context = {
        'board': board,
        'posts': posts,
        'comments': comments
    }
    return render(request,'BoardApp/content.html', context)