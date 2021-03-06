# 190620 | 자기 주도 학습



# GIT

### 1. 무엇인가?

 여러명의 개발자가 특정 프로젝트를 각자의 컴퓨터로 협업하여 개발하면서 버전을 관리할 수 잇는 시스템으로 분산 버전 관리 시스템이라 한다. 

### 2. 왜 필요한가?

 프로젝트를 여러명의 팀원이 동시에 작업한다면 하루가 다르게 업데이트가 될 것이다. 매일 혹은 시간 단위로 업데이트되는 파일들을 공유하고 통합하기 위함이 가장 큰 목적이다. 

 프로젝트 도중 팀원 중 누군가가 잘못하여 특정 부분을 덮어 썼거나 업데이트 하지 못하고 이전 버전의 문서로 작업했을 경우가 빈번하게 발생할 텐데 버전관리와 `branch`를 통해 이를 효과적으로 대처하고 효율적으로 관리할 수 있기 때문에 개발 속도 향상에  큰 도움이 된다..

### 3. 어떻게 활용할 것인가?

 GIT은 협업에 있어 필수불가결한 요소나 다름없다. 하나의 마스터를 두고 팀원들은 `branch`를 설정하여 동시에 프로젝트를 진행하는 것을 가능하게 할 것이다. 

 각자의 진행사항이나 파일들을 공유할 때 프로젝트 매니저가 우선순위를 결정하여 `merge`하여 통합관리할 것이다.



## JIRA

### 1. 무엇인가?

아틀라시안이 개발한 사유 이슈 추척 제품으로 버그 추적, 이슈 추적, 프로젝트 관리 기능을 제공하는 소프트웨어이다. 지라의 이슈 트래킹 시스템을 통해 프로젝트에서 예상 되거나 또는 이미 발생한 "이슈"들을 관리할 수 있다. ("이슈"는 업무, 문제점, 개성 사항 등을 말한다.)

### 2. 왜 필요한가?

 프로젝트 팀원들의 작업 현황을 확인하고 스케줄이나 우선순위를 조절할 수 있다.

역할과 임무를 분명히 할 수 있으며 협업 시 불필요한 커뮤니케이션 비요을 줄일 수 있다.

이슈 해결에 대한 히스토리가 남기 때문에 후에 비슷한 이슈가 발생했을 때 처리 과정을 되짚어 볼 수 있는 자산이 된다.

### 3. 어떻게 활용할 것인가?

 명세서가 나오고 프로젝트가 시작되면 프로젝트 스케쥴에 대한 관리도구와 개발원간에 작업을 배분하고 커뮤니케이션하는 도구로 사용할 것이다.



## AZURE

### 1. 무엇인가?

 전 세계의 Microsoft 데이터 센터에서 응용 프로그램을 빌드하고 배포하고 관리할 수 있는 유연한 개방형 클라우드 플랫폼이다. 서버나 cpu 등 인프라스트럭처 기능을 갖춘 IaaS, 그리고 애플리케이션 개발 환경인 PaaS 두 가지를 모두 제공한다.

### 2. 왜 필요한가?

 퍼블릭 클라우드 플랫폼으로서 사용하며 컴퓨팅에서부터 데이터 저장, 애플리케션 등 오픈 플랫폼으로서 다양한 서비스를 이용할 수 있다. Window Server 등의 Microsoft 사 제품과 친화성이 높으며, 현재 사용 중인 시스템 환경으로부터 원활한 전환이 가능한 것이 가장 큰 특징이다. Windows 이외의 서비스 및 애플리케션 이용도 가능하다. Linux 등의 오픈 소스와 Oracle 등의 제품에 대응하고 있고 NEP, PHP, Ruby, Node.js, Python, Java 등의 개발 언어를 사용할 수 있다. 

### 3. 어떻게 활용할 것인가?

 c9을 사용했던 것처럼 플랫폼으로서 사용



## JENKINS

### 1. 무엇인가?

 소프트웨어 개발 시 지속적으로 통합 서비스를 제공하는 툴이다.

### 2. 왜 필요한가?

 개발중인 프로젝트에서 커밋은 매우 빈번히 일어나기 때문에 커밋 회수만큼 빌드를 실행하는 것이 아니라 작업이 큐잉되어 자신이 실행될 차례를 기다리게 된다. 코드의 변경과 함께 이루어지는 이 같은 자동화된 빌드와 테스트 작업들은 프로젝트 표준 컴파일 환경에서의 컴파일 오류 검출, 자동화 테스트 수행, 정적 코드 분석에 의한 코딩 규약 준수여부 체크, 결합 테스트 환경에 대한 배포작업 등 여러 이점들을 가져다 준다. 

### 3. 어떻게 활용할 것인가?

 프로젝트 기간 동안 커밋 시 미처 실시하지 못한 테스트나 품질 검사를 할 목적으로 사용할 것이다.

