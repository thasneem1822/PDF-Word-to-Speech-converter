import pyttsx3
import PyPDF2
from tkinter.filedialog import *

ax = askopenfilename()
pdfreader = PyPDF2.PdfReader(ax)
pages = len(pdfreader.pages)

for num in range(0,pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()