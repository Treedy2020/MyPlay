import json
import fitz
import streamlit as st
from pdf2image import convert_from_path
from PIL import Image

@st.cache_data
def get_pdf_image(path):
    return convert_from_path(path)

if 'page_ind' not in st.session_state:
    st.session_state.page_ind = 1
    
if 'pdf_1' not in st.session_state:
    st.session_state.pdf_1 = get_pdf_image('./show_data/ECE-100_03.pdf')
if 'pdf_2' not in st.session_state:
    st.session_state.pdf_2 = get_pdf_image('./show_data/ECE-100_02 Amend 4.pdf')
    

pre, current, next = st.columns(3)
with pre:
    if st.button('Previous', disabled=st.session_state.page_ind == 0):
        st.session_state.page_ind -= 1

with current:
    st.button(f'Current: {st.session_state.page_ind}', disabled=True)
with next:
    if st.button('Next', disabled=st.session_state.page_ind == 105):
        st.session_state.page_ind += 1

with open('./show_data/res_show_in_ui.json', 'r') as f:
    st.session_state.show_data = json.load(f)

ind_1, ind_2, diff = st.session_state.show_data[str(int(st.session_state.page_ind) - 1)]

col1, col2 = st.columns(2)
with col1:
    tab1, tab2 = st.tabs(['ECE-100_03.pdf', 'ECE-100_02 Amend 4.pdf'])
    with tab1:
        st.image(st.session_state.pdf_1[ind_1], caption=f'ECE-100_03.pdf Page {ind_1 + 1}')
    with tab2:
        st.image(st.session_state.pdf_2[ind_2], caption=f'ECE-100_02 Amend 4.pdf Page {ind_2 + 1}')
with col2:
    st.info(diff)


    

