import streamlit as st

st.header('st.button')

if st.button('Say hey'):
     st.write('You said hey')
else:
     st.write('Bye, thanks for using this app')