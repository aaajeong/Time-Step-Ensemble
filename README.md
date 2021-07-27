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

