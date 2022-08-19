import json

def posembed(file_path):
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

def main():
    file_path = './json_data/korean.train.1.json'
    pos_list = posembed(file_path)

if __name__ == "__main__":
    main()