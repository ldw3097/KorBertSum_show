import json

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

def main():
    file_path = './json_data/korean.train.1.json'
    label_data = label(file_path)
    segment_label = seg_embed(file_path)
    pos_list = pos_embed(file_path)
    src_list = src_txt(file_path)
    tgt_list = tgt_txt(file_path)

if __name__ == "__main__":
    main()