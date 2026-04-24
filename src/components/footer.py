import streamlit as st 

def footer_home():
    logo_url="blob:https://gemini.google.com/203b5de7-478f-4ede-870a-75c7344dfe2d"
    st.markdown(f"""
            <div style="margin-top:2rem; display:flex; gap:6px;justify-content:center;item-align:center">
                <p style="font-weight:bold; color:white">Created with🖤 </p>
                <img src='{logo_url}'style='max-height:25px'/>
            </div>
            
                """,unsafe_allow_html=True)