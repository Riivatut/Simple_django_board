from django.db import models

# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    mail = models.EmailField(null=True)
    text = models.TextField()
    on_board = models.ForeignKey(Board,related_name="posts")
    father = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.title



