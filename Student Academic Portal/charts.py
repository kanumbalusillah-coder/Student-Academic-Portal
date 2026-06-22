python - "import matplotlib; print(matplotlib.__version__"
import sqlite3
import matplotlib.pyplot as plt

plt.plot([1,2,3,], [4,5,6])
plt.show()
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
SELECT status,count(*)
FROM students
GROUP BY status
""")

data = cursor.fetchall()

status = [x[0] for x in data]
counts = [x[1] for x in data]

plt.bar(status,counts)
plt.title("Students By Status")
plt.show()

plt.pie(counts,labels=status,autopct='%1.1f%%')
plt.title("Status Distribution")
plt.show()

months = ["Jan","Feb","Mar","Apr","May"]

students = [20,35,45,50,70]

plt.plot(months,students)
plt.title("Student Registration Trend")
plt.show()