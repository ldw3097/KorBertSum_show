import os
import json

from pyparsing import line_end

def morph_to_idx(morph):
    bert_dir = './1_bert_download_001_bert_morp_pytorch/001_bert_morp_pytorch'
    file_path = ''
    # check if vocab.korean_morp.list is
    for entry in os.listdir(bert_dir):
        if entry.endswith('list'):
            file_path = bert_dir + '/' + entry

    with open(file_path) as f:
        temp_list = [0 for i in morph]
        lines = f.readlines()
        for idx, item in enumerate(morph):
            # [CLS]
            if idx == 0:
                temp_list[0] = 1
                continue
            # [SEP]
            elif idx == len(morph)-1:
                temp_list[len(morph)-1] = 2
                continue
            
            # others
            for line in lines:
                if line.find(item) != -1:
                    temp_list[idx] = int(line.split('\t')[1].strip('\n'))
                    break
        print(temp_list)

def main():
    train_f = './json_data/korean.train.1.json'

    # match word/morph with indices
    # 0인 토큰 왜 뜨는지 잘 모르겠음
    with open(train_f, 'r') as file:
        data = json.load(file, strict=False)
        for i in range(len(data)):
            for j in range(len(data[i]['src'])):
                morph_to_idx(data[i]['src'][j])

if __name__ == '__main__':
    main()