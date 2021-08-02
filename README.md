# 🎓Survival-Ensemble🎓
- Tensorflow Attention 기계번역 Ensemble 연구 이어서 - Survival Ensemble



#### 📝 연구 주제 : 기계 번역 모델의 앙상블 적용할 때 성능이 좋지 않는 것을 하나씩 떨어뜨리는 서바이벌 방식으로 했을 때 성능 향상이 있을까?

---



🔎 Ensemble Survival 코드 1

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



🔎 Ensemble Survival 코드 2- 맞춘 애들끼리만 살아남자

서바이벌 방식 : 다수결로 나온 단어가 있을 때 다른 단어를 출력한 모델들을 탈락시키는 방식으로 코드를 짜고 있다. 계속 진행하다가 2개의 모델이 남았을 때 더 높은 softmax 확률을 가진 모델 1개로 진행하는 것으로 한다.

그렇다면 '정답(다수결로 나온 단어)'을 맞추지 못한 모델에 정답을 주입하는 일이 없어진다. (그 전의 앙상블은 틀린 모델에 정답을 주입하는 느낌이었음)

모델 개수 : 총 15개로 진행한다.

- 코드 : nmt_Survival_Only_Win.ipynb 
- [Training_Checkpoint](/Users/ahjeong_park/Study/Survival-Ensemble/Checkpoint) 
- [Test Data](/Users/ahjeong_park/Study/Attention-Ensemble-Translation/BLEU/test_data.txt) : 학습하지 않은 1000개의 spa-eng 데이터
- Survival_Translate.xlsx : 번역 결과 & QE 측정



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



