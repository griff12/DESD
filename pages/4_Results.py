import streamlit as st
import numpy as np

percent_eidetic = np.count_nonzero(st.session_state.eidetic_result)/st.session_state.eidetic_result.shape[0]
percent_phonetic = np.count_nonzero(st.session_state.phonetic_result)/st.session_state.phonetic_result.shape[0]

st.write(f'Reading Level: {st.session_state.grade_level}')
st.write(f'Eidetic Result: {percent_eidetic:.0%}')
st.write(f'Phonetic Result: {percent_phonetic:.0%}')