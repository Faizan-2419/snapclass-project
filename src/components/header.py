import streamlit as st 

def header_home():
    logo_url="https://img.freepik.com/premium-photo/3d-student-icon-individual-educational-pursuit-illustration-logo_762678-75954.jpg"
    st.markdown(f"""
            <div style="display:flex; flex-direction:column;align-items:center;justify-content:center; margin-bottom:30px;margine-top:30px">
                <img src='{logo_url}' style='height:100px;'/>
                <h1 style="text-align:center; color:#E0E3FF">SNAP<br/>CLASS</h1>
            </div>
            
                """,unsafe_allow_html=True)

import streamlit as st 

def header_dashboard():
    logo_url="https://vbithyd.ac.in/wp-content/uploads/2021/01/alumni_icon-300x300.png"
    st.markdown(f"""
            <div style="display:flex; align-items:center;justify-content:center;gap:10px">
                <img src='{logo_url}' style='height:90px;transform: translateY(-5px);'/>
                <h2 style="text-align:left; color:#5865F2">SNAP<br/>CLASS</h1>
            </div>
            
                """,unsafe_allow_html=True)