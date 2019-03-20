from cal import cos_similarity
from preprocess import sentence_cut, sentence_to_vec, load_word_vec
from intent_analysis import suject_analysis
import numpy as np
import re

# 加载词向量 记得重写这段代码
# PATH = "sgns.baidubaike.bigram-char"
# global word_vec 
# word_vec = load_word_vec(path=PATH)
# # 用同义词的平均值代替OOV
# word_vec["德勤数智研究院"] = list(np.array(word_vec["德勤"] + word_vec["研究院"])/2)
# word_vec["数智研究院"] = word_vec["德勤数智研究院"]
# word_vec["RPA"] = list(np.array(word_vec["机器人"] + word_vec["自动化"])/2)

print("你好，我是来自德勤数智研究院的小Z，你可以问我一切关于德勤数智研究院的问题。我不接受闲聊哟~")
while True: 
    question = input()
    if_next, response = suject_analysis(question)
    #print(if_next,response)
    if if_next == 1:
        print("搜索关于%s的答案"%response)
    elif if_next == 2:
        answer = '你是不是想问"' +response + '"'
        print(answer)
        response = input()
        if re.sub(r'[^\w\s]','',response) in ['是的','是']:
            print("搜索关于%s的答案"%response)
        elif re.sub(r'[^\w\s]','',response) in ['不是的','不是','不']:
            print('那麻烦您重新提问。')

    else:
        print("不好意思，我好像不太理解你的问题，可以重新描述一遍吗？")