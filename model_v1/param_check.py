import configparser 
import os 

#config = configparser.ConfigParser()
#config.read('model_v1/param.cfg')

def check(config):
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
    

