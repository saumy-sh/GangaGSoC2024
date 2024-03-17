#!usr/bin/python3
import os
import sys
from pypdf import PdfReader, PdfWriter

def pdf_parser(pdffile,output_folder):
#it makes sure that if output_folder doesn't exist, then one is created
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print("created")
    else:
        print(f"{output_folder} found")
    try:
        reader = PdfReader(pdffile,strict= False)
        for page_num in range(0,len(reader.pages)):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
            pdf_file = os.path.join(output_folder,f"page_{page_num + 1}.pdf")
            with open(pdf_file,"wb") as pdf:
                writer.write(pdf)
                print("done")
    except Exception as e:
        print(e)
#here I have given my systems absolute path to folder
output_folder = "/home/saumysharan/GSoC/GangaGSoC2024/pdf_pages"   #name with the absolute path of the output folder where pdf of each page would be stored.
pdffile = sys.argv[1] #it will take input pdf which is to be separated. This can be given as file argument to ganga Executable file
print(pdffile)


pdf_parser(pdffile,output_folder)
