import json
import os

def label(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)
        
        label_list = list()
        for article in data:
            temp_list = [0 for _ in article['src']]
            for idx, sent in enumerate(article['src']):
                for i, tgt in enumerate(article['tgt']):
                    if (sent == tgt):
                        temp_list[idx] = 1
                        article['tgt'][i].pop()
                        break
            label_list.append(temp_list)

    return label_list

def seg_embed(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)

        total_segs = list()
        for article in data:
            seg_list = []
            for idx, sent in enumerate(article['src']):
                if idx % 2 == 0:
                    temp = [0 for _ in sent]
                    seg_list.extend(temp)
                else:
                    temp = [1 for _ in sent]
                    seg_list.extend(temp)
            total_segs.append(seg_list)

    return total_segs

def pos_embed(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)

        pos_list = list()
        for article in data:
            pos = 0
            temp_list = []
            for idx, sent in enumerate(article['src']):
                temp_list.append(pos)
                numofmorphs = len(sent)
                pos += numofmorphs
            pos_list.append(temp_list)

    return pos_list

def src_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)

        src_list = list()
        for sng_art in data:
            sent_list = []
            for _, morphs in enumerate(sng_art['src']):
                morphs.pop(0)
                morphs.pop(len(morphs)-1)
                sent = ' '.join(morphs)
                sent_list.append(sent)
            src_list.append(sent_list)

    return src_list

def tgt_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)

        tgt_list = list()
        for sng_art in data:
            sent_list = []
            for _, morphs in enumerate(sng_art['tgt']):
                morphs.pop(0)
                morphs.pop(len(morphs)-1)
                sent = ' '.join(morphs)
                sent_list.append(sent)
            
            tgt_sent = '<p>'.join(sent_list)
            tgt_list.append(tgt_sent)
            
        return tgt_list
    
def morph_to_idx(morph):
    bert_dir = './1_bert_download_001_bert_morp_pytorch/001_bert_morp_pytorch'
    file_path = ''
    # check if vocab list is
    for entry in os.listdir(bert_dir):
        if entry.endswith('list'):
            file_path = bert_dir + '/' + entry

    with open(file_path, 'r', encoding='utf-8') as f:
        # OoV 문제는 UNK로 처리하는 대신 0으로 변환
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

def tokenembed(file_path):
    # UNK 토큰은 인덱스 0으로 처리
    token_dict = list()
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)
        for i in range(len(data)):
            mydict = {}
            for j in range(len(data[i]['src'])):
                temp_src = morph_to_idx(data[i]['src'][j])
                mydict['src'] = temp_src
            token_dict.append(mydict)
    return token_dict

def main():
    train_file = './json_data/korean.train.1.json'
    tmp0 = tokenembed(train_file)
    tmp1 = label(train_file)
    tmp2 = seg_embed(train_file)
    tmp3 = pos_embed(train_file)
    tmp4 = src_txt(train_file)
    tmp5 = tgt_txt(train_file)

if __name__ == "__main__":
    main()