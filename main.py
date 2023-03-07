import streamlit as st
import splitting

st.set_page_config(layout="wide", page_title="Aspen Progress Report Splitter")
splitter = splitting.Splitter()
  
st.write("## Split PDF with progress reports for a whole class into individual PDFs for each student")
st.sidebar.write("## Upload and download")
sbcont1 = st.sidebar.container()
sbcont2 = st.sidebar.empty()

def splitreportbuttonfunction(*args):
  splitter.SplitReport(*args)
  sbcont2.download_button("Download",splitter.outdir, splitter.outdir)

mainreport = sbcont1.file_uploader("Upload a report", type=["pdf"])

outdir = sbcont1.text_input("Enter a name to be used as the folder name to download", value='reports')
sbcont1.button(label="Split Report", on_click=splitreportbuttonfunction, args=(mainreport, outdir, True))
