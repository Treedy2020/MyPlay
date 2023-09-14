import json
import streamlit as st
from PIL import Image

if 'page_ind' not in st.session_state:
    st.session_state.page_ind = 1
    
def onclik_add():
    st.session_state.page_ind += 1

def onclik_sub():
    st.session_state.page_ind -= 1
    
pre, current, next = st.columns(3)
with pre:
    st.button('Previous', disabled=st.session_state.page_ind == 1, on_click=onclik_sub)
    
with current:
    st.button(f'Current: {st.session_state.page_ind}', disabled=True)
    
with next:
    st.button('Next', disabled=st.session_state.page_ind == 106, on_click=onclik_add)

with open('./show_data/res_show_in_ui.json', 'r') as f:
    st.session_state.show_data = json.load(f)

ind_1, ind_2, diff = st.session_state.show_data[str(st.session_state.page_ind - 1)]
image_path_1, image_path_2 = f'./show_data/ECE-100_03/page_{ind_1 + 1}.png', f'./show_data/ECE-100_02/page_{ind_2 + 1}.png'

col1, col2 = st.columns(2)
with col1:
    tab1, tab2 = st.tabs(['ECE-100_03.pdf', 'ECE-100_02 Amend 4.pdf'])
    with tab1:
        st.image(image_path_1, caption=f'ECE-100_03.pdf Page {ind_1 + 1}')
    with tab2:
        st.image(image_path_2, caption=f'ECE-100_02 Amend 4.pdf Page {ind_2 + 1}')
with col2:
    st.info(diff)


    

