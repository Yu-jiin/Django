from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control mt-2',
            }
        ),
    )
    content = forms.CharField(
        label='Content',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control mt-2',
            }
        ),
    )
    image_description = forms.CharField(
        label='Image description',
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control mt-2',
            }
        ),
    )