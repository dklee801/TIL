# Git , GitHub 기본 사용법



https://moon9342.github.io/git-github

- 여러사람이 공유 데이터(파일)을 동시에 사용할 때 동시성에 문제가 발생, 데이터 유실 문제가 발생할 수 있음.

  - VCS( Version Control System) 프로그램이 많이 사용

    - CVCS( Centreralized Version Control System) : subversion
    - DVCS( Distributed Version Control System) : Git(무료)

    

  - Git : 저장소 두가지 종류가 있음.

    - Local Repsitory ( 내 컴퓨터 안에 저장소가 위치 )
    - Remote Repository ( 다른 컴퓨터 내에 저장소가 위치 ) > GitHub

  

  1. Git 설치 (프로그램 다운로드 후 기본설정으로 설치)

     

  2. 환경 설정

     - git config --global user.name "이름" : 작업자 이름설정

     - git config --global user.email "이메일" : 이메일 설정

       

  3. Local Repository 부터 생성

     - 현재 사용하고 있는 HTML_Basic이라는 프로젝트(폴더)에 대한 Local Repositry 생성

     - commit 과정을 거쳐 우리가 사용하는 모든 파일(환경설정파일 포함)을 Local Repository에 저장

     - 모든 파일을 저장할 필요 없음(환경설정 파일 경우 저장 필요없음) 

     - 불필요한 파일을 commit 하지 않기 위해 특정한 파일하나를 이용 (.gitignore)

     - 이 파일 하나를 만들기

       - 자동으로 만들어주는 website : git ignore

     - 이 파일을 commit 해서 Local Repository에 저장해야함

       

  4.  Remote Repository에 저장

     - Remote Repository를 만들기 위해 GitHub 이용
     - github/ repository 생성
     - webstorm / project > 우클릭 > repository > push

