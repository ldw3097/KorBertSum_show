import json

def posembed():
    # file_path 변경 필요
    file_path = './json_data/korean.train.1.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)

        pos_list = list()
        pos = 0
        for sents in data:
            mydict = {}
            numofsents = len(sents['src'])
            mydict['clss'] = pos
            pos_list.append(mydict)
            pos += numofsents

    return pos_list

def main():
    pos_list = posembed()

if __name__ == "__main__":
    main()