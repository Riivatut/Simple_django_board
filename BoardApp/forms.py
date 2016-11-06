from django.forms import ModelForm, HiddenInput, FileInput
from .models import Post, AttachFile


class PostingForm(ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'mail', 'title', 'text', 'father_id')
        widgets = {
            'father_id': HiddenInput(),
        }


class FileForm(ModelForm):
    class Meta:
        model = AttachFile
        fields = ('image', )
