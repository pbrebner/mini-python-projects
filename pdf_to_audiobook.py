# Python script that takes a pdf input and converts the text to speech
# Uses the pyttsx3-2.71 and PyPDF2

import pyttsx3, PyPDF2

# Test Text to voice conversion
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

# pdf_reader = PyPDF2.PdfFileReader(open("file.pdf", "rb"))
