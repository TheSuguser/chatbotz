import jieba
from process import sentence_cut, sentence_psg_cut
import re

def subject_analysis(sentence):
    """
    主语分析。判断句子中是否包换德勤数智研究院。如果没有包含，则替换掉句子的主语。如果句子不存在可替换的主语，则输出原句
    Args:
        sentence: String
            输入问句
    Returns:
        status: Int
            状态表示符。1代表主语中包括德勤数智研究院; 2代表不包含德勤数智研究院，但存在可替换主语;
            3表示不存在可替换主语。
        response: String
            原句或完成替换的句子
    """
    cors = ['德勤数智研究院', '数智研究院', '数智']  
    if max([c in sentence for c in cors]):
        return 1, sentence 
    else:
        words, tags = sentence_psg_cut(sentence)
        if 'nt' in tags:
            ind = tags.index('nt')
            pattern = words[ind]
            response = sentence.replace(pattern, '德勤数智研究院')
            return 2, response
        else:
            n_tags = ['nt','nr','','ns','n','nz','r']
            for n in n_tags:
                for i in range(len(tags)):
                    if n==tags[i]:
                        response = sentence.replace(words[i],'德勤数智研究院')
                        return 2, response
    return 3, sentence

#print(subject_analysis("腾讯能做什么？"))


