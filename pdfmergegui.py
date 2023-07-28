import PyPDF2
import tkinter as tk
from tkinter import filedialog

def merge_pdfs():
    pdffiles = filedialog.askopenfilenames(title="Select PDF Files", filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
    merger = PyPDF2.PdfMerger()
    for filename in pdffiles:
        pdfFile = open(filename, 'rb')
        pdfReader = PyPDF2.PdfReader(pdfFile)
        merger.append(pdfReader)
        pdfFile.close()
    merger.write('merged.pdf')
    merger.close()
# Add a label to display status
    status_label.config(text="PDF files merged successfully!")

# Create GUI
root = tk.Tk()
root.title("PDF Merger")
root.geometry("600x400")

# Add a button to select and merge PDF files
merge_button = tk.Button(root, text="Select and Merge PDFs", command=merge_pdfs)
merge_button.pack(pady=20)

#status_label = tk.Label(root, text="")
#status_label.pack(pady=10)

# Run the GUI
root.mainloop()
