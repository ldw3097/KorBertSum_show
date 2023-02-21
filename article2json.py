from etri_api_scraper import do_lang
import json

def main():
    file_path = r'./raw_data/train_sample_copy.json'
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

            sent_morphs = list()
            for j in range(2, len(article)):
                print(article[j])
                for idx in range(len(article[j])):
                    # do_lang(open-api key, sentence)
                    tokenize_str = do_lang('your-access-key', article[j][idx]["sentence"])
                    # create src's 'word/morph' structures
                    token = tokenize_str.split()
                    sent_morphs.append(token)
            src_list.append(sent_morphs)

        print("src_list completed")

        extra_indices_set = list()
        for i in range(num_of_arts):
            extractive = data["documents"][i]["extractive"]
            extra_indices_set.append(extractive)
            
        print("extraction completed")

        # create tgt_list
        tgt_list = list()
        for i in range(num_of_arts):
            article = data["documents"][i]["text"]
            # add extractive's morphs
            empty_list = list()
            for idx in extra_indices_set[0]:
                empty_list.append(src_list[i][idx-2])
            tgt_list.append(empty_list)
            # update extra_indices_set
            del extra_indices_set[0]

            if len(extra_indices_set) == 0:
                break

        print("tgt completed")

        list_dic = list()
        for i in range(num_of_arts):
            mydict = {}
            mydict['src'] = src_list[i]
            mydict['tgt'] = tgt_list[i]
            list_dic.append(mydict)
        
        file_path = "./json_data/korean.train.1.json"

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(list_dic, f, ensure_ascii=False)

if __name__ == '__main__':
    main()