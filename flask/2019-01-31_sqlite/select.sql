-- 테이블 값 모두가져오기
SELECT * FROM classmate;

-- 테이블의 특정 컬럼만 가져오기
SELECT id, name FROM classmate;

-- 가져오는 ROW(레코드) 개수를 지정하기
SELECT id, name FROM classmate LIMIT 2;

-- 가져오는 ROW(레코드)의 시작점 지정하기
SELECT * FROM classmate LIMIT 1 OFFSET 2;

-- 특정한 값을 가진 row만 조회하기
SELECT * FROM classmate WHERE address='서울';


-- 서울에 사는 사람의 이름은?
SELECT name FROM classmate WHERE address='서울';

-- 보통 값을 지울 때는 유니크한 값인 id를 지운다
-- 새로 값을 추가한다면 지운 id에 들어가지 않고 뒷번호로 추가된다.  
DELETE FROM classmate WHERE id=3;

--중복없이 조회하기
SELECT DISTINCT age FROM classmate;
