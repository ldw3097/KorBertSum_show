import json

# file_path 변경 필요
file_path = './json_data/korean.train.1.json'
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file, strict=False)

    list_dic = list()

    for idx, sents in enumerate(data):
        mydict = {}
        temp_src = list()
        temp_tgt = list()
        for sent in sents['src']:
            sent.insert(0, '[CLS]')
            sent.append('[SEP]')
            temp_src.append(sent)
        
        for sent in sents['tgt']:
            sent.insert(0, '[CLS]')
            sent.append('[SEP]')
            temp_tgt.append(sent)

        mydict['src'] = temp_src
        mydict['tgt'] = temp_tgt
        list_dic.append(mydict)

    # create json file
    file_path = "./json_data/korean.train.1.json"

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(list_dic, f, ensure_ascii=False)
    