# Python script that takes a pdf input and converts the text to speech
# Uses the pyttsx3 and PyPDF2

import pyttsx3, PyPDF2

pdf_reader = PyPDF2.PdfFileReader(open("file.pdf", "rb"))
