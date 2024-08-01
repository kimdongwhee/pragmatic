from django.forms import ModelForm
from articleapp.models import Article
from django import forms

class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left', 'style': 'height:auto;'}))

    class Meta:
        model = Article
        fields = ["title", "image", "content"]
