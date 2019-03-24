import numpy as np
import jieba
import jieba.posseg as psg
import pandas as pd
from cal import cos_similarity

# jieba中加入新词
jieba.add_word("德勤数智研究院",tag="nt")
jieba.add_word("数智研究院",tag="nt")
jieba.add_word("区块链",tag="n")
jieba.add_word("RPA",tag="n")
jieba.add_word("大数据",tag="n")

def load_word_vec(path):
    """
    加载词向量文件
    Args:
        path: String
            词向量文件路径
    Returns:
        word_vec: Dictionary
            词向量
    """
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
        sentence: String
            输入句
    Returns:
        result: List
            存有各个分词的list
    """
    return [x for x in jieba.cut(sentence)]

def sentence_psg_cut(sentence):
    """
    分词（带词性）
    Args:
        sentence: String 
            输入句
    Returns:
        words: List 
            分词结果
        tags: List
            每个分词对应的词性
    """
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
        sentence: String 
            需要转换成向量的句子
        word_vec: Dictionary
            训练好的词向量文件
    Returns:
        vec: Array
            句向量
    """
    vec = []
    words = sentence_cut(str(sentence))
    for word in words:
        if word in word_vec:
            vec.append(np.array(word_vec[word]))
    #print([v.shape for v in vec])
    vec = np.vstack(vec)
    return np.mean(np.array(vec), axis=0)

def get_similarity_df(sentence, df_qa, word_vec):
    """
    Args:
        sentence: String 
            问句
        df_qa: Dataframe 
            问答集
    Returns:
        df_aq: Dataframe
            添加了similarity列的问答集
    """
    s = []
    vec1 = sentence_to_vec(sentence, word_vec)
    for q in df_qa['question']:
        vec2 = sentence_to_vec(q, word_vec)
        s.append(cos_similarity(vec1,vec2))
    df_qa['similarity'] = s 
    
    return df_qa

def get_answer(sentence, df_qa, word_vec):
    """
    获得similarity最大的答案
    Args:
        sentence: String 
            输入问句
        df_qa: Dataframe 
            问答集
        word_vec: Dictionary 
            词向量文件
    Returns:
        answer: String
            答案
        similarity: Float
            相似度
    """
    df_sim = get_similarity_df(sentence, df_qa,word_vec)
    print(df_sim)
    idx = df_sim['similarity'].idxmax
    return df_sim['answer'][idx], df_sim['similarity'][idx]

def get_random_question(df_qa):
    """
    从问答集中随机输出一个问题
    Args:
        df_qa: Dataframe
            问答集
    Returns:
        question: String
            随机一个问题
    """
    idx = np.random.randint(0,df_qa.shape[0])
    return df_qa['question'][idx]

