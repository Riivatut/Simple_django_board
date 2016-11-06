from django.forms import ModelForm, HiddenInput
from .models import Post


class PostingForm(ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'mail', 'title', 'text','image','father_id')
        widgets = {
            'father_id':HiddenInput(),
        }
