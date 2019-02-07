import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User

# app이라는 instance 생성
app = Flask(__name__)

# flask app 에 sqlalchemy 관련 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# ['SQLALCHEMY_TRACK_MODIFICATIONS'] = True : sqlalchemy 데이터베이스 객체 수정
# 및 신호 방출 등을 추적합니다. 과도한 메모리를 사용하기 때문에 False

# sqlalchemy 초기화
# db= SQLAlchemy(app)
db.init_app(app)

migrate =  Migrate(app, db)

# flask db init
# flask db migrate
# flask db upgrade

@app.route('/')
# 뷰 함수를 쓰면 라우트를 리턴한다.
# users라는 리스트를 받아옴
def index():
    users = User.query.all()
    # return redirect(url_for('index'), name=name)
    return render_template('index.html', users=users)

@app.route('/users/create')
def create():
    username = request.args.get('username')
    email = request.args.get('email')
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/users/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))
    
# id 받아서 넣어준 다음 edit.html로 이동
@app.route('/users/edit/<int:id>')
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)


@app.route('/users/update/<int:id>')
def update(id):
    user = User.query.get(id)
    username = request.args.get('username')
    email = request.args.get('email')
    
    user.username = username
    user.email = email
    db.session.commit()
    return redirect(url_for('index'))
    # return redirect('/')



# 항상 맨 아래에
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)