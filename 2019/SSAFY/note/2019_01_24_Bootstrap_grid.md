# Bootstrap_grid (2019-01-23)

bootstrap은 column을 12개로 나누어 놓았다.

div class에 col-1을 지정해 주면 전체 column에서 1/12만큼의 영역을 사용한다.



#### 내부 div들을 한 줄(row)에 출력한다.

```html
<div class="row">
    <div class="square col-1">.col-1</div>
    <div class="square col-1">.col-1</div>
    <div class="square col-1">.col-1</div>
</div>
```



#### 반응형 고정폭 컨테이너

```html
<div class="container">
```

#### 최대폭 컨테이너

```html
<div class="container-fluid">
```