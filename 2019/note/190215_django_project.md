# Django project



### 1. app 분리

1. settings.py

   > app 추가

```python
INSTALLED_APPS = [
	...
	'home.apps.HomeConfig',
    'utilities.apps.UtilitiesConfig',
]
```

2. urls.py 분리

> 프로젝트 내에 있는 urls.py 를 분리한다.
>
> app마다 app 폴더 내에 urls.py를 생성 
>
> 프로젝트에서는 각 app의 urls.py로 연결되도록 지정해준다. 

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('utilities/', include('utilities.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
]
```



> app의 urls.py 에서는 views 접근 방식이 달라지기 때문에 import를 아래와 같이 바꿔준다.
>
> 경로설정에서는 utilities/를 빼고 뒷주소부터 설정해준다.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')    
]
```



### 2. templates와 static의 분리

* templates

> django는 template을 호출할 때 여러 app들의 template들을 하나의 폴더에 모은 후 에 해당 template을 불러온다. 때문에 app은 다르지만 이름이 같은 template들을 불러올 때 문제가 생긴다.
>
> 이를 해결하기 위해 templates 폴더 안에 app의 이름과 같은 폴더를 생성 후 그 안에 template들을 저장한다.

* static

> css와 image 또한 template처럼 이름 충돌을 방지하기 위해 static 폴더 내에 app의 이름을 가진 폴더를 만들어 그 안에 저장한다.

```
├── 05_detail
│   ├── db.sqlite3
│   ├── detail
│   │   ├── static
│   │   │   └── detail
│   │   │       ├── images
│   │   │       │   ├── favicon.jpg
│   │   │       │   └── preview.jpg
│   │   │       └── stylesheets
│   │   │           └── style.css
│   │   ├── templates
│   │   │   └── detail
│   │   │       ├── my_site.html
```



> 그 다음 template 호출 경로를 모두 변경한다.

```
return render(request, 'home/index.html')
```



### 3. base inheritance

#### 3.1 base.html

> 상속을 위한 하나의 base template을 여러 app에서 사용하려면 프로젝터 폴더에 templates폴더를 생성하여 그 안에 base.html을 넣는다.

```
├── django_project02 (프로젝터 폴더)
│   │   ├── templates
│   │   │   └── base.html
```

* settings.py

> DIRS 경로를 수정해준다.

```
'DIRS': [os.path.join(BASE_DIR, 'django_project02', 'templates')],
```



#### 3.2 base inerhitance

* base.html

  > block-endblock 으로 닫힌 부분을 제외한 것이 상속된다.

```html
<head>
    {% block head %}{% endblock %}
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    {% block body %}{% endblock %}
</body>
```

* index.html

  > block-endblock 사이에 추가하고 싶은 내용을 넣는다.
  >
  > 기본적으로 덮어쓰기 형식이다.

```html
{% extends 'base.html' %}

{% block title %}Index{% endblock %}

{% block body %}
    <header class="d-flex justify-content-center align-items-center">
        <h1>Header</h1>
    </header>
{% endblock %}
```

* css와 image 불러오기

```html
{% load static %}

{% block css %}
    <link rel="stylesheet" href="{% static 'detail/stylesheets/style.css' %}" type="text/css"/>
{% endblock %}

{% block body %}
<img src="{% static 'detail/images/preview.jpg' %}" alt="image" style="height:200px;width:300px"></img>
{% endblock %}
```



### 4. footer

> 부모에 `d-flex`를 먹여야 오른쪽 영역이 끝까지 넓어져 자식태그에 `ml-auto`가 적용될 수 있다.

```html
<footer class="fixed-bottom d-flex">
    <a>SSAFY</a>
    <a href="#top" class="ml-auto">상단으로 올라가기</a>
</footer>
```



### 5. card

> 왼쪽카드는 고정, 오른쪽 카드는 스크롤에 따라 이동

```html
<div class="container">
    <div class="row">        
        <div class="col-6">
        	<div class="card position-fixed" style="width: 18rem;">
                ...
            </div>
        </div>
        <div class="col-6">
            <div class="card" style="width: 18rem;">
                ...
            </div>
            ...
        </div>
    </div>
</div>                
```



### 6. favicon

> 임의의 이미지를 favicon으로 사용할 수 있다.

```html
<link rel="shortcut icon" href="{% static 'detail/images/favicon.jpg' %}" type="image/x-icon" />
```



### 7. 태그 내 스타일 변경

```html
<img src="..." style="height:300px;width:300px">
```

 

### 8. 지정경로를 제외한 다른 요청이 들어오면 보여줄 404페이지

> django 는 위에서부터 경로를 읽어 내려가기 때문에 404페이지 경로는 가장 밑에 작성해야 한다.

```python
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('mypage/', views.mypage, name='mypage'),
    path('', views.index, name='index'),    
    path('<str:not_found>/', views.not_found, name='not_found'),
]
```











