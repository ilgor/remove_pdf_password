import pikepdf
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import simpledialog


def validate_password(password, file_path):
    while password:
        try:
            return pikepdf.open(file_path, password=password)
        except:
            password = ask_for_pdf_password(title="PDF password", prompt="Re-enter your PDF password: ")

def create_new_file_without_password(file_path):
    password = ask_for_pdf_password(title="PDF password", prompt="Enter your PDF password: ")
    pdf = validate_password(password, file_path)
    new_file_path = file_path.replace('.pdf', '_no_password.pdf')
    pdf.save(new_file_path)
    window.destroy()

def ask_for_pdf_password(title, prompt):
    return simpledialog.askstring(title=title, prompt=prompt)
    
def select_file():
    filetypes = (('PDF files', '*.pdf'),)

    file_path = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    
    create_new_file_without_password(file_path=file_path)

window = tk.Tk()
window.title('Choose File')
window.resizable(False, False)
window.geometry('300x150')

open_button = ttk.Button(window, text='Open PDF File', command=select_file)
open_button.pack(expand=True)

window.mainloop()