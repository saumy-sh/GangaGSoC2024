import unittest
from python_scripts.pdf import pdf_parser
from reportlab.pdfgen.canvas import Canvas
import os
 

class Testpdf(unittest.TestCase):
    def test_pdf_created(self):
        test_pdf_path = "test_pdf.pdf"
        tmp_folder_path = "test/tmp_output"
        canvas = Canvas(test_pdf_path)
        page1_text = "Ganga is in itself a great way to manage files in it. It is really useful."
        page2_text = "It is good to have such tools!"
        canvas.drawString(200,500,page1_text)
        canvas.showPage()
        canvas.drawString(200,500,page2_text)
        canvas.save()
        pdf_parser(test_pdf_path,tmp_folder_path)
        tmp_pdfs = os.listdir(tmp_folder_path)
        self.assertIsNotNone(tmp_pdfs)
        self.assertEqual(len(tmp_pdfs),2) 




