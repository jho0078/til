# 1. Grid system

* bootstrap은 12열의 그리드 시스템을 사용한다.
* 그리드를 만들려면 가장 상위에 container, 하위에 row, 그 다음 하위에 그리드를 사용해야 한다.

```html
<div class="container">
    <div class="row">
         <div class="square col-md-3 col-6"></div>
```



## Grid options

|                     | Extra small <576px | Small ≥576px | Medium ≥768px | Large ≥992px | Extra large ≥1200px |
| ------------------- | ------------------ | ------------ | ------------- | ------------ | ------------------- |
| Max container width | None (auto)        | 540px        | 720px         | 960px        | 1140px              |
| Class prefix        | `.col-`            | `.col-sm-`   | `.col-md-`    | `.col-lg-`   | `.col-xl-`          |



```html
<div class="square col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2"></div>
```



## offset

* 지정 크기만큼 요소를 왼쪽으로부터 떨어져 배치되게 한다.
* 아래의 경우 2의 크기를 가진 그리드가 왼쪽으로부터 5의 크기만큼 떨어져서 위치하게 된다.

```html
<div class="square offset-5 col-2">offset-5</div>
```



## container-fluid

- 너비가 정해지지 않아서 부모 요소의 너비에 따라 좌우된다.
- 주로 전체폭 레이아웃을 만들 때 사용한다.

```html
<div class="container-fluid">
```



# 2. 글자

### 1. 헤딩

* h1~h6 태그가 있다
* h2태그를 사용하면서 h1태그의 글자 스타일을 사용할 수 있다.

```html
<h2 class="h1">	
```

* mark, del, s, ins, u, small, strong, em 등의 태그가 있다.



### 2. 정렬 클래스

* text-left, text-right, text-center
* text-justify : 긴 문장의 좌우 끝을 정렬(톱니 현상 제거)
* text-nowrap : 문장을  한줄로 만들며 레이아웃의 범위를 벗어나게 한다.



### 3. 리스트

* ol(ordered list)로 묶으면 앞에 숫자가 목록 앞에 생성되고(순서 있는 목록)
* ul(unorderd list)로 묶으면 불릿 기호가 생성된다.(순서 없는 목록)
* 불릿 기호를 제거하려면 ul태그에 list-unstyled 클래스를 사용한다.

```html
<ul>목록</ul>
<ol>나이
    <li>24</li>
    <li>26</li>
</ol>
<ul>이름
    <li>아이유</li>
    <li>사나</li>
</ul>
```





