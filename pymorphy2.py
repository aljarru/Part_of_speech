# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:09:18 2022

@author: irina
"""

import streamlit as st
import re
import nltk



text="This story is about something that happened to them when they were sent away from London during the war because of the air-raids."

st.title("Разбор предложения по частям речи")
st.write(text)
text_tokens =nltk.pos_tag(nltk.word_tokenize(text))
st.write(text_tokens)
