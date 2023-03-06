import streamlit as st
from splitting import *

st.set_page_config(layout="wide", page_title="Aspen Progress Report Splitter")
st.write("## Split PDF with progress reports for a whole class into individual PDFs for each student")

st.sidebar.write("## Upload and download")
mainreport = st.sidebar.file_uploader("Upload a report", type=["pdf"])

st.sidebar.button(label="Split Report", on_click=SplitReport(mainreport,alreadyOpened=True))