import streamlit as st

st.title("테스트 파일입니다")
st.header("테테테테스트")

# Button
if st.button("버튼"):
    st.write("버튼을 누르셨네요")

# Check box
checkbox_btn = st.checkbox('체크박스')
if checkbox_btn:
    st.write('체크박스를 누르셨네요')

