<h1 align="center">
  <br>
  <a href="https://github.com/TheSuguser/chatbotz"><img src="https://github.com/TheSuguser/chatbotz/raw/zzheng/img/logo.png" alt="Markdownify" width="400"></a>
  <br>
  ChatbotZ
  <br>
</h1>

<h4 align="center">本项目是一个封闭域内的聊天问答机器人。</h4>

## How to use
### 依赖
* python = 3.6
* numpy = 1.16.2
* jieba = 0.39
* pandas = 0.24.2
* scipy = 1.2.1

也可通过``requirements.txt``用``pip``直接安装依赖。建议在虚拟环境中使用。
```
# Clone this repository
$ git clone https://github.com/TheSuguser/chatbotz.git

# Go into the repository
$ cd chatbotz

# Install the dependencies
$ pip install -r requirements.txt
```

### 配置文件
ChatbotZ的相关配置在``param.cfg``中。因为词向量文件太大，因此没有上传在github上，需要自行下载，并在``word_vec_path``后添加词向量文件的路径。推荐使用基于百度百科训练的词向量。[下载地址](https://pan.baidu.com/s/1Gndr0fReIq_oJ3R34CxlPg)

## How it works
### ChatbotZ基本运行逻辑
ChatbotZ的基本运行逻辑如下图所示
![](img/chatbotz_process.png)

