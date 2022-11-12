import streamlit as st
import decoding_phonetic
import numpy as np
from streamlit_extras.switch_page_button import switch_page

st.title('Type the word you hear spoken exactly how sounds.')
st.header('Correct spelling is not required.')
st.write("For instance, the word laugh could be spelled 'laf'.")


if 'phonetic_words' not in st.session_state:
	wrong_words = {}
	for level in st.session_state.desd_words:
		wrong_words[level] = []
		for word, correct in st.session_state.desd_words[level].items():
			if correct == False or correct == None:
				wrong_words[level].append(word)
	st.session_state.phonetic_words = wrong_words[st.session_state.grade_level]
    
	i = list(wrong_words).index(st.session_state.grade_level)
	while len(st.session_state.phonetic_words) < 5:
		i += 1
		for word in list(wrong_words.items())[i][1]:
			st.session_state.phonetic_words.append(word)

answers = []
test_words = st.session_state.phonetic_words[:5]
with st.form("my_form"):
	for i, word in enumerate(test_words):
		audio_file = open(f'audio_files/{word}.mp3', 'rb')
		audio_bytes = audio_file.read()
		st.audio(audio_bytes, format='audio/mp3')
		answers.append(st.text_input(f'Word # {i+1}'))

   # Every form must have a submit button.
	submitted = st.form_submit_button("Submit")
	if submitted:
		st.session_state.phonetic_result = np.array([decoding_phonetic.correct(test_word, test_answer) for test_word, test_answer in list(zip(test_words, answers))])
		switch_page("Results")