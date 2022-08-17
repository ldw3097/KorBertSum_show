from tokenembed import *
from label import *
from segmentembed import *
from positionembed import *
from srctgt import *
import torch

def news_to_input(token_id, label, segs, clss, src_txt, tgt_txt):
    b_data_dict = {"src": token_id,
                "labels": label,
                "segs": segs,
                "clss": clss,
                "src_txt": src_txt,
                "tgt_txt": tgt_txt}

    b_list = list()
    b_list.append(b_data_dict)
    return b_list

def main():
    train_f = './json_data/korean.train.1.json'

    # match word/morph with indices
    # UNK 토큰은 인덱스 0으로 처리
    token_dict = list()
    with open(train_f, 'r') as file:
        data = json.load(file, strict=False)
        for i in range(len(data)):
            temp_dic = {}
            for j in range(len(data[i]['src'])):
                temp_src = morph_to_idx(data[i]['src'][j])
                temp_dic['src'] = temp_src
            token_dict.append(temp_dic)

    tmp0 = token_dict
    tmp1 = label()
    tmp2 = segembed()
    tmp3 = posembed()
    tmp4 = src_txt()
    tmp5 = 'hehe'

    for idx in range(len(token_dict)):
        inputdata = news_to_input(tmp0[idx]['src'], tmp1[idx]['label'], tmp2[idx]['segs'], tmp3[idx]['clss'], tmp4[idx]['src_txt'], tmp5)
        a = torch.tensor(inputdata)
        print(a)

if __name__ == "__main__":
    main()