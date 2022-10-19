from speech_recognition import speech_result
import streamlit as st

desd_words = ['baby', 'one', 'boat', 'do', 'car']


st.title("Online DESD")

if "current_word" not in st.session_state:
    st.session_state.counter = 0
    st.session_state.current_word = desd_words[st.session_state.counter]

if st.button('Next Word'):
    st.write("Say this word: ")
    st.header(st.session_state.current_word)
    st.session_state.counter += 1
    st.session_state.current_word = desd_words[st.session_state.counter]
    st.write(speech_result())
