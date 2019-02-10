-- CREATE
INSERT INTO users (username, email)
VALUES ('junho', 'example@gmail.com');

user = User(username='junho', email='example@gmail.com')

--READ
SELECT * FROM users;
users = User.query.all()

SELECT * FROM users WHERE username='junho';
users = User.query.filter_by(username='junho').all()

SELECT * FROM users WHERE username='junho' LIMIT 1;
users = User.query.filter_by(username='junho').first()

-- None(값이 없다면 None이 뜬다.)
miss = User.query.filter_by(username='ssafy').first()

-- Get one by id
-- PRIMARY KEY만 get으로 가져올 수 있다.
SELECT * FROM users WHERE id=1;
users = User.query.get(1)

-- LIKE
users = User.query.filter(User.email.like('%exam%')).all()
-- 세번째 것 출력
users = User.query.limit(1).offset(2).all()

-- UPDATE
user = User.query.get(1)
user.username = 'ssafy'
db.session.commit()
user.username

-- DELETE
user = User.query.get(1)
db.session.delete(user)
db.session.commit()


