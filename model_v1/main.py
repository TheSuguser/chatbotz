from cal import cos_similarity
from preprocess import sentence_cut, sentence_to_vec, load_word_vec
from intent_anlysis import suject_analysis
import numpy as np

# 加载词向量 记得重写这段代码
PATH = "model_v1/sgns.baidubaike.bigram-char"
global word_vec 
word_vec = load_word_vec(path=PATH)

# 用同义词的平均值代替OOV
word_vec["德勤数智研究院"] = list(np.array(word_vec["德勤"] + word_vec["研究院"])/2)
word_vec["数智研究院"] = word_vec["德勤数智研究院"]
word_vec["RPA"] = list(np.array(word_vec["机器人"] + word_vec["自动化"])/2)

print("你好，我是来自德勤数智研究院的小Z，你可以问我一切关于德勤数智研究院的问题。")
while True: 
    question = input()
    if_next, response = suject_analysis(question)
    print(if_next,response)