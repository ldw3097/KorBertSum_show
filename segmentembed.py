import json

def segembed():
    # file_path 변경 필요
    file_path = './json_data/korean.train.1.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)

        seg_list = list()
        for sents in data:
            mydict = {}
            temp_list = [0 for _ in sents['src']]
            for idx, _ in enumerate(temp_list):
                if (idx % 2 != 0):
                    temp_list[idx] = 1
            mydict['segs'] = temp_list
            seg_list.append(mydict)

    return seg_list

def main():
    segment_label = segembed()
    
if __name__ == "__main__":
    main()