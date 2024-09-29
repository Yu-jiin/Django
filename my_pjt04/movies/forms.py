from django import forms
from .models import Movie

class MovieForm(forms.form):
    class Meta:
        model = Movie
        fields = '__all__'