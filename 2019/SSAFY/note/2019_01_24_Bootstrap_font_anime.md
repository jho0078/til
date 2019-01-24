1. 외부 폰트 받아오기

* google fonts 사이트 -> 원하는 폰트 골라서 + 클릭 -> 아래 배너 열어서

* EMBED ->  @IMPORT -> @import url('https://fonts.googleapis.com/css?family=**Black+Han+Sans**&subset=korean'); 복사 후 style 태그 안에 붙여넣기

* specify in CSS 의 font-family: 'Black Han Sans', sans-serif; 복사 -> style 태그 안에 아래 형식으로 집어넣음

```html
body {
        font-family: 'Black Han Sans', sans-serif;
    }
```



#### 2. animate css

* 원하는 항목 선택 후 view on github 클릭 -> Usage의 CNDJS 버전 복사 후 bootstrap CDN 아래에 붙여넣기

```html
<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.min.css">
</head>
```



#### 3. font awesome

* free -> svg 선택 -> script복사 후 body의 bootstrap script 아래에 붙여넣기

* 사이트에서 원하는 icon 검색 ->  i class 태그 복사 후 div 태그 안에 넣어서 사용

```html
<div class="container">
    <i class="fab fa-cc-apple-pay fa-5x faa-bounce animated"></i>
</div>
```

* 사이즈 조절

docs -> sizing icon -> 원하는 사이즈 찾아서 class 안에  작성 ex) fa-5x



#### 4. Font-Awesome Animation - I-lin

* Minified CSS 클릭 -> 전체 복사 -> font_animation.min.css 파일 만들어서 붙여넣기

* 본 html 파일에 CDN작성

```html
<link rel="stylesheet" href="font_animation.min.css">
```

* Usage에서 원하는 애니메이션 글자 복사 후 class에 추가

  ```html
  <div class="container">
      <i class="fab fa-cc-apple-pay fa-5x faa-bounce animated"></i>
  </div>
  ```

  

  