import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime

# DATABASE
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    gender TEXT,
    status TEXT,
    contact TEXT,
    created_date TEXT
)
""")

cursor.execute("SELECT COUNT(*) FROM students")
count = cursor.fetchone()[0]

if count == 0:

    students = [
        ("Fatmata Sesay","Female","Active","076111111"),
        ("Ibrahim Koroma","Male","Active","076222222"),
        ("Aisha Conteh","Female","Inactive","076333333"),
        ("Mohamed Turay","Male","Pending","076444444"),
        ("John Kamara","Male","Active","076555555"),
        ("Mary Bangura","Female","Active","076666666"),
        ("Ahmed Sesay","Male","Inactive","076777777"),
        ("Grace Koroma","Female","Pending","076888888"),
        ("Ibrahim Sillah","Male","Active","076999999"),
        ("Hawa Conteh","Female","Active","076123456"),
        ("Musa Kamara","Male","Active","076123457"),
        ("Jeneba Kanu","Female","Inactive","076123458"),
        ("Abdul Bangura","Male","Pending","076123459"),
        ("Mariama Sesay","Female","Active","076123460"),
        ("Joseph Turay","Male","Active","076123461"),
        ("Kadiatu Koroma","Female","Inactive","076123462"),
        ("Alusine Kamara","Male","Active","076123463"),
        ("Zainab Conteh","Female","Pending","076123464"),
        ("Sorie Bangura","Male","Active","076123465"),
        ("Adama Kanu","Female","Active","076123466")
    ]

    today = datetime.now().strftime("%Y-%m-%d")

    for student in students:
        cursor.execute("""
        INSERT INTO students
        (fullname,gender,status,contact,created_date)
        VALUES (?,?,?,?,?)
        """, (
            student[0],
            student[1],
            student[2],
            student[3],
            today
        ))

    conn.commit()

conn.close()

# GUI
root = tk.Tk()
root.title("Student Academic Portal Dashboard")
root.geometry("1000x600")

tk.Label(
    root,
    text="Student Academic Portal Dashboard",
    font=("Arial",16,"bold")
).pack(pady=10)

tree = ttk.Treeview(
    root,
    columns=("ID","Name","Gender","Status","Contact","Date"),
    show="headings"
)

tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Gender", text="Gender")
tree.heading("Status", text="Status")
tree.heading("Contact", text="Contact")
tree.heading("Date", text="Date")

tree.pack(fill="both", expand=True)

# LOAD RECORDS
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

for record in records:
    tree.insert("", "end", values=record)

conn.close()

root.mainloop()