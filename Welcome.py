import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Online DESD")

st.write('Description of the DESD Test *TODO*')

if st.button('Begin Test'):
    switch_page("Decoding")