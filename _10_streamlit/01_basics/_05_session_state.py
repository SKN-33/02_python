import args
import streamlit as st
from pandas.core.methods import describe

st.title("Session State")

description = """
- Streamlit 은 버튼 클릭 등 사용자 상호작용이 발생하면 스크립트(코드)를 위에서 아래로 다시 시작한다
- 그래서 일반 변수에 저장된 값들이 매번 초기화 된다
- session_state 를 이용하면 같은 사용자 안에서 값을 유지한다
    (사용자 기준 == 브라우저)
"""

st.markdown(description)

count: int = 0

# clicked = st.button("클릭 시 count 1 증가")
# clicked # Streamlit magic

if st.button("클릭 시 count 1 증가"):
    count += 1 # 카운트 1씩 증가

st.write("클릭한 횟수: ", count)

st.subheader("session_state를 이용한 count", divider="rainbow")

#session_state
# - 서버 컴퓨터 메모리 영역에 접속한 사용자별 객체

#st.session_state에 count가 없으면
# -> 최초 1회 접속 시에만 실행
if "count" not in st.session_state:
    st.session_state["count"] = 0

if st.button("클릭 시 st.session_state['count'] 1 증가"):
    st.session_state['count'] += 1 # 카운트 1씩 증가

if st.button("클릭 시 st.session_state['count'] 1 감소"):
    st.session_state['count'] -= 1 # 카운트 1씩 증가


st.write( "클릭한 횟수: ", st.session_state['count'])




