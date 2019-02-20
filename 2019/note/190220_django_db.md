

#### 0. 복습

```
pyenv virtualenvs
pyenv local django-venv
django-admin startproject crud .
#settings.py
ALLOWED_HOSTS = ["*"]
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
c9 open .gitignore
python manage.py startapp boards
models.py 작성
python manage.py makemigrations boards
python manage.py migrate
```



#### 1. 테이블 생성

```python
# boards라는 테이블 설계도를 생성
python manage.py makemigrations boards
Migrations for 'boards':
  boards/migrations/0001_initial.py
    - Create model Student
python manage.py migrate

# boards 0001을 보겠다
python manage.py sqlmigrate boards 0001

# db에 table 생성정보 넣기
python manage.py migrate

# db에 들어갔는지 확인
sqlite3 db.sqlite3
```



#### 2. 장고 orm (shell)

인스턴스를 이용한 테이블 값 추가

```python
# orm 진입
python manage.py shell
>>> from boards.models import Board

# table 전체 목록 보기
>>> Board.objects.all()

# 인스턴스 생성하여 테이블 수정
>>> board = Board()
>>> board.title = 'first'
>>> board.content = 'django!'
>>> board.save()

# 나가기
>>> exit()
```



확장 프로그램 설치

```python
pip install django-extensions

# settings.py에 추가
INSTALLED_APPS = [
	'django_extensions',
]

# 진입
python manage.py shell_plus

# 테이블 추가
>>> board = Board(title='second', content='django!!')
>>> board.save()
>>> Board.objects.all()
<QuerySet [<Board: 1: first>, <Board: 2: second>]>

>>> Board.objects.create(title='third', content='django!!!')
<Board: 3: third>
```



조건에 따른 탐색

```python
# 시간 출력
board.created_at

# 입력값의 제한에 대해 출력
board.full_clean()

# 조건에 따른 탐색
Board.objects.filter(title='first').all()
Board.objects.filter(title='first').first()

board = Board.objects.get(pk=1)
board = Board.objects.filter(id=1)

boards = Board.objects.filter(title__contains='fi').all()
boards = Board.objects.filter(title__startswith='fi')
boards = Board.objects.filter(content__endswith='!')

# 내림차순으로 정렬
boards = Board.objects.order_by('-title').all()
```



#### 3. admin

```
python manage.py createsuperuser
```



```python
# admin.py
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'birthday', 'age',)

admin.site.register(Student, StudentAdmin)
```

