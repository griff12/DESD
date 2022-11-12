import streamlit as st
import numpy as np
from streamlit_extras.switch_page_button import switch_page

st.title('Type the word you hear spoken exactly how it should be spelled')
st.session_state.grade_level = '3'

if 'eidetic_words' not in st.session_state:
    correct_words = {}
    for level in st.session_state.desd_words:
        correct_words[level] = []
        for word, correct in st.session_state.desd_words[level].items():
            if correct:
                correct_words[level].append(word)
    st.session_state.eidetic_words = correct_words[st.session_state.grade_level]
    if len(st.session_state.eidetic_words) < 5:
        i = list(correct_words).index(st.session_state.grade_level) - 1
        for word in list(correct_words.items())[i][1]:
            st.session_state.eidetic_words.append(word)

text = []
test_words = st.session_state.eidetic_words[:5]
with st.form("my_form"):
	for i, word in enumerate(test_words):
		audio_file = open(f'audio_files/{word}.mp3', 'rb')
		audio_bytes = audio_file.read()
		st.audio(audio_bytes, format='audio/mp3')
		text.append(st.text_input(f'Word # {i+1}'))

   # Every form must have a submit button.
	submitted = st.form_submit_button("Submit")
	if submitted:
		st.session_state.eidetic_result = np.compare_chararrays(text, test_words, "==", rstrip=True)
		switch_page("Encoding_Phonetic")