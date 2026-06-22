import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import matplotlib.pyplot as plt

# ==========================
# DATABASE SETUP
# ==========================

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
            datetime.now().strftime("%Y-%m-%d")
        ))

conn.commit()
conn.close()

# ==========================
# CHARTS
# ==========================

def show_bar_chart():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT status, COUNT(*)
    FROM students
    GROUP BY status
    """)

    data = cursor.fetchall()

    status = [row[0] for row in data]
    count = [row[1] for row in data]

    plt.bar(status,count)
    plt.title("Students By Status")
    plt.show()

    conn.close()


def show_pie_chart():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT gender, COUNT(*)
    FROM students
    GROUP BY gender
    """)

    data = cursor.fetchall()

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Gender Distribution")
    plt.show()

    conn.close()


def show_line_chart():

    months = ["Jan","Feb","Mar","Apr","May","Jun"]
    students = [10,15,20,25,30,35]

    plt.plot(months,students,marker="o")
    plt.title("Student Registration Trend")
    plt.show()

# ==========================
# DASHBOARD
# ==========================

def open_dashboard():

    dashboard = tk.Tk()
    dashboard.title("Student Academic Portal Dashboard")
    dashboard.geometry("1000x600")

    tk.Label(
        dashboard,
        text="Student Academic Portal Dashboard",
        font=("Arial",16,"bold")
    ).pack(pady=10)

    search_entry = tk.Entry(dashboard,width=30)
    search_entry.pack()

    tree = ttk.Treeview(
        dashboard,
        columns=(
            "ID",
            "Name",
            "Gender",
            "Status",
            "Contact",
            "Date"
        ),
        show="headings"
    )

    for col in (
        "ID",
        "Name",
        "Gender",
        "Status",
        "Contact",
        "Date"
    ):
        tree.heading(col,text=col)

    tree.pack(fill="both",expand=True)

    def load_students():

        tree.delete(*tree.get_children())

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")

        rows = cursor.fetchall()

        for row in rows:
            tree.insert("",tk.END,values=row)

        conn.close()

    def search_student():

        keyword = search_entry.get()

        tree.delete(*tree.get_children())

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM students
        WHERE fullname LIKE ?
        """,('%'+keyword+'%',))

        rows = cursor.fetchall()

        for row in rows:
            tree.insert("",tk.END,values=row)

        conn.close()

    tk.Button(
        dashboard,
        text="Search",
        command=search_student
    ).pack(pady=5)

    tk.Button(
        dashboard,
        text="Bar Chart",
        command=show_bar_chart
    ).pack(pady=2)

    tk.Button(
        dashboard,
        text="Pie Chart",
        command=show_pie_chart
    ).pack(pady=2)

    tk.Button(
        dashboard,
        text="Line Graph",
        command=show_line_chart
    ).pack(pady=2)

    load_students()

    dashboard.mainloop()

# ==========================
# LOGIN
# ==========================

def login():

    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":

        root.destroy()

        open_dashboard()

    else:
        messagebox.showerror(
            "Error",
            "Invalid Username or Password"
        )

root = tk.Tk()
root.title("Student Academic Portal")
root.geometry("350x250")

tk.Label(
    root,
    text="Student Academic Portal",
    font=("Arial",16,"bold")
).pack(pady=20)

tk.Label(root,text="Username").pack()

username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root,text="Password").pack()

password_entry = tk.Entry(root,show="*")
password_entry.pack()

tk.Button(
    root,
    text="Login",
    command=login
).pack(pady=15)

root.mainloop()