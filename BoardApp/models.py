from django.db import models
from django.utils import timezone


class Board(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    time = models.DateTimeField(default = timezone.now)
    author = models.CharField(max_length=100,blank=True,default='Анонимус')
    title = models.CharField(max_length=200,blank=True)
    mail = models.EmailField(null=True,blank=True)
    text = models.TextField()
    on_board = models.ForeignKey(Board,related_name="posts")
    father = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return self.title

