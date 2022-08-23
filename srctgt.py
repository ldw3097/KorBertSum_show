import json

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

def main():
    # check file_path
    file_path = './json_data/korean.train.1.json'
    src_list = src_txt(file_path)
    tgt_list = tgt_txt(file_path)

if __name__ == "__main__":
    main()