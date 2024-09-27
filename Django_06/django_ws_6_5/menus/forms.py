from django import forms
from .models import Menu
from django.core.exceptions import ValidationError
import re

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '메뉴 이름을 작성해 주세요.'
                    }
                ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': '메뉴 설명을 작성해 주세요.'
                    }
                ),
            'price': forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    # 'maxlength' : 8,
                }
                ),
            'is_vegan': forms.RadioSelect(
                choices=[
                    (True, 'YES'),
                    (False, 'NO')
                ],
                attrs={'class': 'form-control'}
                ),
        }

    def clean_price(self):
        # price = self.cleaned_data.get('price')
        price = self.cleaned_data['price']
        
        # 가격이 숫자인지 확인
        if not re.match(r'^\d+(\.\d{1,2})?$', price):
            raise ValidationError('올바른 가격을 입력해주세요.')
        
        # 최대 8자리 체크
        if len(price) > 8:
            raise ValidationError('가격은 최대 8자리여야 합니다.')
        
        return price