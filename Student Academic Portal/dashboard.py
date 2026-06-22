import tkinter as tk
from tkinter import ttk
import sqlite3

root = tk.Tk()
root.title("Student Academic Portal Dashboard")
root.geometry("1000x600")
root.configure(bg="lightblue")

tk.Label(
    root,
    text="Student Academic Portal Dashboard",
    font=("Arial",16,"bold"),
    bg="lightblue"
).pack(pady=10)

tree = ttk.Treeview(
    root,
    columns=("ID","Name","Gender","Status","Contact","Date"),
    show="headings"
)

for col in ("ID","Name","Gender","Status","Contact","Date"):
    tree.heading(col, text=col)

tree.pack(fill="both", expand=True)

def load_data():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    tree.delete(*tree.get_children())

    for row in rows:
        tree.insert("", "end", values=row)

    conn.close()

load_data()

root.mainloop()