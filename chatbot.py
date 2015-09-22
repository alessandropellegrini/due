#!/usr/bin/python

import pickle,random

successorlist=pickle.load(open('training-set','rb'))

def nextword(a):
    if a in successorlist:
        return random.choice(successorlist[a])
    else:
        return 'il'

def generate_reply(message):
    s=random.choice(message.split())
    response=''
    while True:
        neword=nextword(s)
        response+=' '+neword
        s=neword
        if neword[-1] in ',?!.':
            break

    if response[-1] == ',':
        response = response[:-1] + '.'
    
    return response
