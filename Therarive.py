import streamlit as st
from PIL import Image

st.set_page_config(layout='wide')

st.logo(Image.open("image/logo.png"), icon_image=Image.open("image/logo_icon.png"))

pg = st.navigation([st.Page("Home.py", title="Home"),
                    #st.Page("Depressions.py", title="Types of Depressions"),
                    st.Page("Chat_With_Our_Professionals.py", title="Chat With Professionals"),
                    st.Page("Community.py", title='Community')])
pg.run()
