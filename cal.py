import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        m1 = float(entry1.get())
        m2 = float(entry2.get())
        m3 = float(entry3.get())

        total = m1 + m2 + m3
        average = total / 3

        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "Fail"

        lbl_total.config(text=f"Total Marks: {total}")
        lbl_avg.config(text=f"Average Marks: {average:.2f}")
        lbl_grade.config(text=f"Grade: {grade}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("350x300")

# Labels and Entries
tk.Label(root, text="Subject 1 Marks").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Subject 2 Marks").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Subject 3 Marks").pack()
entry3 = tk.Entry(root)
entry3.pack()

# Button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result Labels
lbl_total = tk.Label(root, text="Total Marks:")
lbl_total.pack()

lbl_avg = tk.Label(root, text="Average Marks:")
lbl_avg.pack()

lbl_grade = tk.Label(root, text="Grade:")
lbl_grade.pack()

# Run the application
root.mainloop()