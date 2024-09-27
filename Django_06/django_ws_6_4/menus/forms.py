from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
            
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control mt-2',
                'placeholder' : '메뉴 이름을 작성해 주세요.',
            }
        ),
    )
    price = forms.CharField(
        label='Price',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control mt-2',
            }
        ),
    )
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(
            attrs={
                'class' : 'form-control mt-2',
                'placeholder' : '메뉴 설명을 작성해 주세요.',
            }
        ),
    )