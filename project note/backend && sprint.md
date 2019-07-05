## 백엔드



node.js

mvc 패턴 작성 방법

### MVC 패턴

하나의 애플리케이션, 프로젝트를 구성할 때의 디자인 패턴으로, 그 구성요소를 Model, View, Controller 세 가지로 구분한 패턴

![image](https://user-images.githubusercontent.com/46305309/60699068-37cc6e80-9f2d-11e9-9168-f2fc7462f651.png)

Controller : 중앙 통제

Model : 연산처리, DB, 컨트롤러에서 요청이 들어오면 연산처리 후 정보를 return

View : 사용자에게 보여지는 모습을 제공



서버 어떻게 키는지

express - nodejs에서 사용할 라이브러리



### Node 의 express 를 이용한 MVC 구축

1. Node.js 설치

2. npm install --save express

   > --save 는 의존성 주입으로, 다른 사람이 내가 개발한 걸 테스트할 경우 npm install 로 필요한 모듈을 한번에 다운 받을 수 있게 모듈에 대한 의존성을 주입시킨다. 
   >
   > **-g  전역 설치 , --save 프로젝트 단위 설치 , --save-dev 프로젝트 단위 개발툴 설치 ( 배포 X )**

### mongodb 

1. NoSQL 데이터베이스
   * Document는 JSON objects 형태의 key-value의 쌍으로 이루어진 테이터로 구성된다.
2. 동적 스키마를 가진다. (RDMS 처럼 고정 스키마가 없다.)
   * 하나의 Collection 내의 document 가 각각 다른 스키마를 갖을 수 있다.
   * document가 각자의 고유한 field를 가질 수 있다.

3. join 이 효과적이지 않다.
   * 하나의 document에 포스트의 sub document로 댓글을 포함시킨다. (빠른 query를 가능하게 한다.)
4. Sharding 클러스터 구축이 가능하다. (여러 개의 데이터베이스에 데이터를 분할)



## 애자일

### 스크럼 기법

각자 어떤 task를 했고 다음에 어떤 것을 할지

task를 달성하지 못했다면 왜 못했고 어떻게 할 생각인지

* 스크럼 마스터

조에서 스크럼 통합 후  조 마스터끼리 똑같이 진행



프로젝트 진행 중 여러 개의 스프린트 진행

지라에서 스프린트를 나눠준다

스트린트 내에서 여러 개의 task를 진행 - 플래닝 포커

팀별로 하나의 스프린트에서 몇개의 task를 달성했는지 파악 후 다음 스프린트 때 task 개수를 조정

스프린트 주기는 1주 혹은 2주

