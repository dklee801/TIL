#### FC layer(Dense layer)

- Fully Connected layer
- 완전 연결 네트웍
- 데이터가 1차원으로 들어가야함.



이미지 데이터는 기본 3차원(흑백 2차원)

> FC layer에 들어가면서 1차원으로 되면서 공간정보에 대한 데이터가 없어짐. 

 

#### 성능평가 지표 (Precion, Recall, Accuracy, f1-score)



학습종료 > 성능평가 metric > precsion & recall : f1-score

accuracy : 직관적인 지표, domain에 대한 Bias(편향)이 심한 단점

예 : 희귀병, 대부분은 정상, 극소수가 비정상, : accuracy 높을 수밖에.



###### classfication metircs

`sklearn.metrics.classfication_report( x, y ,z)`

- x: "T값"(정답), 1차원 array
  - multinomial인 경우 T: one_hot encoding ( 다차원 )
  - 그러므로 onehot encoding 사용 불가
- y: "Pred"(예측값) : 1차원 array
- z: 출력 시 각 label을 표현하기 위한 문자열

###### return

dict 2개 , key값은 label1 & label2...

API reference보고 확인



###### confusion metrix

sklearn.metrics.confusion(x, y, z)

결과

array([[1, 1, 0], 

​			[1, 0, 0], 

​			[1, 0, 2]])



#### epoch수는 어떻게 결정?



- `1 epoch`: 전체 training data로 1번 학습
  - epoch 수가 너무 작으면 : underfitting
  - epoch 수가 너무 크면 : overfitting



- epoch 할수록

  - training data 에 대해 accuracy 높아짐
  - validation data에 대해 accuracy가 증가하다가 어느 순간부터 과적합 발생하여 떨어짐.

  

- epoch을 크게 잡고, 1epoch 마다 training data accuracy/ validation data accuracy 를 배열로 저장해서 확인.

