# -*- coding: utf-8 -*-
from cal import cos_similarity
from process import sentence_cut, sentence_to_vec, load_word_vec, get_similarity_df, get_answer, get_random_question
from intent_analysis import suject_analysis
from param_check import check
import numpy as np
import pandas as pd
import re
import configparser

print('小Z正在启动噢，请耐心等待...')

# 加载配置文件
print('正在加载配置文件')
config = configparser.ConfigParser()
config.read('../model_v1/param.cfg')
check(config)

# 加载词向量 
print('正在加载词向量')
word_vec_path = config.get('Path','word_vec_path')
global word_vec 
word_vec = load_word_vec(path=word_vec_path)

# 用同义词的平均值代替OOV
word_vec["德勤数智研究院"] = list((np.array(word_vec["德勤"]) + np.array(word_vec["研究院"]))/2)
word_vec["数智研究院"] = word_vec["德勤数智研究院"]
word_vec["RPA"] = list((np.array(word_vec["机器人"]) + np.array(word_vec["自动化"]))/2)
word_vec['区块链']=list((np.array(word_vec["区块"]) + np.array(word_vec["链"]))/2)
word_vec['云']=list((np.array(word_vec["互联网"]) + np.array(word_vec["计算"]))/2)

# 加载问答集
print('正在加载问答集')
qa_set_path = config.get('Path','qa_set_path')
df_qa = pd.read_csv(qa_set_path,names=['question','answer'])

# 获得模型可接受最小相似度
threshold = float(config.get('Model', 'threshold'))

print('*****************************************************************')
print('你好，我是来自德勤数智研究院的小Z，你可以问我一切关于德勤数智研究院的问题。我可不接受闲聊哟~')
status = 0
response_next = ''

while True: 
    if status==0:
        question = input()
    else:
        status = 0
        question = response_next
    if_next, response = suject_analysis(question)

    if if_next == 1:
        answer, similarity = get_answer(response,df_qa, word_vec)
        if similarity >= threshold:
            print(answer)
        else:
            response = get_random_question(df_qa)
            print('不好意思，我好像不太理解你的问题，可以重新描述一遍吗？或者你可以问我“%s”。'%response)

    elif if_next == 2:
        answer = '你是不是想问"' +response + '"'
        print(answer)
        response_next = input()
        if re.sub(r'[^\w\s]','',response_next) in ['是的','是','Yes','yes']:
            answer, similarity = get_answer(response, df_qa, word_vec)
            if similarity >=threshold:
                print(answer)
            else:
                response = get_random_question(df_qa)
                print('不好意思，我好像还是不太理解你的问题，可以重新描述一遍吗？或者你可以问我“%s”。'%response)

        elif re.sub(r'[^\w\s]','',response_next) in ['不是的','不是','不', 'no', 'Non']:
            print('那麻烦您重新提问。')
        else:
            status = 1
    else:
        response = get_random_question(df_qa)
        print('不好意思，我好像不太理解你的问题，可以重新描述一遍吗？或者你可以问我“%s”。'%response)