from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from BoardApp.models import Board, Post
from .forms import PostingForm


# Create your views here.


def index(request):
    return render(request, 'BoardApp/index.html')


def show_boards(request, board_name):
    board = get_object_or_404(Board, name=board_name)
    posts = Post.objects.filter(on_board=board, father_id__isnull=True).order_by('-time')
    comments = Post.objects.filter(on_board=board, father_id__isnull=False)

    # forms
    if request.method == "POST" and 'new_thread' in request.POST:
        form = PostingForm(request.POST)
        if form.is_valid():
            tread = form.save(commit=False)
            tread.published_date = timezone.now()
            tread.on_board = board
            board.counter += 1
            board.save()
            tread.post_id = board.counter
            tread.save()

    elif request.method == "POST" and 'new_post' in request.POST:
        form = PostingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.on_board = board
            board.counter += 1
            board.save()
            post.post_id = board.counter
            post.save()
    else:
        form = PostingForm()

    context = {
        'board': board,
        'posts': posts,
        'comments': comments,
        'form':  PostingForm()
    }
    return render(request, 'BoardApp/content.html', context)


def post_new(request):
    form = PostingForm()
    return render(request, 'BoardApp/content.html', {'form': form})
