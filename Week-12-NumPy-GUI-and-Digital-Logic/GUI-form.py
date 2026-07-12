import tkinter as tk

# Create window
root = tk.Tk()
root.title("Window Wizard")
root.geometry("350x200")

# Labels
label1 = tk.Label(root, text="Name:")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(root, text="Age:")
label2.grid(row=1, column=0, padx=10, pady=10)

# Text Fields
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Functions
def submit():
    name = entry1.get()
    age = entry2.get()
    print("Name:", name)
    print("Age:", age)

def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

# Buttons
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.grid(row=2, column=0, pady=20)

reset_btn = tk.Button(root, text="Reset", command=reset)
reset_btn.grid(row=2, column=1)

# Run window
root.mainloop()
