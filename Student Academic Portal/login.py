import tkinter as tk
from tkinter import messagebox

def login():

    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Success","Login Successful")
        root.destroy()

        import dashboard

    else:
        messagebox.showerror("Error","Invalid Login")

root = tk.Tk()
root.title("Student Academic Portal")

tk.Label(root,text="Username").pack(pady=5)
user_entry = tk.Entry(root)
user_entry.pack()

tk.Label(root,text="Password").pack(pady=5)
pass_entry = tk.Entry(root,show="*")
pass_entry.pack()

tk.Button(root,text="Login",command=login).pack(pady=10)

root.mainloop()