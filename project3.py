import tkinter as tk
from tkinter import messagebox
import string

def is_pangram(text):
    text = text.lower()
    letters_in_text = set(text)
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(letters_in_text)

def check_pangram():
    text = entry.get()
    result = is_pangram(text)

    if result:
        messagebox.showinfo("Result", "✅ It's a Pangram!")
    else:
        messagebox.showwarning("Result", "❌ Not a Pangram.")

root = tk.Tk()
root.title("Pangram Checker")
root.geometry("400x300")

label = tk.Label(root, text="Enter sentense below")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack()


click = tk.Button(root, text="Click", command=check_pangram)
click.pack(pady=10)

root.mainloop()
