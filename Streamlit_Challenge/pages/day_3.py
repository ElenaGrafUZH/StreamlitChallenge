import streamlit as st

st.header("Challenge Day 3")

if st.button('Say hello'): #if button clicked then
    st.write('Why hello there')
else:
    st.write('Goodbye')