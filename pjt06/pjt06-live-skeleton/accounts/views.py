from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import CustomUserCreationForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        pass
    else:
        form = CustomUserCreationForm()
    context= {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        pass
    else:
        pass

@require_http_methods(['POST'])
def logout(request):
    pass