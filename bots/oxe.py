# -*- coding: utf-8 -*-

import nltk
import numpy as np
import random
import string
from sklearn.features_extration.text import Tfidfvectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open('copus.txt', 'r', errors = 'ignore') as f:
    raw = f.read().lower()

nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETINGS_INPUTS = ("hello", "hi","grettings", "sup", "what's up", "hey",)
GREETINGS_RESPONSES =["hi", "hey", "*nods*", "hi there","hello", "i'm so glad"]

def greeting(setence):
    for word in setence.split():
        if word.lower() in GREETINGS_INPUTS:
            return random.choice(GREETINGS_RESPONSES)

def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    
    TfidfVec = TfidfVecttorizer(tokenizer=LemNormalizer,stop_words='english')
    tfidf =TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1],tfidf)
    idx = vals.argsort() [0] [-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf == 0):
        robo_response += "I can't undesteand you"
    else:
        robo_response += sent_tokens[idx]

    return robo_response
    
    
flag = True
print("ROBO: My name is botinho and i will answer all your question about chatbots. If you want to exit type Bye")

while(flag):
    user_response = input().lower()

    if(user_response == 'Bye'):
        flag = False
        print("ROBO: BYE...TAKE CARE......")

    else:
        if(greeting(user_response)):
            print("ROBO:" + greeting(user_response))

        else:
            print("ROBO:", end="")
            print(response(user_response))
            sent_tokens.remove(user_response)

    
    
    
    
    

    
