-- 영화 극한직업 테이블에 추가
INSERT INTO movies
VALUES(20182530, '극한직업', '15세이상관람가', '이병헌',
20190123, 3138467, 111, '한국', '코미디');

-- 영화코드가 20040521인 데이터 출력, 삭제
SELECT * FROM movies WHERE 영화코드=20040521;

DELETE FROM movies WHERE 영화코드=20040521;

-- 영화코드가 20185124인 데이터 출력
SELECT * FROM movies WHERE 영화코드=20185124;

-- 영화코드가 20185124인 데이터의 비어있는 컬럼에 '없음'을 입력 
UPDATE movies
SET 감독='없음'
WHERE 영화코드=20185124;

-- 해당 데이터의 감독이 변경되었는지 확인
SELECT * FROM movies WHERE 영화코드=20185124;