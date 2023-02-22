from etri_api_scraper import do_lang
import json
from kiwipiepy import Kiwi

def get_src(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)
    
        src_list = list()
        num_of_arts = len(data["documents"])
        # create src_list
        for i in range(num_of_arts):
            article = data["documents"][i]["text"]

            for sentence in article:
                if len(sentence) == 0:
                    del article[article.index(sentence)]

            # # analyze morphs via ETRI tokenizer
            # sent_morphs = list()
            # for j in range(2, len(article)):
            #     print(article[j])
            #     for idx in range(len(article[j])):
            #         # do_lang(open-api key, sentence)
            #         tokenize_str = do_lang('your access key', article[j][idx]["sentence"])
            #         # create src's 'word/morph' structures
            #         token = tokenize_str.split()
            #         sent_morphs.append(token)
            # src_list.append(sent_morphs)

            # analyze morphs via Kiwi tokenizer
            temp_list2 = list()

            for j in range(2, len(article)):
                print(article[j])
                for idx in range(len(article[j])):
                    kiwi = Kiwi()
                    temp_list1 = list()
                    tokenize_list = kiwi.tokenize(article[j][idx]["sentence"])[:-1]

                    for z in range(len(tokenize_list)):
                        token = tokenize_list[z].form + '/' + tokenize_list[z].tag
                        temp_list1.append(token)
                    temp_list2.append(temp_list1)
                src_list.append(temp_list2)

        with open('src.json', 'w', encoding='utf-8') as file:
            json.dump(src_list, file, ensure_ascii=False)

        return src_list
    
def get_extra_indices(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)
        num_of_arts = len(data["documents"])

        extra_indices_set = list()
        for i in range(num_of_arts):
            extractive = data["documents"][i]["extractive"]
            extra_indices_set.append(extractive)
        
        print(extra_indices_set)
        print("extraction completed")

        return extra_indices_set
    
def get_tgt(file_path, src_list: list, extra_indices_set: list):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)
    
        num_of_arts = len(data["documents"])
        # create tgt_list
        tgt_list = list()
        for i in range(num_of_arts):
            article = data["documents"][i]["text"]
            # add extractive's morphs
            empty_list = list()
            for idx in extra_indices_set[0]:
                print(idx)
                empty_list.append(src_list[i][idx-2])
            tgt_list.append(empty_list)
            # update extra_indices_set
            del extra_indices_set[0]

            if len(extra_indices_set) == 0:
                break
        print("tgt completed")

        return tgt_list

def make_json(file_path, src_list, tgt_list):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file, strict=False)
        num_of_arts = len(data["documents"])

        list_dic = list()
        for i in range(num_of_arts):
            mydict = {}
            mydict['src'] = src_list[i]
            mydict['tgt'] = tgt_list[i]
            list_dic.append(mydict)
        
        file_path = "./json_data/korean.train.2.json"

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(list_dic, f, ensure_ascii=False)

def main():
    file_path = r'./raw_data/train_sample_copy.json'
    src_txt = get_src(file_path)
    extra_indices_set = get_extra_indices(file_path)
    tgt_txt = get_tgt(file_path, src_txt, extra_indices_set)
    make_json(file_path, src_txt, tgt_txt)

if __name__ == '__main__':
    main()