from django.db import models

# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    mail = models.EmailField(null=True)
    text = models.TextField()
    on_board = Board()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()
    on_article = Article()

