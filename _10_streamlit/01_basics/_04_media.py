import streamlit as st

st.title("Media - image")
# 서버 이미지
st.image("../data/image01.jpg", caption="아아 그랬구나")

# 웹 이미지
imate_url = "https://t1.daumcdn.net/cafeattach/aVeZ/8101c70b1bc9e2fdb417c8f61e9339517449e07e"
st.image(imate_url, caption="웹 이미지")




