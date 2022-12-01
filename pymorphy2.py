# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:09:18 2022

@author: irina
"""

import streamlit as st
import re
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize



text="This story is about something that happened to them when they were sent away from London during the war because of the air-raids."

st.title("Разбор предложения по частям речи")
st.write(text)
text_clean=re.sub(r'[.,"\'-?:!;]', '', text)
text_lower=text_clean.lower()
st.write(text_lower)
li=list(text_lower.split(" "))
st.write(li)
text_tokens = word_tokenize(text)

text_tagged = pos_tag(li)
st.write(text_tagged)
