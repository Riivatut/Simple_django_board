from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Board(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Post(models.Model):
    ordering = ['-time']
    time = models.DateTimeField(default = timezone.now)
    author = models.CharField(max_length=100, blank=True, default='Анонимус')
    mail = models.EmailField(null=True, blank=True)
    title = models.CharField(max_length=200, blank=True)
    text = models.TextField()

    on_board = models.ForeignKey(Board,related_name="posts")
    post_id = models.PositiveIntegerField(null=True, blank=True)
    father_id = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class AttachFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="image")
    image = models.FileField(null=True, blank=True, upload_to='uploads/')
    image_thumbnail = ImageSpecField(source='image',  processors=[ResizeToFill(100, 50)],
                              format='JPEG',
                              options={'quality': 60})
