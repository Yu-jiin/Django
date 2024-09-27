from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    summary = forms.CharField(
        label='Summary',
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'summary',
                'rows' : 5,
                'cols' : 50,
            }   
        ),
    )
    memo = forms.CharField(
        label='Memo',
        widget=forms.Textarea(
            attrs={
                'placeholder' : 'memo',

            }
        ),
    )

    class Meta:
        model = Memo
        fields = '__all__'

