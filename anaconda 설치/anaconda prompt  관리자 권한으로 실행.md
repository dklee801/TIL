anaconda prompt > 관리자 권한으로 실행

python -n pip install --upgrade pip



가상환경을 생성

conda create -n data_env python =3.7 openssl



정상적으로 가상환경이 만들어 졌는지 확인

conda info --envs



파이썬 버전 확인

python -v



새로운 가상환경으로 전환

activate data_env



파이썬 버전 확인

python -v



개발도구인 IDE를 설치해야함. jupyter notebook 이라는 web기반의 개발툴 이용



현재 data_env 가상환경에서

conda install nb_conda



jupyter notebook이 사용할 기본 디렉토리(working directory)를 설정

이 작업을 하기 위해 환경설정파일을 하나 생성해서 기본 디렉토리를 지정해서 사용.

> jupyter notebook --generate config



config file 을 수정해서 jupyter notebook의 working dir를 설정

> 해당 파일 찾아서  ctrl + f : notebook_dir
>
> 없으면
>
> 
>
> notebook = 'c:/notebook_dir' 적기
>
> 해당 위치에 notebook_dir 폴더 생성



IDE실행

jupyter notebook