from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404,render
from BoardApp.models import Board

# Create your views here.


def index(request):
    template = loader.get_template('BoardApp/index.html')
    return HttpResponse(template.render())


def show_boards(request,board_name):
    board = get_object_or_404(Board,name=board_name)

    return render(request,'BoardApp/content.html', {'board':board})