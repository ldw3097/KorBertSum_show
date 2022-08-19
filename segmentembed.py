import json

def segembed(file_path):
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

def main():
    # check file_path
    file_path = './json_data/korean.train.1.json'
    segment_label = segembed(file_path)

if __name__ == "__main__":
    main()