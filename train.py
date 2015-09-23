#!/usr/bin/python

import sys
import pickle

text=[]
trainset=str(sys.argv[1])

for line in open(trainset):
    for word in line.split():
        text.append (word)

textset=list(set(text))
follow={}
for l in range(len(textset)):
    working=[]
    check=textset[l]
    for w in range(len(text)-1):
        if check==text[w] and text[w][-1] not in '(),.?!':
            working.append(str(text[w+1]))
    follow[check]=working
a=open('training-set','wb')
pickle.dump(follow,a,2)
a.close()
