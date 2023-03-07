import streamlit as st
import splitting

splitter = splitting.Splitter()

st.set_page_config(layout="wide", page_title="Aspen Progress Report Splitter")
st.write("## Split PDF with progress reports for a whole class into individual PDFs for each student")

st.sidebar.write("## Upload and download")
mainreport = st.sidebar.file_uploader("Upload a report", type=["pdf"])

st.sidebar.button(label="Split Report", on_click=splitter.SplitReport, args=(mainreport, True))
if mainreport:
  st.sidebar.download_button(label='Download', data=mainreport, mime='application/pdf')
filenamelist = splitter.filenamelist
for i in range(len(filenamelist)):
    filenamelist[i] = filenamelist[i].split('/')[-1]
st.write(f'Filenames: {filenamelist}')
st.sidebar.multiselect(label="Individual Reports", options=filenamelist, default=filenamelist)
