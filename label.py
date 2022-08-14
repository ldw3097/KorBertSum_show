import json

def label():
    # file_path 변경 필요
    file_path = './json_data/korean.train.1.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)
        
        label_dict = list()
        for sents in data:
            mydict = {}
            temp_list = [0 for _ in sents['src']]
            for idx, sent in enumerate(sents['src']):
                for i, tgt in enumerate(sents['tgt']):
                    if (sent == tgt):
                        temp_list[idx] = 1
                        sents['tgt'][i].pop()
                        break
            mydict['label'] = temp_list
            label_dict.append(mydict)

    return label_dict

def main():
    label_data = label()

if __name__ == "__main__":
    main()