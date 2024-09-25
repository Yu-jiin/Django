from django import forms
from .models import Article

# 입력받을 애들만 적으면 됨 created_at은 입력 안받으니까 안적어
# TextField는 없음 
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = '__all__'
#         # exclude = ('title',)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placdholder' : 'Enter the title',
                'maxlength' : 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class' : 'my-content',
                'placeholder' : 'Enter the content',
                'rows' : 5,
                'cols' : 50,
            }
        ),
        error_messages={'required' : '내용을 입력해주세요'}
    )
    class Meta:
        model = Article
        fields = '__all__'