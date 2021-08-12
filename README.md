# 🎓Survival-Ensemble🎓
- Tensorflow Attention 기계번역 Ensemble 연구 이어서 - Survival Ensemble



#### 📝 연구 주제 : 기계 번역 모델의 앙상블 적용할 때 성능이 좋지 않는 것을 하나씩 떨어뜨리는 서바이벌 방식으로 했을 때 성능 향상이 있을까?

---



#### 🔎 Ensemble Survival 코드 1

- 코드 : [nmt_Ensemble_Survival.ipynb](https://github.com/aaajeong/Survival-Ensemble/blob/main/nmt_Ensemble_Survival.ipynb)
  - 5개의 모델 중에서 제일 좋지 않은 모델은 제외하고
  - 나머지 모델에서 소프트 보팅 & 가장 높은 확률을 가진 모델 로 결출력
- [Test Data](/Users/ahjeong_park/Study/Attention-Ensemble-Translation/BLEU/test_data.txt) : 학습하지 않은 1000개의 spa-eng 데이터
- [Training Data](/Users/ahjeong_park/Study/Attention-Ensemble-Translation/BLEU/spa-eng(for BLEU).txt)
- [Training Checkpoint](/Users/ahjeong_park/Study/Attention-Ensemble-Translation/5 Models Checkpoints_60000) : 트레이닝 데이터 1~60000 line
- [QE 계산 코드](/Users/ahjeong_park/Study/Attention-Ensemble-Translation/BLEU/Calculate_QE.ipynb)
- [Survival_Ensemble.xlsx](https://github.com/aaajeong/Survival-Ensemble/blob/main/Survival_Translate.xlsx) : 위 설명한 2개 버전 서바이벌 모델 결과 & QE 비교 정리

💥 서바이벌 방식 수정 필요 💥

- 여러 개의 모델 중에 **맞춘 애들만!!!** 살아남는 것
- 틀린 모델은 제외되는 것
- **그래서 모델은 많을 수록 좋다.**
- 번역을 시작할때는 모든 모델 참여



#### 🔎 Ensemble Survival 코드 2- 맞춘 애들끼리만 살아남자

서바이벌 방식 : 다수결로 나온 단어가 있을 때 다른 단어를 출력한 모델들을 탈락시키는 방식으로 코드를 짜고 있다. 계속 진행하다가 2개의 모델이 남았을 때 더 높은 softmax 확률을 가진 모델 1개로 진행하는 것으로 한다.

그렇다면 '정답(다수결로 나온 단어)'을 맞추지 못한 모델에 정답을 주입하는 일이 없어진다. (그 전의 앙상블은 틀린 모델에 정답을 주입하는 느낌이었음)

모델 개수 : 총 15개로 진행한다.

- 코드 : nmt_Survival_Only_Win.ipynb 
- [Training_Checkpoint](/Users/ahjeong_park/Study/Survival-Ensemble/Checkpoint) 
- [Test Data](/Users/ahjeong_park/Study/Attention-Ensemble-Translation/BLEU/test_data.txt) : 학습하지 않은 1000개의 spa-eng 데이터
- Survival_Translate.xlsx : 번역 결과 & QE 측정

[ 서바이벌 모델 번역 과정]

1. 모델이 출력한 단어 중에 다수결로 뽑힌 단어를 '세미 정답' 이라고 하겠다.

   - 모델 결과 리스트에서 가장 많이 등장한 단어 찾기

     ~~딕셔너리로 횟수 count 후 가장 많은 횟수의 단어 출력?~~

     파이썬 max(data, key) 함수 이용 : 리스트 최빈 값 출력

     → 문제 : 최빈값이 여러개일 경우 제일 앞에 있는 요소 출력한다.

   - 세미 정답 저장

   - 세미 정답을 출력한 모델들을 저장(인덱스로 저장) -> 살아남은 모델들을 '위너' 라고 하겠다.

   - 위너 모델들로 다시 서바이벌 참여 모델을 업데이트 한다.

2. 위너 모델에 세미 정답을 input 으로 전달 (어차피 위너가 세미 정답을 출력한 것 이기 때문에 그대로 input 전달한 것이라고 생각하면 됨)

3. 위 1, 2 를 반복

4. 만약 2개의 모델이 남았을 경우

   - 2개의 모델의 예측이 같을 때 : 둘 중 하나의 예측을 세미 정답으로 결정.

   - 2개의 모델의 예측이 다를 때 : 각 모델의 softmax 중 큰 값의 예측을 세미 정답으로 결정

     그리고 최종 winner 모델을 결정한다.

5. 최후의 모델 1개가 남았을 때 time-step 이 남아있다면, 1개의 모델로 번역을 이어 진행한다.



[QE 측정 결과]

서바이벌 모델 VS 앙상블에 사용된 단일 모델

|                                                   | Survival - 맞춘 모델만 살아남기 | Ensemble (Soft Voting) | Ensemble-Model1 | Ensemble-Model2 | Ensemble-Model3 |
| ------------------------------------------------- | ------------------------------- | ---------------------- | --------------- | --------------- | --------------- |
| **Translation  Quality Estimator (QE)      평균** | **0.753046**                    | 0.748706               | 0.680984        | 0.710045        | 0.698374        |

**👉 단일 모델과 비교했을 때 서바이벌 모델의 성능이 좋아보인다.** RNN의 time-step 에서 앙상블을 이용해서 번역을 한 결과 단일 모델 보다 성능이 더 좋아보인다. 그렇다면 이 서바이벌 방식이 정말로 좋은가 확인해보기 위해서 **앙상블을 하지 않은 "진짜 다수결" 번역 모델**과 비교 해보자.



#### 🔎 단일 모델 결과의 다수결을 통한 번역 - 진짜 다수결 번역 

​	진짜 다수결 번역이란, 각각의 모델에 대해서 나온 결과물로 다수결 처리하여 번역하는 것을 말하겠다. 즉 RNN 중간 time-step 에서 앙상블을 이용하지 않고 원래대로 각 모델마다 번역 결과를 내놓으면, 그 결과를 기반으로 다수결을 통해 최종 번역을 완성한다.

방법 :모델이 출력한 각각의 단어의 confidence(softmax) 평균 값으로, 그 평균은 문장에 대한 weight가 된다.

(예시)

5모델 중에서,

1번 모델:  I love you → 각 단어의 softmax 의 평균 값 ➡️ a

2번 모델 :  I love you → 각 단어의 softmax 평균 값 ➡️ b



3번 모델 : I like you → 각 단어의 softmax 평균 값 ➡️ c

4번 모델 :   I like you → 각 단어의 softmax 평균 값 ➡️ d

5번 모델:  I like you → 각 단어의 softmax 평균 값 ➡️ e

먼저 1,2,3,4,5 모델의 결과가 같은지/아닌지를 그룹핑한다.

(a, b, d) 와 (c, e) 가 그룹핑 되었다고 하면, 각 그룹의 소프트맥스 평균의 합을 구한다. 

즉, **(a, b, d) 는 a+b+d** 이고, **(c, e) 는 c+e** 이다.

이 중 *평균의 합이 가장 큰 그룹의 답* 을 채택하는 것이다.

**이는 단순하게 모델 수에 기반한 다수결이 아니라 소프트맥스의 합을 고려한 다수결 결과이다.**

**따라서 소프트맥스의 합이 높게 나온 숫자가 적은 쪽의 그룹이 숫자가 많은쪽을 이길 수도 있다.**



모델 개수 : 총 15개로 진행한다.

- 코드 : nmt_Real_majority.ipynb 
- [Training_Checkpoint](/Users/ahjeong_park/Study/Survival-Ensemble/Checkpoint) 
- [Test Data](/Users/ahjeong_park/Study/Attention-Ensemble-Translation/BLEU/test_data.txt) : 학습하지 않은 1000개의 spa-eng 데이터
- Survival_Translate.xlsx : 번역 결과 & QE 측정
