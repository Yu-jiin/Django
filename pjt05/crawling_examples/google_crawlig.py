from bs4 import BeautifulSoup
import requests

def crawling_basic():
    # 가져올 url 문자열로 입력
    url = 'https://www.google.com/search?q=%ED%83%95%EC%88%98%EC%9C%A1&oq=%ED%83%95%EC%88%98%EC%9C%A1&gs_lcrp=EgZjaHJvbWUqDQgAEAAY4wIYsQMYgAQyDQgAEAAY4wIYsQMYgAQyCggBEC4YsQMYgAQyDQgCEAAYgwEYsQMYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQgyMDM2ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8'  

    response = requests.get(url)  

    html_text = response.text

    with open('soup.txt', 'w', encoding='utf-8') as file:
        file.write(html_text)


crawling_basic()