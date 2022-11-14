from speech_recognition import speech_result
import streamlit as st
import time
from streamlit_extras.switch_page_button import switch_page

st.title("Online DESD")

if "current_word" not in st.session_state:
    st.session_state.desd_words = {
                'K': {'baby': True, 'one': None, 'boat': True, 'do': True, 'car': True},
                '1L': {'was': True, 'daddy': True, 'book': True, 'good': True, 'doll': True},
                '1U': {'girl': True, 'apple': True, 'they': True, 'story': True, 'some': True},
                '2': {'above': True, 'what': True, 'any': True, 'busy': True, 'night': True},
                '3': {'done': True, 'huge': True, 'ocean': True, 'station': True, 'could': True},
                '4': {'because': False, 'echo': False, 'couple': False, 'eager': True, 'together': True},
                '5': {'bought': False, 'delicious': False, 'neighbor': True, 'achieve': True, 'region': True},
                '6': {'malicious': False, 'bureau': None, 'similar': None, 'campaign': None, 'waltz': None},
                '7-8': {'prairie': None, 'gadget': None, 'facsimile': None, 'emphasize': None, 'prescription': None},
                '9-12': {'zealous': None, 'clique': None, 'atrocious': None, 'catastrophe': None, 'liquidate': None}
            }
    st.session_state.counter = 0
    st.session_state.level_counter = 0
    st.session_state.current_word = list(st.session_state.desd_words[list(st.session_state.desd_words)[st.session_state.counter]])[st.session_state.level_counter]
    st.session_state.correct = 0
    st.session_state.wrong = 0
    st.session_state.total_wrong = 0
    st.session_state.level_correct = 0
    st.session_state.grade_level = 'K'

if st.button("Next Word"):
    
    st.write("Say this word: ")
    time.sleep(0.75)
    st.header(st.session_state.current_word)

    current_level = list(st.session_state.desd_words)[st.session_state.counter]
    if speech_result() == st.session_state.current_word:
        st.session_state.correct += 1 
        st.session_state.desd_words[current_level][st.session_state.current_word] = True
    else:
        st.session_state.desd_words[current_level][st.session_state.current_word] = False
        st.session_state.wrong += 1
        st.session_state.total_wrong += 1
    
    st.session_state.level_counter += 1
    
    if st.session_state.correct >= 3:
        st.session_state.grade_level = list(st.session_state.desd_words)[st.session_state.counter]
    
    # st.write(f"Current Level Correct: {st.session_state.correct}")
    # st.write(f"Current Level Wrong: {st.session_state.wrong}")
    # st.write(f"Total Wrong: {st.session_state.total_wrong}")
    # st.write(f"Counter: {st.session_state.counter}")
    # st.write(f"Level Counter: {st.session_state.level_counter}")

    if st.session_state.wrong >= 3 and st.session_state.total_wrong >= 5 and st.session_state.level_counter >= 5:
            st.write(f"Reading Level: {st.session_state.grade_level}")
            st.write(st.session_state.desd_words)
            time.sleep(1)
            st.write(f"Beginning Encoding Section")
            time.sleep(2)
            switch_page("Encoding_Eidetic")
    
    if st.session_state.level_counter >= 5:
        st.session_state.counter += 1 
        st.session_state.level_counter = 0 
        st.session_state.correct = 0
        st.session_state.wrong = 0
    
    st.session_state.current_word = list(st.session_state.desd_words[list(st.session_state.desd_words)[st.session_state.counter]])[st.session_state.level_counter]

