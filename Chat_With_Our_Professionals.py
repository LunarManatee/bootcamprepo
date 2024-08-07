import streamlit as st
import time
import random as rd
import datetime

st.header('Chat With Professionals - 🗪')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message['role'] == 'user':
        datum=message.get('date', None)
        st.markdown(datum)
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What's Up?"):
    temp = datetime.datetime.now()
    date = temp.strftime("%c")
    st.markdown(date)
    with st.chat_message('user'):
        st.markdown(prompt)
    st.session_state.messages.append({"date": date, "role":"user", "content":prompt})

#bot response

if prompt:
    response = f"Echo: {prompt}"
    with st.chat_message('assistant'):
        widget = st.empty()
        for i in range(0, rd.randint(7, 8)):
            widget.markdown('.')
            time.sleep(0.2)
            widget.markdown('..')
            time.sleep(0.2)
            widget.markdown('...')
            time.sleep(0.2)
        widget.markdown(response)
    st.session_state.messages.append({"role":"assistant", "content":response})