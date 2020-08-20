# Git 원격 저장소 활용

Git 원격 저장소 기능을 제공해주는 서비스는 `gitlab`, `bitbucket`, `github` 등이 있다.



## 0. 원격 저장소 설정

```bash
$ git remote add origin {url}
```

- git 원격 저장소를 추가하고 `origin`이라는 이름으로 `url`로 설정

- 설정된 저장소를 확인하기 위해서는 아래의 명령어를 입력한다.

  ```bash
  $ git remote -v
  origin  https://github.com/dklee801/TIL.git (fetch)
  origin  https://github.com/dklee801/TIL.git (push)
  ```

  

## 원격 저장소에 push

```bash
$ git push origin master
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
Delta compression using up to 8 threads
Compressing objects: 100% (12/12), done.
Writing objects: 100% (12/12), 39.21 KiB | 13.07 MiB/s, done.
Total 12 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/dklee801/TIL.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

