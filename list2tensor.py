import json
import torch
import embedding

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
    train_file = './json_data/korean.train.1.json'

    tmp0 = embedding.tokenembed(train_file)
    tmp1 = embedding.label(train_file)
    tmp2 = embedding.seg_embed(train_file)
    tmp3 = embedding.pos_embed(train_file)
    tmp4 = embedding.src_txt(train_file)
    tmp5 = embedding.tgt_txt(train_file)

    for idx in range(len(tmp0)):
        inputdata = news_to_input(tmp0[idx]['src'], tmp1[idx]['label'], tmp2[idx]['segs'], tmp3[idx]['clss'], tmp4[idx]['src_txt'], tmp5)
        a = torch.tensor(inputdata)
        print(a)

if __name__ == "__main__":
    main()