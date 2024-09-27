from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
        ),
    )
    content = forms.CharField(
        label='Description',
        widget=forms.Textarea(
        ),
        error_messages={'required' : '내용을 입력해주세요'}
    )
    images = forms.ImageField(
        label='Movie image'
    )
    class Meta:
        model = Movie
        fields = '__all__'

