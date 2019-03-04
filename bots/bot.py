# -*- coding: utf-8 -*-
from chatterbot import ChatBot

bot = ChatBot('Test' , trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

bot.train('chatterbot.corpus.portuguese')

while True:
    res = input('Você: ')
    resp = bot.get_response(res)
    print('Bot: ', resp)