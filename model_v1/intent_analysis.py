import jieba
from preprocess import sentence_cut, sentence_psg_cut
import re

def suject_analysis(sentence):
    cors = ["德勤数智研究院", "数智研究院"]  
    if max([c in sentence for c in cors]):
        return 1, sentence 
    else:
        words, tags = sentence_psg_cut(sentence)
        if "nt" in tags:
            ind = tags.index("nt")
            pattern = words[ind]
            response = sentence.replace(pattern, "德勤数智研究院")
            return 2, response
        else:
            n_tags = ["r","nt","nr","ns","n","nz"]
            for n in n_tags:
                for i in range(len(tags)):
                    if n==i:
                        response = sentence.replace(words[i],"德勤数智研究院")
                        return 2, response
    return 3, sentence


#print(suject_analysis("我能问些什么？"))