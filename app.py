import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

def main():
    # st.header("This is title")
    # name=st.text_input("enter your name")
    
    # col1, col2=st.columns(2,gap='small')
    # with col1:
    #     if st.button("display my name",type="primary",key='btn1',width='stretch'):
    #         print("hi",name)
    # with col2:
    #     if st.button("bye",type="primary",key='btn2',width='stretch'):
    #         print("bye")
    if 'login_type' not in st.session_state:
        st.session_state['login_type']=None
    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case None:
            home_screen()
            
    
main()