# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:09:18 2022

@author: irina
"""

import streamlit as st
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text=st.text_input('Enter a sentence: ')


st.title("Parsing a sentence by parts of speech")
st.write(text)

text_tokens =nltk.pos_tag(nltk.word_tokenize(text))

option=st.selectbox("Which part of speech do you want to delete (nouns by default) ?", ['nouns', 'adjectives', 'pronouns', 'глаголы'])
choice=[]
if option=='nouns':
    choice=['NN', 'NNS', 'NNP', 'NNPS']
elif option=='adjectives':
    choice=['JJ', 'JJR', 'JJS']
elif option=='pronouns':
    choice=['PRP', 'PRP$']
elif option=='verbs':
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
        
