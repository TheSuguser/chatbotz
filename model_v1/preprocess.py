import numpy as np
import jieba
import jieba.posseg as psg

# jieba中加入新词
jieba.add_word("德勤数智研究院",tag="nt")
jieba.add_word("数智研究院",tag="nt")
jieba.add_word("区块链",tag="n")
jieba.add_word("RPA",tag="n")
jieba.add_word("大数据",tag="n")

def load_word_vec(path):
    word_vec = {}
    with open(path) as f:
        try:
            while True:
                text_line = f.readline().strip('\r\t\n ')
                if text_line:
                    text_data = text_line.split(' ')
                    word_vec[text_data[0]] = []
                    for i in text_data[1:]:
                        word_vec[text_data[0]].append(float(i))
                else:
                    break
        finally:
            f.close()
    return word_vec

def sentence_cut(sentence):
    """
    分词
    Args:
        sentence[String]
    Returns:
        list
    """
    return [x for x in jieba.cut(sentence)]

def sentence_psg_cut(sentence):
    pairs =  [x for x in psg.cut(sentence)]
    words = []
    tags = []
    for pair in pairs:
        pair = list(pair)
        words.append(pair[0])
        tags.append(pair[1])
    return words, tags

def sentence_to_vec(sentence,word_vec):
    """
    返回句向量
    Args:
        sentence[String]: 需要转换成向量的句子
        word_vec: 训练好的词向量文件
    Return:
        vec[Array]: 句向量
    """
    vec = []
    words = sentence_cut(sentence)
    for word in words:
        if word in word_vec:
            vec.append(word_vec[word])
    return np.mean(vec, axis=0)