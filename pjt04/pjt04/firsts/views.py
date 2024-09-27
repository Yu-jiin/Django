from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
from .models import Weather
# io        : 입출력 연산을 위한 Python 표준 라이브러리
# BytesIO   : 메모리 내에서 이진 데이터를 파일처럼 다룰 수 있는 버퍼 제공 
# base64    : 텍스트 <-> 이진데이터 변환할 수 있는 모듈 
from io import BytesIO
import base64
plt.switch_backend('Agg')
# Create your views here.
def index(request):
    x = [1,2,3,4,5]
    y = [1,2,3,4,5]
    plt.clf()       # 그래프 초기화
    plt.plot(x,y)   # 그래프 그리기
    plt.title('Test Graph')
    plt.ylabel('y label')
    plt.xlabel('x label')
    # plt.show()      # 예전 출력 방식

    # 버퍼를 활용 -> 임시 저장 공간
    # 1. 비어있는 버퍼 생성
    buffer = BytesIO()
    # 2. 버퍼에 그래프를 저장 
    plt.savefig(buffer, format='png')
    # 3. 버퍼의 내용을 base64를 활용하여 인코딩
    # - 이미지 데이터(경로 포함)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    # print(image_base64)
    buffer.close()
    
    context = {
        'chart_image' : f'data:image/png;base64,{image_base64}'
    }

    return render(request, 'firsts/index.html', context)


import pandas as pd

def example(request):
    # 1. csv 파일 읽기 pandas
    # 2. DB에 저장
    #   - 중복된 데이터 저장 X 
    #   - 필드를 데이터를 보고 생성하는 연습
    #   - DB 관련 로직 구현 연습 
    csv_path = 'firsts/data/test_data.csv'
    df = pd.read_csv(csv_path)
    # print(df)
    for index, row in df.iterrows():
        # 중복제거
        if not Weather.objects.filter(date=row['Date']).exists():
            continue
        weather = Weather(
            date=row['Date'],
            temp_avg_f=row['TempAvgF'],
            events=row['Events'] if pd.notna(row['Events']) else ""
        )
        weather.save()

    weathers = Weather.objects.all()
    context = {
        'weathers': weathers,
    }

    return render(request, 'firsts/example.html', context)