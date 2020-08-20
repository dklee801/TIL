# Git 특강

질문: url : http://hpy.hk/4ai

### git

> git : (분산) 버전 관리 시스템 (DVCS)



 GUI (Graphic User Interface)

- 그래픽 유저 인터페이스

CLI (Command Line Interface)

> - 명령줄 인터페이스
>
> `ls` : 경로 내 파일
>
> `touch name.txt` : 경로 내 파일 생성
>
> `mkdir git` : 경로 생성
>
> `cd` : change directoty
>
> `cd ..`: 상위 directory
>
> `cd .`: 현재 directory



##### `git init` : git 저장소 생성 / 초기화 (최초 1회)

어떠한 작업을 하고 나서

1) `git add.`: commit할 목록에 추가

2) `git commit -m 'Fisrt commit'`

3) `git log` : 버전(이력)

4) `git status` : 상태



# Git 기초



Git 을 윈도우에서 활용하기 위해선 [git bash](https://gitforwindows.org/)를 설치.



## 1. 저장소 초기화

``` bash
$ git init

Initialized empty Git repository in C:/Users/?대룞洹?Desktop/TIL/.git/

(master) $
```

- 로컬 저장소를 만들고 나면, `.git/` 폴더가 생성되고, bash에 `(master)` 라고 표기됨.
- 저장소를 만들기 전에 반드시 원하는 디렉토리인지 확인하는 습관을가지고, 저장소 내부에 저장소를 만들지 말것.
  - 예) Desktop -> git 저장소, TIL -> 다른 git 저장소 (X)



## 2. `add`

작업한 내용을 commit 대상 목록에 추가함.

```bash
git sta
```

