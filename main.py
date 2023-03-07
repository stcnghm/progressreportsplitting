import streamlit as st
import splitting


splitter = splitting.Splitter()

def splitreportbuttonfunction(*args):
  splitter.SplitReport(*args)
  st.sidebar.download_button("Download",outdir)
  
st.set_page_config(layout="wide", page_title="Aspen Progress Report Splitter")
st.write("## Split PDF with progress reports for a whole class into individual PDFs for each student")

st.sidebar.write("## Upload and download")
mainreport = st.sidebar.file_uploader("Upload a report", type=["pdf"])

outdir = st.sidebar.text_input("Enter a name to be used as the folder name to download", value='reports')
st.sidebar.button(label="Split Report", on_click=splitreportbuttonfunction, args=(mainreport, outdir, True))
