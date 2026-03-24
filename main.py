from tkinter import *
from tkinter.filedialog import askopenfilename
import pyttsx3
from pdf_reader import read_pdf
from word_reader import read_word

def convert():
    file = askopenfilename()

    if file.endswith(".pdf"):
        text = read_pdf(file)

    elif file.endswith(".docx"):
        text = read_word(file)

    else:
        from tkinter import messagebox 
        messagebox.showerror("error","unsupported file format")
        return
    engine = pyttsx3.init()
    engine.say(text)
    engine.save_to_file(text,"output.mp3")
    engine.runAndWait()


# GUI
root = Tk()
root.title("Audio Converter")

btn = Button(root, text="Select File & Convert", command=convert)
btn.pack(pady=20)

root.mainloop()
