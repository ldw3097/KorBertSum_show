import json

def src_txt():
    news_path = r'./raw_data/train_sample_copy.json'
    with open(news_path, 'r') as file:
        data = json.load(file, strict=False)
    
        numofarts = len(data["documents"])
        src_list = list()
        # create src_list
        for i in range(numofarts):
            mydict = {}
            article = data["documents"][i]["text"]

            # empty list delete
            for sentence in article:
                if len(sentence) == 0:
                    del article[article.index(sentence)]
            art_length = len(article)

            sents = list()
            for j in range(2, art_length):
                # for each sentence
                for idx in range(len(article[j])):
                    sent = article[j][idx]["sentence"]
                    sents.append(sent)

            mydict['src_txt'] = sents
            src_list.append(mydict)

    return src_list

def tgt_txt(src_list):
    news_path = r'./raw_data/train_sample_copy.json'
    with open(news_path, 'r') as file:
        data = json.load(file, strict=False)

        numofarts = len(data["documents"])

        extra_indices_set = list()
        # extract the indices of extractive sentences
        for i in range(numofarts):
            extractive = data["documents"][i]["extractive"]
            extra_indices_set.append(extractive)

        # create tgt_list
        tgt_list = list()
        for i in range(numofarts):
            mydict = {}
            
            sents = list()
            for idx in extra_indices_set[0]:
                sent = src_list[i]['src_txt'][idx-2]
                sents.append(sent)
            # update extra_indices_set
            del extra_indices_set[0]

            if len(extra_indices_set) == 0:
                break
            
            mydict['tgt_txt'] = sents
            tgt_list.append(mydict)

        return tgt_list

def main():
    src_list = src_txt()
    tgt_list = tgt_txt(src_list)

if __name__ == "__main__":
    main()