# -*- coding: utf-8 -*-
import argparse
from ctypes.wintypes import tagRECT
import time
import os
from tokenize import Token
from turtle import ScrolledCanvas
import pandas as pd
import ast
import json
import six
import glob
import numpy as np
from tqdm import tqdm
from kiwipiepy import Kiwi

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-mode', default='', type=str, choices=['train','valid','test'])
    parser.add_argument('-news_dir', default='', type=str, help='target file to json')
    parser.add_argument('-output', default='', type=str, help='json output directory')

    # parser.random_state("-random_state", default="", type=int, help="random state")

    args = parser.parse_args()
    mode = args.mode
    news_dir = args.news_dir
    output = args.output

    # main process
    news_path = r'./raw_data/train_sample_copy.json'
    with open(news_path, 'r') as file:
        data = json.load(file, strict=False)
    
        src_list = list()
        numofarts = len(data["documents"])
        # create src_list
        for i in range(numofarts):
            article = data["documents"][i]["text"]

            # empty list delete
            for sentence in article:
                if len(sentence) == 0:
                    del article[article.index(sentence)]
            art_length = len(article)

            temp_list2 = list()
            # analyze each sentence's morphs
            for j in range(2, art_length):
                # for each sentence
                for idx in range(len(article[j])):
                    kiwi = Kiwi()
                    temp_list1 = []
                    tokenize_list = kiwi.tokenize(article[j][idx]["sentence"])[:-1]
                    # create src's 'word/morph' structures
                    for z in range(len(tokenize_list)):
                        token = tokenize_list[z].form + '/' + tokenize_list[z].tag
                        temp_list1.append(token)
                    temp_list2.append(temp_list1)
            src_list.append(temp_list2)
            print(("{} completed".format(i)))         
        print("src_list completed")

        extra_indices_set = list()
        # extract the indices of extractive sentences
        for i in range(numofarts):
            extractive = data["documents"][i]["extractive"]
            extra_indices_set.append(extractive)
        print("extraction completed")

        # create tgt_list
        tgt_list = list()
        for i in range(numofarts):
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
        # type conversion
        list_dic = list()
        for i in range(numofarts):
            mydict = {}
            mydict['src'] = src_list[i]
            mydict['tgt'] = tgt_list[i]
            list_dic.append(mydict)
        
        # create json file
        file_path = "./json_data/korean.train.1.json"

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(list_dic, f, ensure_ascii=False)
        # temp = list()
        # for i,a in enumerate(tqdm(list_dic)):
        #     if (i+1)%6 != 0:
        #         temp.append(a)
        #     else:
        #         filename = 'korean.'+mode+'.'+str(i//6)+'.json'
        #         with open(output+"/"+filename, "w", encoding='utf-8') as json_file:
        #             json.dump(temp, json_file, ensure_ascii=False)
        #         temp = []
if __name__ == '__main__':
    main()