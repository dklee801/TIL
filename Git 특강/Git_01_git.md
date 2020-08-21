# Git 특강

질문: url : http://hpy.hk/4ai



blog : https://jekyllrb.com/docs/

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

`git add .` : 변경사항 모두 추가

`git add name.txt` : 특정파일만 추가

`git add foler/` : 특정 폴더 추가

```bash
# 작업 후 상태

$ git status
On branch master

No commits yet

Untracked files:
# Git 으로 관리 된 적 없는 파일

  (use "git add <file>..." to include in what will be committed)
  # commit 될 것들에 포함시키기 위해서는 add 명령어를 써라
        git.md
        markdown.md
        markdown_images/

nothing added to commit but untracked files present (use "git add" to track)
# 총평
# commit 될 것이 없다
# 하지만 새로 생성한 파일은 존재한다.
```

add 명령이 된 후 상태

```bash
$ git status
On branch master

No commits yet

Changes to be committed:
# commit이 될 변경 사항들.
# working directory에는 파일이 없고
# staging aread에는 있음.
  (use "git rm --cached <file>..." to unstage)
        new file:   git.md
        new file:   markdown.md
        new file:   markdown_images/image-20200820140538364.png
```



## 3. `commit`

```bash
$ git commit -m 'add markdown.md'
[master (root-commit) 3e9f006] add markdown.md
 3 files changed, 151 insertions(+)
 create mode 100644 git.md
 create mode 100644 markdown.md
 create mode 100644 markdown_images/image-20200820140538364.png
```

- `commit`은 버젼(이력)을 기록하는 명령어이다.

- commit 메세지는 해당하는 이력을 나타낼 수 있도록 작성 하여야 한다.

- commit 이력을 확인하기 위해서는 아래의 명령어를 사용

  ```bash
  $ git log
  commit 3e9f00679e561bb76745ec785bd6ae0b68a04ef3 (HEAD -> master)
  Author: dklee801 <dklee801@gmail.com>
  Date:   Thu Aug 20 14:58:05 2020 +0900
  
      add markdown.md
  $ git log -1
  $ git log --oneline
  3e9f006 (HEAD -> master) add markdown.md
  $ git log --oneline --1
  ```

  ```bash
  $ git status
  On branch master
  nothing to commit, working tree clean
  ```

  

- 새로운 코드를 학습할때마다 commit 하면 이후에 코드가 변했을 때도 추적해서 확인할 수 있음.
- PEP8 : 파이썬 스타일 가이드



