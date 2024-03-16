#!usr/bin/python3
import os
import sys
from pypdf import PdfReader, PdfWriter

def pdf_parser(pdffile,output_folder):
    try:
        reader = PdfReader(pdffile)
        print(reader.metadata)
        for page_num in range(0,len(reader.pages)):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
            pdf_file = os.path.join(output_folder,f"page_{page_num + 1}.pdf")
            with open(pdf_file,"wb") as pdf:
                writer.write(pdf)
                print("done")
    except Exception as e:
        print(e)
output_folder = "pdf_pages"   #name of the output folder where pdf of each page would be stored
pdffile = sys.argv[1] #it will take input pdf which is to be separated. This can be given as file argument to ganga Executable file
print(pdffile)
#it makes sure that if output_folder doesn't exist, then one is created
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print("created")
else:
    print(f"{output_folder} found")

pdf_parser(pdffile,output_folder)
