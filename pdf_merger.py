import PyPDF3
pdf_file = ['1.pdf', '2.pdf', '3.pdf']
merger = PyPDF3.PdfFileMerger()
for file in pdf_file:
    pdfFile = open(file, 'rb')
    readFile = PyPDF3.PdfFileReader(pdfFile)
    merger.append(readFile)
pdfFile.close()
merger.write("mergedfile.pdf")
