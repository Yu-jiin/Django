from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    works = Todo.objects.all()
    context = {
        'works': works
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, pk):
    work = Todo.objects.get(pk=pk)
    context = {
        'work': work
    }
    return render(request, 'todos/detail.html', context)