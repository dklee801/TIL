# CNN 정리



Input data(x,t) > feed forward 방식으로 전달



- 첫 layer : input layer : 들어온 데이터를 그냥 by_pass 시킴(통과)

  

- convolution layer : 합성곱 연산 레이어 , convolution 처리

  - convolution : filter/ stride / channel / padding(작아진 이미 처리)

    - 이렇게 convolution해서 나온 결과 : feature map

        	- feature map의 채널은 필터의 개수와 같음.

        - 이 feature map을 ReLU 함수에 통과시켜서 값이 나옴

        - 나온 결과 : Activation map : 이 값을 방금의 convolution layer 혹은 다음의 pooling layer 혹은 fc layer 로 보낼 수 있다.
      - 하지만 일반적으로 pooling layer에 보냄

  

- pooling layer : pooling 처리
- Max pooling / Min pooling / Avg pooling
  - 일반적으로 CNN은 Max pooling 이용
    - CNN 에선 가장 큰값이 일반적으로 특징을 잘 표현하기 때문
  - Kernel size :  pooling의 영역을 어떻게 잡을지
    - Kernel의 크기와 stride의 길이를 잡음
      - 이렇게 해서 특징을 부각, 이미지 크기는 축소
      - 만약에 이미지 사이즈를 줄일 필요가 없다면 pooling 없어도 됨.



- 이제 나온 데이터를 Flatten해야함
  - : 4차원의 데이터를 2차원으로 펼침
  - 일반적으로 dense레이어에는 1차원의 데이터가 여러개인 2차원으로 들어가야되기 때문



- 이제 DNN으로 들어감
  - 위의 Flatten의 데이터는 DNN의 입력데이터
  - Flatten처리 후 데이터의 크기를 줄이기 위해 Drop out작업함 (40~50% 정도 줄임 : 데이터 과적합을 피하기 위해.)
  - 이후 데이터를 hidden layer로
  - 이후 output layer에서 결과 출력



이 구조를 keras 로 구현



3,