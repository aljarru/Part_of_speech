# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 09:09:18 2022

@author: irina
"""
import streamlit as st
import pymorphy2 as pm
import pymorphy2_dicts_ru as ru


text='Повесть эта о том, что случилось, когда твой дедушка был еще маленьким. Ее очень важно прочесть, чтобы понять, как возникла связь между нашим миром и Нарнией.'

st.title("Разбор предложения по частям речи")
st.write(text)
st.write(text)