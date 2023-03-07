import streamlit as st
import splitting
import os

st.set_page_config(layout="wide", page_title="Aspen Progress Report Splitter")
splitter = splitting.Splitter()
  
st.write("## Split PDF with progress reports for a whole class into individual PDFs for each student")
st.write('When you run the progress reports on Aspen, it gives you one PDF file with every student\'s progress report in it.')
st.write('This tool will let you split that file into one file for each student, with the student\'s name and the report date as the file name')
st.write('1) Select the report that you want to split')
st.write('2) Choose a name for a folder to put the individual reports into, and hit enter to confirm')
st.write('3) Click the split reports button. After you do this a download button will appear')
st.write('4) When you click the download button, your computer will download a zip file with all the reports in it')
st.sidebar.write("## Upload and download")
sbcont1 = st.sidebar.container()
sbcont2 = st.sidebar.container()
sbcont2.write(" ")

def splitreportbuttonfunction(*args):
  splitter.SplitReport(*args)
  sbcont2.download_button("Download",open(splitter.outdir, 'rb'), splitter.outdir, mime='application/zip',on_click=os.remove, args=(splitter.outdir,))

mainreport = sbcont1.file_uploader("Upload a report", type=["pdf"])

outdir = sbcont1.text_input("Enter a name to be used as the folder name to download", value='reports')
sbcont1.button(label="Split Report", on_click=splitreportbuttonfunction, args=(mainreport, outdir.replace(' ', '_'), True))
