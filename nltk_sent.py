# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:09:18 2022

@author: irina
"""

import streamlit as st
import nltk


text=st.text_input('Введите предложение для разбора')
#text="This story is about something that happened to them when they were sent away from London during the war because of the air-raids."

st.title("Разбор предложения по частям речи")
st.write(text)

text_tokens =nltk.pos_tag(nltk.word_tokenize(text))

option=st.selectbox("Какую часть речи Вы хотите удалить(по умолчанию- существительные) ?", ['существительные', 'прилагательные', 'местоимения', 'глаголы'])
choice=[]
if option=='существительные':
    choice=['NN', 'NNS', 'NNP', 'NNPS']
elif option=='прилагательные':
    choice=['JJ', 'JJR', 'JJS']
elif option=='местоимения':
    choice=['PRP', 'PRP$']
elif option=='глаголы':
    choice=['VB', 'VBG', 'VBD', 'VBN', 'VBP', 'VBZ', 'MD' ]
else:
    choice=['NN', 'NNS', 'NNP', 'NNPS']
text_new=''
for i in text_tokens:
    print(i[1])
    if i[1] in choice:
        text_new+='___________ '
    else:    
        text_new+= ' '+ i[0] + ' '
print(text_new)
st.write(text_new)
        
