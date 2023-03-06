import streamlit as st
from splitting import *

st.set_page_config(layout="wide", page_title="Aspen Progress Report Splitter")
st.write("## Split PDF with progress reports for a whole class into individual PDFs for each student")

st.sidebar.write("## Upload the report")
mainreport = st.sidebar.file_uploader("Upload a report", type=["pdf"])

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
    
if mainreport!=None:
    displayPDF(mainreport)