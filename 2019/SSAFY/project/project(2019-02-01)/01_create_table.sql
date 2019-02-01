CREATE TABLE movies (
'영화코드' INTEGER PRIMARY KEY,
'영화이름' TEXT,
'관람등급' TEXT,
'감독' TEXT,
'개봉연도' INTEGER,
'누적관객수' INTEGER,
'상영시간' INTEGER,
'제작국가' TEXT,
'장르' TEXT
);

-- 1-1
.read 01_create_table.sql

-- 1-2 header와 mode 설정
.import boxoffice.csv movies
.mode csv
.headers on
.mode column

-- 1-3 전체 출력
SELECT * FROM movies;