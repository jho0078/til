-- 스키마 작성
CREATE TABLE movies (
'영화코드' INTEGER PRIMARY KEY,
'영화이름' TEXT,
'관람등급' TEXT,
'감독' TEXT,
'개봉연도' INT,
'누적관객수' INT,
'상영시간' INT,
'제작국가' TEXT,
'장르' TEXT
);

-- csv 모드
.mode csv

-- boxoffice.csv movies 테이블 생성
.import boxoffice.csv movies

-- 맨 위에 헤더 표시
.headers on

-- 좌측 정렬
.mode column

-- 전체 출력
SELECT * FROM movies;