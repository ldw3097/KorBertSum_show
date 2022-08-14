import os
import json

def morph_to_idx(morph):
    bert_dir = './1_bert_download_001_bert_morp_pytorch/001_bert_morp_pytorch'
    file_path = ''
    # check if vocab.korean_morp.list is
    for entry in os.listdir(bert_dir):
        if entry.endswith('list'):
            file_path = bert_dir + '/' + entry

    with open(file_path) as f:
        # OoV 문제는 UNK로 처리하는 대신 0으로 인덱스 넣어줌
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
                    
        return temp_list

def main():
    train_f = './json_data/korean.train.1.json'

    # match word/morph with indices
    # UNK 토큰은 인덱스 0으로 처리
    list_dict = list()
    with open(train_f, 'r') as file:
        data = json.load(file, strict=False)
        for i in range(len(data)):
            mydict = {}
            for j in range(len(data[i]['src'])):
                temp_src = list()
                temp_src.append(morph_to_idx(data[i]['src'][j]))
                mydict['src'] = temp_src
            list_dict.append(mydict)

if __name__ == '__main__':
    main()