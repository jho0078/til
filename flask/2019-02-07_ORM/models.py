from flask_sqlalchemy import SQLAlchemy

# sqlalchemy 초기화
db= SQLAlchemy()

# TABLE 만들기
# nullable=False : Not null(값이 비어있을 수 없다.)
# unique=True : 중복값 없도록 설정
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User '{self.username}'>"
        
# sqlite 상에서 했던 명령(위와 같다.)    
# CREATE TABLE users
# id INTEGER PRIMARY KEY,
# username TEXT,
# email TEXT
# );