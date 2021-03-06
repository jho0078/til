## Django

- 다소 독선적

  > 독선적 (Opinionated) : 개발자의 자유도가 적다. 보다 안정적
  >
  > 관용적 : 개발자의 자유도가 높다.

- 파이썬 사용



### 0. 준비

1. pyenv 설치

   > pyenv : 프로젝트 별로 각각 맞는 다양한 python 버전으로 실행해 볼 수 있도록 환경 제공

   ```python
   # install pyenv
   git clone https://github.com/pyenv/pyenv.git ~/.pyenv
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
   source ~/.bashrc
   pyenv install 3.6.7
   pyenv global 3.6.7
   pyenv rehash
   
   # 파이썬 설치 확인
   jho0078:~/workspace $ python -V
   Python 3.6.7
   ```

2. virtualenv 설치

   > virtualenv : python 프로젝트마다 각각의 가상환경을 만들어 준다.

   ```python
   # install pyenv-virtualenv
   git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
   echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. git 설정

   ```python
   jho0078:~/workspace $ git config --global user.name 'jho0078'
   jho0078:~/workspace $ git config --global user.email "jho0078@gmail.com"
       
   # 확인
   jho0078:~/workspace $ git config --global --list
   ```

4. 가상환경 생성, 폴더 생성, 장고 설치

   ```python
   # 가상환경 생성
   jho0078:~/workspace $ pyenv virtualenv 3.6.7 django-venv
   jho0078:~/workspace $ pyenv virtualenvs  # 확인
   
   # 폴더생성
   jho0078:~/workspace $ mkdir PROJECT01
   jho0078:~/workspace $ cd PROJECT01
   
   # 가상환경 내 장고 설치
   jho0078:~/workspace/PROJECT01 $ pyenv local django-venv 
   (django-venv) jho0078:~/workspace/PROJECT01 $ pip install django 
   (django-venv) jho0078:~/workspace/PROJECT01 $ pip install --upgrade pip
   ```

5. gitignore

   ```python
   (django-venv) jho0078:~/workspace/PROJECT01 $ touch .gitignore
   (django-venv) jho0078:~/workspace/PROJECT01 $ ls -al #파일 있는지 확인
   ```

   > https://www.gitignore.io/api/django 에서 전체 내용 복사 후 .gitignore 파일에 붙여넣기



### 1. Django start

#### 1.1 장고 프로젝트

1. 프로젝터 생성

   > django, test, class, django-test 등은 프로젝트 이름으로 사용할 수 없다.

   ```python
   # 프로젝트 생성(이름: django_intro)
   # 마지막 .을 붙이면 현재 위치에 만든다.
   (django-venv) jho0078:~/workspace/PROJECT01 $ django-admin startproject django_intro .
   ```

   

2. 서버 실행

   ```python
   ALLOWED_HOSTS = ['django-intro-jho0078.c9users.io'] 
   ALLOWED_HOSTS = ["*"]
   ```

3. gitignore 설정

   ```python
   (django-venv) jho0078:~/workspace/PROJECT01 $ touch .gitignore
   (django-venv) jho0078:~/workspace/PROJECT01 $ ls -al #파일 있는지 확인
   ```

4. TIMEZONE/LANGUAGE_CODE 설정

   ```python
   # 한국어/시간 설정
   LANGUAGE_CODE = 'ko-kr'
   TIME_ZONE = 'Asia/Seoul'
   ```

5. 로켓 페이지 한글화 확인

   > python manage.py runserver $IP:$PORT 

6. 프로젝트 구조

   > tree : 폴더 구조를 볼 수 있다.

   `manage.py` : 장고 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

   `프로젝트이름폴더` : 디렉토리 내부에는 프로젝트를 위한 실제 파이썬 패키지들이 저장된다. 이 디렉토리 내의 이름을 이용하여 프로젝트 어디서나 파이썬 패키지들을 import 할 수 있습니다.

   `settings.py` : 현재 장고 프로젝트의 모든 환경과 구성을 저장한다.

   `__init__.py` : 파이썬으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일

   `urls.py` : 현재 장고 프로젝트의 URL 선언을 저장. 사이트의 URL과 VIEWS의 연결을 지정

   `wsgi.py` : 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점



#### 1.2 장고 어플리케이션(APP)

* 실제 특정한 역할을 하는 친구가 바로 APP
* 프로젝트는 이러한 어플리케이션의 집합
* 하나의 프로젝트는 여러 개의 어플리케이션을 가질 수 있다.
* 각각의 어플리케이션은 MTV 패턴으로 구성되어 있다.

1. 어플리케이션 만들기

   ```python
   (django-venv) jho0078:~/workspace/PROJECT01 $ python manage.py startapp home
       
   # settings.py
   # INSTALLED_APPS 리스트에 추가(가장 아래에 추가)
   # project와 app의 연결(apps.py에서 확인 가능)
   INSTALLED_APPS = [
       'home.apps.HomeConfig',
   ]
   ```

2. 어플리케이션 구조

* `admin.py` : 관리자용 페이지 커스터마이징 장소
* `apps.py` : 앱의 정보가 있는 곳. 우리는 수정할 일이 없다.
* `models.py` : 앱에서 사용하는 Model을 정의하는 곳
* `tests.py ` : 테스트 코드를 작성하는 곳
* `views.py` : 뷰들이 정의되는 곳. 사용자에게 어떤 데이터를 보여줄지 구현되는 곳

3. 어플리케이션 등록

   > home > apps.py > class HomeConfig()
   >
   > home.apps.HomeConfig 등록
   >
   >  혹은 그냥 `home` 이라고 작성 가능하다. 다만 추후에 자세한 설정을 찾을 수 없다.



### 2. MTV 패턴

### 3. views - urls

코드 작성 순서

1. 처리할 views (controller)

2. 요청 urls

3. 결과를 보여줄 template 

4.  실행

   > python manage.py runserver $IP:$PORT

* HttpResponse 로 첫 리턴 값 출력해보기
* path(route, views, name) 2개의 필수 인수와 1개의 선택 인수
* 저녁 메뉴 리턴 실습



### 4. Template

* 장고에서 사용되는 템플릿들은  DTL(Django Template Language) 이다.

* jinja2와 문법이 유사하지만 다르다.

#### 4.1 Template Variable

* render()

  * render(request, template_name, context=None,

     content_type=None, status=None, using=None)

#### 4.2 Variable Routing

> value를 넘길 때는 딕셔너리 형태로 넘긴다.

```python
def hello(request, name):
	return render(request, 'hello.html', {'name' : name})
```



### 5. Form data(get/post)

POST 방식

- 보통 데이터 베이스 값을 넣을 때 사용
- 때문에 보안을 위해 값을 넘겨줄 때 토큰 값을 같이 넘겨줘야 한다.

```html
<form action="/home/user_create/" method="POST">        
    {% csrf_token %}
    <input type="text" name="nickname"/>
    <input type="text" name="password"/>
    <input type="submit" value="Submit"/>
</form>
```



````pthon
request.Get.get('data')
request.POST.get('data')
{% csrf_token %} 를 form 안에서 같이 보내줘야 한다.
````

> csrf 공격과 같은 보안과 관련된 사항은 settings에 MIDDLEWARE에 되어있다.
>
> 실제로 요청은 미들웨어 설정 사항들은 순차적으로 거른다. 응답은 아래에서 위로 거쳐서 응답이 리턴된다.



### 6. Template Inheritance

home.templates/base.html 생성

