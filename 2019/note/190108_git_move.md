# git 자리이동





#### 1. git clone

기본 파일 위치 cd desktop/sm

> git clone https://github.com/jho0078/til.git

주소 복사 후 붙여넣기(insert)

*git clone할 경우 - remote, init 과정이 필요없음 (자리이동)

til폴더로 



#### 2. 이전 사용자의 git 정보 지우기

​	1. terminal에서 지우기

> git credential reject

> protocol=https

> host=github.com

​	2. 제어판 - 사용자 계정 - 자격 증명 관리자



#### 3. git push → 로그인



#### 4. git 사용자 정보 저장

git commit 할 때 들어가는 정보 (github과는 별개)

git config --global user.name 'jho0078'

git config --global user.email jho0078.jho0078@gmail.com

git config --global  --list



#### 5. repositary 만들기

1. readme.txt git push
2.  git clone https://github.com/kshm2483/pushpull.git
3.  cd pushpull/ pushpull 폴더가  다운받아지는 동시에 master생김
4.  readme.txt 파일 수정 
5.  git add .
6.  git commit -m "커밋이름"