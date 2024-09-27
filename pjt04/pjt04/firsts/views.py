from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
# Create your views here.
def index(request):
    x = [1,2,3,4,5]
    y = [1,2,3,4,5]
    plt.plot(x,y)   # 그래프 그리기
    plt.title('Test Graph')
    plt.ylabel('y label')
    plt.xlabel('x label')
    # plt.show()      # 예전 출력 방식

    # 버퍼를 활용 -> 임시 저장 공간


    return render(request, 'firsts/index.html')