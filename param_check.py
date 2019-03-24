import configparser 
import os 

#config = configparser.ConfigParser()
#config.read('model_v1/param.cfg')

def check(config):
    """
    检查配置文件各参数是否合理.
    Args:
        config:
            配置文件
    Returns:
        None
    """
    try:
        word_vec_path=config.get('Path', 'word_vec_path')
        qa_set_path = config.get('Path', 'qa_set_path')
    except:
        print('请在配置文件中输入问答集和词向量文件的路径。')
        exit(1)
        
    if os.path.isfile(word_vec_path) != True:
        print('请输入正确的词向量文件路径')
        exit(1)
    if os.path.isfile(qa_set_path) != True:
        print('请输入正确的问答集文件路径')
        exit(1)
    
    try:
        threshold = config.get('Model', 'threshold')
    except:
        print('请在配置文件中输入可接受最小相似度(0到1之间)。')
        exit(1)
    
    if float(threshold)<0 or float(threshold) > 1:
        print('可接受最小相似度范围为0到1之间。请重新配置。')
        exit(1)

