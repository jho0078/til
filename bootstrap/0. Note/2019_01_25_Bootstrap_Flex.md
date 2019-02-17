# Flex



## 1. flex-direction

* 축 방향을 설정할 수 있으며 거꾸로 배열하는 것도 가능하다.

```html
<style>
        /* 기존 블럭 속성을 인라인 속성으로 바꿈 */
        .container {
            display: flex;
            display: inline-flex;
            /* 브라우저 높이 비율로 크기 조절 */
            height: 100vh;
            border: 10px solid royalblue;
            /* 축 방향 바꾸기? row가 기본값*/
            flex-direction: row;
            flex-direction: column;
            flex-direction: row-reverse;
            flex-direction: column-reverse;
            /* 감쌀지 화면 너머 보내버릴지? wrap이 기본값*/
            flex-wrap: wrap;
            flex-wrap: nowrap;
            flex-flow: row nowrap;
        }
</style>
```



## 2. flex-grow

* 컨테이너 폭에 꽉차게 맞춰준다.

> 아래의 경우 item1, item2, item3를 컨테이너 안에 가로로 배열하였다.
>
> 세 박스의 가로 크기의 합이 컨테이너보다 작기 때문에 남는 공간이 생기는데 flex-grow를 사용하여
>
> 남는 공간을 박스에 배분할 수 있다.
>
> 아이템의비율을 원래 남는 부분에서 지정된 비율만큼 계산해서 더해준다.
>
> 남은 픽셀에서 item2에 2/5만큼, item3에 3/5만큼 더해준다.

```html
<style>
    .item {
        width: 300px;
        height: 200px;
    }	
    .item2 {
        flex-grow: 2;
    }
    .item3 {
        flex-grow: 3;
    }
</style>
```



## 3. justify -content

* flex item의 x축 정렬과 간격을 제어한다.

```html
<style>
    .container {
        display: flex;
        height: 100vh;
        border: 10px solid royalblue;

        /* start: 기본값 end: 오른쪽으로 붙는다. 순서유지 */
        /* justify content는 x축 정렬 */
        justify-content: flex-start;
        justify-content: flex-end;
        justify-content: center;
        /* 남는 공간을 조절하고 싶다면 margin을 사용한다 */
        justify-content: space-between; /* 양 끝에 공간이 남지 않는다 */
        justify-content: space-around;  /* 양 끝에 공간이 남는다 */
                                        /* 내부 공간크기가 외부 공간크기의 2배 유지 */
    }
</style>
```



## 4.  align-items

* flex item의 y축 정렬과 간격을 제어한다.

```html
<style>
    .container {
        display: flex;
        height: 100vh;
        border: 10px solid royalblue;
        
		/* align-items는 y축 정렬 */
        align-items: flex-start;
        align-items: flex-end;
        align-items: center;
        align-items: stretch; /* 늘림 */
        align-items: baseline; /* 포함하고 있는 문자열을 기준으로 정렬 */
        
        /* 상위 flex-container에 적용되어 있는 align-items 속성과 다른 효과를 하위에
        개별적으로 적용하고 싶을 때 사용(우선순위 더 높음) */ 
        align-self: flex-auto; /* flex container에 적용되어 있는 속성 그대로 사용 */
        align-self: flex-start;
        align-self: flex-end;
        align-self: center;
        align-self: stretch;
        aligh-self: baseline;
    }
</style>	
```



## 5. order

* item의 정렬 순서를 정할 수 있다
* 아무것도 지정하지 않으면 0이 기본값이다.
* 아래의 경우 item4 > item > item8 > item2 순으로 배열된다.

```html
<style>   
    .item {
        order: 0;
    }
       
    .item2 {
        order: 2;
    }

    .item8 {
        order: 1;
    }

    .item4 {
        order: -1;
    }    
</style>
```

