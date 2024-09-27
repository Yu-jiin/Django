from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = '__all__'

        widgets = {
            'location': forms.TextInput(attrs={'placeholder':'제주도'}),
            'plan' : forms.Textarea(attrs={'placeholder':'ex) 슉.슈슉.'}),
            'start_date': forms.TextInput(attrs={'placeholder':'ex)2022-02-22'}),
            'end_date': forms.TextInput(attrs={'placeholder':'ex)2022-02-22'}),
        }
    # location = forms.CharField(
    #     label='Location',
    #     widget=forms.TextInput(
    #         attrs={
    #             'placeholder' : 'ex) 제주도',
    #             'maxlength' : 10,
    #         }
    #     ),
    # )