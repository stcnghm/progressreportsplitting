# -*- coding: utf-8 -*-
import PyPDF2
import re
import tempfile

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
        newFile = open(filename, 'wb')
        writer.write(newFile)
        newFile.close()
    
    def SplitReport(self, pdfFileObj, alreadyOpened=False):
      # creating a pdf file object
      if not alreadyOpened:
        pdfFileObj = open(pdfFileObj, 'rb')
        self.outdir = tempfile.TemporaryDirectory().name

        
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
          newPrevFileName = self.outdir+prevfilename
          self.WriteReport(newPrevFileName, pdfWriter)
          self.filenamelist.append(newPrevFileName)
          pdfWriter = PyPDF2.PdfWriter()
          pdfWriter.add_page(pageObj)
          prevfilename = filename
          if i==len(pdfReader.pages)-1:
            newPrevFileName = self.outdir+prevfilename
            self.WriteReport(newPrevFileName, pdfWriter)
            self.filenamelist.append(newPrevFileName)
            pdfWriter = PyPDF2.PdfWriter()
            prevfilename = filename
        elif i==len(pdfReader.pages)-1:
          pdfWriter.add_page(pageObj)
          newPrevFileName = self.outdir+prevfilename
          self.WriteReport(newPrevFileName, pdfWriter)
          self.filenamelist.append(newPrevFileName)
          prevfilename = filename
        else:
          pdfWriter.add_page(pageObj)
      
      # closing the pdf file object
      pdfFileObj.close()
      
    #SplitReport('report883.pdf', 'doublepagereports/')
    #print(filenamelist)
