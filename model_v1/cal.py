import numpy as np
from scipy.linalg import norm

def cos_similarity(vec1, vec2):
    """
    计算两个向量之间的余弦相似度
    Args:
        vec1[Array]:  
        vec2[Array]:   
    Returns:
        similariy[Float]: vec1和vec2之间的余弦相似度
    """
    similarity = np.dot(vec1,vec2) / (norm(vec1) * norm(vec2))

    return similarity
