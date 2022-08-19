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

def main():
    # check file_path
    file_path = './json_data/korean.train.1.json'
    label_data = label(file_path)

if __name__ == "__main__":
    main()