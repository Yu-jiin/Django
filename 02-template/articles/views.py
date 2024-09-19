import random
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name' : 'alice' ,
        'ssafy' : {
            'key' : 'value'
        }
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'articles/dinner.html', context)