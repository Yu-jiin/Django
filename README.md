Django !!  
배틀싸피 done 

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

---

3. 앱 생성 및 등록

```bash
# 가능하지만 쓰지 않는다.
# $ django-admin startapp my_app

# 1. 앱 생성 -> 등록
$ python manage.py startapp my_app


```



> 프로젝트는 프로젝트 생성 명령어로 만듬

- 이때 app은 없었음
  > 그러고, 추가로 app 생성함
- 이건.. 프로젝트랑 완전 별개 폴더이다.
  > 프로젝트가 방금 만들어진 app의 존재를 알리가 없음 .
  > settings.py의 INSTALLED_APPS에 'my_app' 등록해야함 !!!
  >
  > 
```

# 도파민아저씨와 포항피바다의 합작 프로젝트

## 1. 프로젝트 생성
- **레포지토리 만들기**: `git_flow_practice` (README 포함, 프리마켓으로 생성)
- **클론 받기**: 레포지토리 클론

## 2. 멤버 초대
- 팀원 및 강사님 초대

## 3. 개발 환경 설정
1. **VS 코드 열기**
2. `.gitignore` 파일 생성 (https://www.toptal.com/developers/gitignore 참조)
3. 가상 환경 생성 및 활성화
   ```bash
   py -m venv venv
   source venv/Scripts/activate  # Windows 경우
   # 또는
   source venv/bin/activate       # Mac/Linux 경우
필수 패키지 설치
bash
코드 복사
pip freeze > requirements.txt
브랜치 생성 및 전환
bash
코드 복사
git branch dev
git switch dev
변경사항 확인 및 커밋
bash
코드 복사
git status
git add .
git commit -m "기본 환경 설정 문서"
git log --oneline
4. Django 앱 생성 및 설정
프로젝트 및 앱 생성
bash
코드 복사
django-admin startproject pjt .
python manage.py startapp articles
앱 등록: pjt/settings.py 파일에서 INSTALLED_APPS에 articles 추가
모델 등록 및 마이그레이션
bash
코드 복사
python manage.py makemigrations
python manage.py migrate
Django Extensions 추가: INSTALLED_APPS에 'django_extensions' 추가
Django 쉘 사용
bash
코드 복사
python manage.py shell_plus
article = Article(title='test')
article.save()
exit()
데이터 덤프 및 fixtures 설정
bash
코드 복사
python manage.py dumpdata --indent=4 articles > articles.json
mkdir articles/fixtures
mv articles.json articles/fixtures/
변경사항 커밋 및 푸시
bash
코드 복사
git add .
git commit -m "초기 데이터 추가"
git push -u origin dev
팀원 작업 흐름
레포지토리 클론

git pull origin dev로 최신 코드 가져오기
가상 환경 설정 및 패키지 설치
bash
코드 복사
python -m venv venv
pip install -r requirements.txt
새로운 브랜치 생성

git branch accounts 후 git switch accounts로 이동
앱 생성 및 설정
bash
코드 복사
python manage.py startapp accounts
INSTALLED_APPS에 accounts 추가
AUTH_USER_MODEL 설정
슈퍼유저 생성 및 데이터 덤프

bash
코드 복사
python manage.py createsuperuser
python manage.py dumpdata --indent=4 accounts > users.json
mkdir accounts/fixtures
mv users.json accounts/fixtures/
변경사항 커밋 및 푸시

bash
코드 복사
git add .
git commit -m "accounts 모델 추가"
git push origin accounts
머지 리퀘스트 생성: 프로젝트 레포지토리에서 accounts 브랜치를 dev로 머지

추가 설정 및 작업
설정 브랜치 생성

bash
코드 복사
git branch settings
git switch settings
BASE_DIR / 'templates' 추가 후 저장
변경사항 커밋 및 푸시
bash
코드 복사
git add .
git commit -m "settings 수정"
git push origin settings
다른 브랜치와의 통합

bash
코드 복사
git pull origin accounts
아티클 브랜치 작업

bash
코드 복사
git branch articles
git switch articles
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata users.json
아티클 생성 및 데이터 덤프

bash
코드 복사
python manage.py shell_plus
user = User.objects.get(pk=1)
article = Article(user=user, title='test')
article.save()
exit()
python manage.py dumpdata --indent=4 articles > articles.json
최종 커밋 및 푸시

bash
코드 복사
git add .
git commit -m "user article 1:N 관계 추가"
git push origin articles
