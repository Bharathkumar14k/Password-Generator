import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    try:
        length_password = int(length_entry.get())
        if length_password <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a positive integer for the password length.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length_password))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Password Copied", "Password has been copied to clipboard.")
    else:
        messagebox.showwarning("No Password", "No Password Generated")

root = tk.Tk()
root.geometry("300x300")
root.title("Password Generator")
root.config(bg="beige")

Title = tk.Label(root, text="Password Generator", bg="beige", fg="black", font=("futura", 15, "bold"))
Title.pack(anchor="center", pady="20px")


length_label = tk.Label(root, text="Select the Length of Your Password")
length_label.pack()

length_entry = tk.Entry(root, width=30)
length_entry.pack()


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password:")
password_label.pack()

password_entry = tk.Entry(root, width=30)
password_entry.pack()

copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack(pady=10)

root.mainloop()
