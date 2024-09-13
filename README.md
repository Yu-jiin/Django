Django

1. django 시작하기

```bash
# 1. 프로젝트 시작하자마자 gitignore 생성하기
$ code .gitignore

# 2. 가상 환경 생성하기
$ python -m venv venv

# 3. 가상환경 활성화 하기
$ source venv/Scripts/Activate

# 4. 프로젝트 진행에 필요한 라이브러리 설치하기
$ pip install django
우리는 파이썬 버전 3.9.x 쓰고 있습니다.
'pip install django' 명령어 실행
설치되는 장고 버전은 4.2.x 버전입니다.

# 5. 현재 버전을 다음에도 똑같이 유지하기위해 기록
$ pip freeze > requirements.txt

```

2. django 프로젝트 생성하기

```bash
$ django-admin startproject my_pjt .


# 서버 켜기
$ python manage.py runserver
# 서버 끄기
$ ctrl + c
```
