# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pandas as pd 

def read_data():
    f1 = open("data/questions.txt")
    f2 = open("data/answers.txt")

    q = f1.readlines()
    a = f2.readlines()

    data = []

    for i in range(len(q)):
        data.append(q[i])
        data.append(a[i])
    
    return data  

training_date = read_data()
bot = ChatBot("chatbotz")
trainer = ListTrainer(bot)
trainer.train(training_date)

while True:
    try:
        user_input = input()
        res = bot.get_response(user_input)
        print(res)
    
    except (KeyboardInterrupt, EOFError, SystemExit):
        break




    

