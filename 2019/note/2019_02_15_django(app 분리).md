# app 분리



### 1. settings.py

```
'home.apps.HomeConfig',
    'utilities.apps.UtilitiesConfig',
]
```



### 2. urls.py

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





### 3. templates

> templates 폴더 안에 app의 이름을 가진 폴더를 생성 후 그 안에 template들을 저장한다.



```
return render(request, 'home/index.html')
```

