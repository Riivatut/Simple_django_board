from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from BoardApp.models import Board, Post, AttachFile
from .forms import PostingForm, FileForm


# Create your views here.


def index(request):
    return render(request, 'BoardApp/index.html')


def show_boards(request, board_name):
    board = get_object_or_404(Board, name=board_name)
    posts = Post.objects.filter(on_board=board, father_id__isnull=True)
    comments = Post.objects.filter(on_board=board, father_id__isnull=False)
    file_form_list = [ FileForm() for i in range(4)]

    # forms
    if request.method == "POST" and 'new_thread' in request.POST:
        form = PostingForm(request.POST)
        file_form = FileForm(request.FILES)
        if form.is_valid():
            tread = form.save(commit=False)
            tread.published_date = timezone.now()
            tread.on_board = board
            board.counter += 1
            board.save()
            tread.post_id = board.counter
            tread.save()
            if file_form.is_valid() and request.FILES:
                for img in request.FILES.getlist('image'):
                    AttachFile.objects.create(post=tread, image=img)

    elif request.method == "POST" and 'new_post' in request.POST:
        form = PostingForm(request.POST)
        file_form = FileForm(request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.on_board = board
            board.counter += 1
            board.save()
            post.post_id = board.counter
            post.save()
            if file_form.is_valid() and request.FILES:
                for img in request.FILES.getlist('image'):
                    AttachFile.objects.create(post=post, image=img)
    else:
        form = PostingForm()
        file_form = FileForm()

    context = {
        'board': board,
        'posts': posts,
        'comments': comments,
        'form':  PostingForm(),
        'file_form_list': file_form_list
    }
    return render(request, 'BoardApp/content.html', context)


def post_new(request):
    form = PostingForm()
    return render(request, 'BoardApp/content.html', {'form': form})
