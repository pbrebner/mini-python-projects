# Python script that takes a pdf input and converts the text to speech
# Uses the pyttsx3-2.71 and PyPDF2

import pyttsx3, PyPDF2

# Test Text to voice conversion
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

# pdf = input("Audiobook File?\n")

# Really Struggles to read the file correctly
pdf_reader = PyPDF2.PdfFileReader(open("audiobook.pdf", "rb"), strict=False)
engine = pyttsx3.init()
for page in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page)
    text = page.extractText()
    print(text)
    engine.say(text)
    engine.runAndWait()
engine.stop()