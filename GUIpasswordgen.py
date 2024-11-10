import tkinter as tk
from tkinter import messagebox
from passwordgen import generate_password, copy_to_clipboard

def GUI_generate_password():
    length = length_entry.get()
    if length.isdigit() and 0 < int(length) <= 100:
        password = generate_password(int(length))
        password_var.set(password)
    else:
        messagebox.showerror("Length Invalid", "Please enter a valid password length between 1 and 100")

def GUI_copy_to_clipboard():
    password = password_var.get()
    if password:
        copy_to_clipboard(password)
        messagebox.showinfo("Copied","Password copied to clipboard!")
    else:
        messagebox.showerror("Error","Error!, No password generated to copy!")

root = tk.Tk()
root.title("Password Generator")

# Create and pack widgets
length_label = tk.Label(root, text="Enter password length (1-100):")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=GUI_generate_password)
generate_button.pack(pady=10)

password_var = tk.StringVar()
password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=5)

password_display = tk.Entry(root, textvariable=password_var, state="readonly", width=30)
password_display.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=GUI_copy_to_clipboard)
copy_button.pack(pady=10)

# Run the application
root.mainloop()