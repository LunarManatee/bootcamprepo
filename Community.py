import streamlit as st
import time
import random as rd
import datetime

st.header('Community Chat - 👋')

name = 'Lunar'

if "messages_com" not in st.session_state:
    st.session_state.messages_com = []

for message in st.session_state.messages_com:
    datum=message.get('date', None)
    st.markdown(datum)
    with st.chat_message("user"):
        st.markdown(message["content"])

if prompt := st.chat_input("What's Up?"):
    temp = datetime.datetime.now()
    date = temp.strftime("%c")
    st.markdown(date)
    with st.chat_message('user'):
        st.markdown(f"{name}: {prompt}")
    st.session_state.messages_com.append({"date":date, "name":name, "content":f"{name}: {prompt}"})