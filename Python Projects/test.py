from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
me=load_lottieurl("https://lottie.host/efcd0c5b-43f0-4c65-854d-f8500db06bb4/dY0K1rU7tY.json")
img1=Image.open("images/streamlit_img.png")

with st.container():
    st.subheader("Hi, I am Adam Xu! :wave:")
    st.title("A secondary school student that is learning coding.")
    st.write("I hope everyone can get into learning coding and have fun with it.")
    st.write("[I want to learn to code in Python >](https://www.youtube.com/watch?v=kqtD5dpn9C8)")
    st.write("[I want to learn to code in C++ >](https://www.youtube.com/watch?v=ZzaPdXTrSb8)")

with st.container():
    st.write("---")
    l_col, r_col=st.columns(2)
    with l_col:
        st.header("All About Me")
        st.write("##")
        st.write(
            """
            - I like coding because I think it is fun and interesting to do.
            - I like player chess online because it is a good way to rest myself and just play a good game of chess.
            - I like skipping because it is good for my body.
            - I like eggs because they are delicious no matter how you cook them.
            - I like Fanta because it makes me refreshed.
            - I also have a gaming Youtube channel.
            """)
        st.write(st.write("[My Channel >](https://www.youtube.com/channel/UC-PTF-p8sJ_mIoala8nv1fg)"))
    with r_col:
        st_lottie(me, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    img_col, text_col=st.columns(2)
    with img_col:
        st.image(img1)
    with text_col:
        st.subheader("You can learn to make your own streamlit websites too!")
        st.write("[Learn More >](https://www.youtube.com/watch?v=VqgUkExPvLY)")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form="""
        <form action="https://formsubmit.co/adam.jq.xu@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>
        """
    l_col, r_col=st.columns(2)
    with l_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with r_col:
        st.empty()