import streamlit as st 
from supabase import create_client,client
from supabase import create_client

supabase:client=create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)