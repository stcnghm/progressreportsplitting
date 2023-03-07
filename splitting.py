# -*- coding: utf-8 -*-
import PyPDF2
import re
import tempfile
import streamlit as st
import zipfile
import io

class Splitter():
    filenamelist = []
    outdir = ''
    def FindPageNumber(self, pageObj):
      text = pageObj.extract_text()
      lines = text.splitlines()
      for line in lines:
        pattern = r"Page\s+(\d+)"
        match = re.search(pattern, line)
        if match:
            page_number = int(match.group(1))
            return(page_number)
      return 1
      
    def FindName(self, pageObj):
      text = pageObj.extract_text()
      lines = text.splitlines()
      for line in lines:
        if line.startswith("Student: "):
          line = line.replace("Student: ", "")
          line = line.replace(", ", "-")
          line = line.replace(" ", "_")
          return line
    def FindDate(self, pageObj):
      text = pageObj.extract_text()
      lines = text.splitlines()
      for line in lines:
        for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October','November','December']:
          x = line.find(month)
          if x!=-1:
            line = line[x:]
            line = line.replace(", ", "_")
            line = line.replace(" ", "_")
            return line
    
    def WriteReport(self, filename, writer):
      with zipfile.ZipFile(self.outdir, 'a') as zf:
        pdf_buffer = io.BytesIO()
        writer.write(pdf_buffer)
        zf.writestr(filename, pdf_buffer.getvalue())
    
    def SplitReport(self, pdfFileObj, outdir, alreadyOpened=False):
      # creating a pdf file object
      if not alreadyOpened:
        pdfFileObj = open(pdfFileObj, 'rb')
      if outdir=="":
        self.outdir = 'reports.zip'
      else:
        self.outdir = outdir + '.zip'

        
      # creating a pdf reader object
      pdfReader = PyPDF2.PdfReader(pdfFileObj)
       
      prevpageObj = pdfReader.pages[0]
      prevname = self.FindName(prevpageObj)
      prevdate = self.FindDate(prevpageObj)
      prevfilename = f"{prevname}-{prevdate}.pdf"
      pdfWriter = PyPDF2.PdfWriter()
      
      pdfWriter.add_page(prevpageObj)
      
      for i in range(1, len(pdfReader.pages)): 
        # creating a page object
        pageObj = pdfReader.pages[i]
        name = self.FindName(pageObj)
        date = self.FindDate(pageObj)
        filename = f"{name}-{date}.pdf"
        if self.FindPageNumber(pageObj)==1:
          self.WriteReport(prevfilename, pdfWriter)
          self.filenamelist.append(prevfilename)
          pdfWriter = PyPDF2.PdfWriter()
          pdfWriter.add_page(pageObj)
          prevfilename = filename
          if i==len(pdfReader.pages)-1:
            self.WriteReport(prevfilename, pdfWriter)
            self.filenamelist.append(prevfilename)
            pdfWriter = PyPDF2.PdfWriter()
            prevfilename = filename
        elif i==len(pdfReader.pages)-1:
          pdfWriter.add_page(pageObj)
          self.WriteReport(prevfilename, pdfWriter)
          self.filenamelist.append(prevfilename)
          prevfilename = filename
        else:
          pdfWriter.add_page(pageObj)
      
      # closing the pdf file object
      pdfFileObj.close()
      
    #SplitReport('report883.pdf', 'doublepagereports/')
    #print(filenamelist)
