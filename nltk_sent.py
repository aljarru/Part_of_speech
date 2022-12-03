import streamlit as st
import nltk



text="This story is about something that happened to them when they were sent away from London during the war because of the air-raids."

st.title("Разбор предложения по частям речи")
st.write(text)

text_tokens =nltk.pos_tag(nltk.word_tokenize(text))

st.write("Удаляем существительные из текста")
text_new=''
for i in text_tokens:
    print(i[1])
    if i[1]=='NN':
        text_new+='___________'
    else:
        text_new+= ' '+ i[0] + ' '
print(text_new)
st.write(text_new)
