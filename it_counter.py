#!usr/bin/python3
import sys
from pypdf import PdfReader

word_to_be_counted = "it"

pdffile = sys.argv[1] #takes input of file from which no of times repetition of word is counted
def word_counter(pdffile):
    reader = PdfReader(pdffile)
    it_count = 0
    page = reader.pages[0].extract_text(extraction_mode="layout")
    words = page.split(" ")
    for word in words:
        if word.lower().lstrip(".").rstrip(".") == word_to_be_counted:
            it_count += 1
    return (it_count)

print(word_counter(pdffile))