

1. 파이썬에서은 객체지향프로그래밍 언어입니다. 파이썬에서 기본적으로 정의된 클래스 5개만 작성해보세요.

int tuple set dict str

2. 다음 중 틀린 것은? 3

과거 절차지향 프로그램

클래스 순서 상관없이 필요한 것만 씀



pip install -U flask flask 설치

from flask import Flask

app = Flask(__name__)

@app.route('/')  홈 주소



from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():

​    return '안녕하세요'



터미널 flask run