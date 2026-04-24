import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home
from src.components.footer import footer_home
def home_screen():

    
    header_home()
    style_background_home()
    style_base_layout()
    col1,col2=st.columns(2, gap="large")
    
    with col1:
        st.header("I'm Student")
        st.image("https://png.pngtree.com/png-vector/20230903/ourmid/pngtree-3d-student-maintain-cleanliness-png-image_9943479.png",width=120)
        if st.button("student portal",type="tertiary",icon=":material/arrow_outward:", icon_position="right"):
            st.session_state['login_type']='student'
            st.rerun()
    with col2:
        st.header("I'm Teacher")
        st.image("https://cdn3d.iconscout.com/3d/premium/thumb/teacher-3d-icon-png-download-11785877.png",width=120)
        if st.button("teacher portal", type="tertiary", icon=":material/arrow_outward:", icon_position="right"):
            st.session_state['login_type']='teacher'
            st.rerun()
    footer_home()   