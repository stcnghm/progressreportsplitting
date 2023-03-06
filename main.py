import streamlit as st
from splitting import *

st.set_page_config(layout="wide", page_title="Aspen Progress Report Splitter")
st.write("## Split PDF with progress reports for a whole class into individual PDFs for each student")

st.sidebar.write("## Upload the report")
mainreport = st.sidebar.file_uploader("Upload a report", type=["pdf"])

pdfdisplay = f'<iframe src="{mainreport};base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
st.markdown(pdfdisplay, unsafe_allow_html=True)