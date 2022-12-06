import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Online DESD")

st.write('The DESD is a screening test that allows for assessment of a student\'s specific reading difficulties and whether the student is at risk for dyslexia. The test identifies the specific skills that a child brings to bear o nthe task of reading words. It consists of three sections: Decoding, Eidetic Encoding and Phonetic Encoding.')
st.write('The Decoding section provides a measure of sight-word recognition (Reading Standard Score). Indicators in the Encoding section allow the examiner to distinguish deficits in sight-word recognition from deficits in phonetic analysis. This makes it easier to detect and describe reading problems and to refer students for appropriate educational therapy')

if st.button('Begin Test'):
    switch_page("Decoding")