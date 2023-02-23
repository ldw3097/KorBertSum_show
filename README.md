# 문서 요약 텍스트를 활용한 KorBertSum input data 생성하기

문서 요약 텍스트(https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=97) 를 활용해서 KorBertSum input data를 생성하는 레포지토리입니다.

이 문서의 원저작권은 BertSum(https://github.com/nlpyang/BertSum) 에 있습니다.

KorBertSum 블로그(https://velog.io/@raqoon886/KorBertSum-SummaryBot) 를 전반적으로 참고했습니다.

[BertSum](https://arxiv.org/pdf/1903.10318.pdf, "BertSum") 에서 embedding 방식에 관해 도움을 받을 수 있습니다.

## 전제 조건

    pip3 install logger
    pip3 install kiwipiepy

ETRI 홈페이지(https://aiopen.etri.re.kr/bertModel) 에서 access key를 발급받은 뒤 BERT model을 다운로드 받아야 합니다.
(사용협약서상 모델을 공개하지 않는 점 양해 부탁드립니다.)

학습은 Colab Pro 환경에서 진행했습니다.

## 사용 방법

### 문서 요약 텍스트에서 기사 전체 문단과 extractive sentence를 json 파일로 생성한다.

    python article2json.py

### 임베딩을 진행한다.

    python embedding.py

### list를 tensor 파일로 변환한다.

    python list2tensor.py

## 주의사항

get_src 함수에 Kiwi tokenizer와 ETRI tokenizer로 형태소 분석하는 기능을 구현했습니다.

현재 원인 모를 이유로 ETRI 형태소 분석이 되지 않아 Kiwi tokenizer로 재배포했습니다.

Kiwi와 ETRI 형태소 분석기의 태그셋이 서로 다른 부분이 있는데, 이 점이 성능에 영향을 미칠 수도 있는 점 유의 바랍니다.

list2tensor.py에서 마무리로 .pt 확장자로 변환해주는 로직을 추가해줘야 합니다.

# 출처
BertSum 논문: https://arxiv.org/pdf/1903.10318.pdf  
참고한 블로그: https://velog.io/@raqoon886/KorBertSum-SummaryBot    
ETRI 형태소분석기: https://aiopen.etri.re.kr/guide/WiseNLU
Kiwi 형태소분석기: https://github.com/bab2min/kiwipiepy 
