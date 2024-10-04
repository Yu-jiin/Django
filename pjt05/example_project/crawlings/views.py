from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .models import Article

def get_google_data(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    # Chrome 옵션 설정
    options = Options()
    options.add_argument('--headless')  # 브라우저를 숨기고 백그라운드에서 실행

    # 크롬 브라우저가 열린다. 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source 
    soup = BeautifulSoup(html, "html.parser")

    # div 태그 중 g 클래스를 가진 모든 요소 선택
    g_list = soup.select("div.g")

    titles = []
    # 해당 요소를 반복하며
    for g in g_list:
        # 요소 안에 LC20lb MBeuO DKV0Md 클래스를 가진 특정 요소 선택
        title = g.select_one(".LC20lb.MBeuO.DKV0Md")
        # 요소가 존재 한다면
        if title is not None:
            title_text = title.text
            titles.append(title_text)
    return titles



def index(request):
    if request.method == 'POST':
        results = []
        query = request.POST.get('query')
        titles = get_google_data(query)
        print(titles)

        for title in titles:
            # Article.objects.create(query=query, title=title)
            # # 중복 제거 
            # if Article.objects.filter(query=query, title=title).exists():
            #     Article.objects.create(query=query, title=title)

            article, created_article = Article.objects.get_or_create(query=query, title=title)
    
    context = {
        'results' : Article.objects.all()
    }


    return render(request, 'crawlings/index.html', context)