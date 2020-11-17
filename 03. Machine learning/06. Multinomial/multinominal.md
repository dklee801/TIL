# Multinominal



## 성능 평가지표 (Metric)

- 성능 평가를 하는 방법 : 정답 vs 모델의 예측값에 대한 정답 비율



- Confusion matrix : 로지스틱 결과와 실제 정답과의 관계를 표현
  - 분류결과 True : Positive / False : Negative
  - 실제 정답을 맞췄을때,  True: True / False : False
  -  True positive, True negative, False positvie...



- 실제 사용하는 성능평가 matric

  - precision (정밀도) : 우리의 모델이 True로 분류한 것 중 실제 True 인것에 대한 비율

    > (실제 True,모델 True ) /
    >
    > ((실제 True, 모델 True) + (실제 False, 모델이 True))

  - recall (재현율) : 실제 True인 것중에 우리의 Model이 True로 예측한 비율(Sensitivity)

    > (실제 True, 모델 True) / 
    >
    > ((실제 True, 모델 True) + (모델 False, 실제 True))

  

  - 예시

    - 사진을 입력받으면 개 or 고양이인지 검출

    1. A: 검출율 99.9% : 거의 모든 고양이를 찾아냄, but 오검율(실제 고양이가 아닌경우도 검출되는 경우) 도 높음

    2. B: 검출율 60% :하지마면 오검율이 거의 없음(실제 고양이가 아닌경우는 검출하지않음.)

       = 상황에 따라 유용한 정도가 다름.

    - 검출율 : 검출을 얼마나 잘해냈는지 : Recall (재현율)
    - 정확도:  검출한게 얼마나 정확한지 : Precision (정밀도)

    

  - accuracy (정확도) : 

    > ((모델 True, 실제 True) +(모델 False, 실제 False))  /
    >
    > (TP + FN + FP +TN)





## 성능평가 주요 개념.



- #### Learning rate : 

  > w(weight), b(bias) 
  >
  > w = w - a * (E(w,b) / Aw)
  >
  > a : learning rate = 미분값에 곱해주는 alpha, 상수
  >
  > - 미분한 값이 우리가 가진 w값보다 클수 가 있음, 이렇게 되면 w값이 불안정하기 때문에 최적의 값 찾기 어려워짐. 이를 조절해주는 learning rate, alpha

  - 적절한 learning rate <우리의 alpha값

    - w가 점점 최적화되지않고, 크게 작게 반복

      > ##### "overshooting"

  - 적절한 learning rate > 우리의 alpha

    - 설정한 반복 회수안에 최적의 w를 찾지 못하고 도중에 중단

      > ##### "local minima"

  - 일반적으로 0.01 or 0.001으로 learning rate로 설정 후, 출력되는 loss값을 확인. 

    실제로 예측한 값과 정답과의 차에 대한 cross entrophy값 즉, loss값을 보고 설정 



- #### nomalization (정규화)

  1. ###### Min - Max nomalization

     > 최대 - 최소 , x에서 최소값 빼고 그 비율에 대해 b를 구해서 0과 1사이로 모든 원소들을 scailing

     - 장점 : 0~1 사이로 모든 feature를 sacailing
     - 단점 : 이상치에 상당히 취약

  2. ###### Standardization(표준화) = z-score nomalization

     > 표준 편차 이용

     - 장점 : 이상치에 둔감
     - 단점 : 모든 feature에 대해 동일 척도로 scailing을 못함.

  3. ###### Student's T 분포



- #### Underfitting / Overfitting

  

  - **Underfitting** : 너무 대충 학습이 된 경우.

    

  - **Overfitting** : Training data에 대해 과하게 학습이 되어 실제 데이터에 적용이 잘 안되는 경우

    - 해결하려면

      1. 많은 양의 Training data : 프로그램적으로 해결이 불가

      2. feature(독립변수: 컬럼) 의 개수를 줄여야함. (상관관계분석 등을 통해)

      3.  weight의 값을 인위적으로 조절 (w의 값이 클수록 curve가 심해짐 = overfitting의 가능성이 커짐)

         - w값을 줄이는 법 regulazation

      4. Deep learning의 "Drop out"
  
      5. 학습의 수를 줄이기 (epoch 줄이기)
  
         - 전체 학습데이터를 이용해서 n번학습 : "n epoch"



- #### Evaluation(평가)

  - 가지고 있는 Training data set을 이용해서 어떻게 성능 평가를 할 것인가?

    

  - 하지말아야할 것! 

    ###### : training data set으로 학습한 후 training data set으로 평가 진행

    ###### : 성능이 아주 좋게 나올 수 밖에 없음.

    

  - Training data와 Testing data로 나눠야함.

    - ###### Testing data set

      Testing data는 최종으로 한번 accuracy 측정을 위한 데이터,

      이 데이터 셋으로 모델을 수정하면 안됨.

    - ###### Training data set

      학습 용

    - ###### Validation data set

      model 의 개선 작업을 위해

      

  -  데이터량이 작으면 underfitting, 해결하기 위해 epoch의 수를 늘리면 overfitting

    > 해결하기 위해 Cross validation(CV)

    - **K-fold 방식**

      (K는 상수값, data set을 k분의 1만큼 쪼개서 K번 fold 나눠서 진행.)

      > e.g) 3-fold
      >
      > fold1 = test / train / train
      >
      > fold2 = train/ test / train
      >
      > fold3 = train / train/ test
      >
      > fold1,2,3의 accuracy의 평균

      

  ## Multinominal classification(다중분류)

  - 이항 분류의 집합

    > 다중 분류는 이항분류를 하여 각각 logistic 중 확률이 가장 큰 것을 기반으로 분류

    

  - 다중 분류에서는 각각의 확률값을 sigmoid 대신 softmax를 이용하면 각 레이블의 전체 확률의 합을 1로 만듦