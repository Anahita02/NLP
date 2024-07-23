# PyPDF2 library to read in text data from a PDF file
import PyPDF2

#read a PDF. rb -> readind in a binary method we use it cause we have a pdf file not the a tex file
myfile  = open('US_Declaration.pdf', mode='rb')
pdf_reader = PyPDF2.PdfReader(myfile)
len(pdf_reader.pages)
page_one = pdf_reader.pages[0]
print(page_one.extract_text())
mytext = page_one.extract_text()
myfile.close()

# add a page to a pdf
f = open('US_Declaration.pdf', mode='rb')
pdf_reader = PyPDF2.PdfReader(f)
first_pge = pdf_reader.pages[0]
pdf_writer = PyPDF2.PdfWriter() #add pages
pdf_writer.add_page(first_pge)
pdf_output = open('MY_BRAND_NEW.pdf','wb')
pdf_writer.write(pdf_output)
pdf_output.close()
f.close()
brand_new = open('MY_BRAND_NEW.pdf','rb')

pdf_reader = PyPDF2.PdfReader(brand_new)
len(pdf_reader.pages)

f = open('US_Declaration.pdf','rb')

# list all the text
pdf_text = []

pdf_reader = PyPDF2.PdfReader(f)

for p in range(len(pdf_reader.pages)):
    
    page = pdf_reader.pages[p]
    
    pdf_text.append(page.extract_text())
    
f.close()

pdf_text

len(pdf_text)

for page in pdf_text:
    print(page)
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('\n')