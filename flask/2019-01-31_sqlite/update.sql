UPDATE classmate
SET name='강예원', address='제주'
WHERE id=3;

-- .read update.sql
-- SELECT * FROM classmate;

UPDATE classmate
SET name='박성주', address='제주'
-- and 는 사용할 수 없다.
WHERE id=1 or id=6;