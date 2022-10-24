from speech_recognition import speech_result
import streamlit as st
import time

st.title("Online DESD")

if "current_word" not in st.session_state:
    st.session_state.desd_words = {
                'K': {'baby': False, 'one': False, 'boat': False, 'do': False, 'car': False},
                '1L': {'was': False, 'daddy': False, 'book': False, 'good': False, 'doll': False},
                '1U': {'girl': False, 'apple': False, 'they': False, 'story': False, 'some': False},
                '2': {'above': False, 'what': False, 'any': False, 'busy': False, 'night': False},
                '3': {'done': False, 'huge': False, 'ocean': False, 'station': False, 'could': False},
                '4': {'because': False, 'echo': False, 'couple': False, 'eager': False, 'together': False},
                '5': {'bought': False, 'delicious': False, 'neighbor': False, 'achieve': False, 'region': False},
                '6': {'malicious': False, 'bureau': False, 'similar': False, 'campaign': False, 'waltz': False},
                '7-8': {'prairie': False, 'gadget': False, 'facsimile': False, 'emphasize': False, 'prescription': False},
                '9-12': {'zealous': False, 'clique': False, 'atrocious': False, 'catastrophe': False, 'liquidate': False}
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
    st.header(st.session_state.current_word)

    if speech_result() == st.session_state.current_word:
        st.session_state.correct += 1 
        current_level = list(st.session_state.desd_words)[st.session_state.counter]
        st.session_state.desd_words[current_level][st.session_state.current_word] = True
    else:
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

    if st.session_state.wrong >= 3 and st.session_state.total_wrong >= 5:
            st.write(f"Reading Level: {st.session_state.grade_level}")
            st.write(st.session_state.desd_words)
            exit()
    
    if st.session_state.level_counter >= 5:
        st.session_state.counter += 1 
        st.session_state.level_counter = 0 
        st.session_state.correct = 0
        st.session_state.wrong = 0
    
    st.session_state.current_word = list(st.session_state.desd_words[list(st.session_state.desd_words)[st.session_state.counter]])[st.session_state.level_counter]
