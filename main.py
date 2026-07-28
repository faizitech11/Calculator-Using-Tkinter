import tkinter as tk
import math



def press(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        expression = entry.get().replace("×", "*").replace("÷", "/")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, value ** 2)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sqrt():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, math.sqrt(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def percent():
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, value / 100)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")




root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("420x620")
root.configure(bg="#1E1E1E")
root.resizable(False, False)


entry = tk.Entry(
    root,
    font=("Arial", 24),
    bd=8,
    relief="ridge",
    justify="right",
    bg="white"
)
entry.pack(fill="both", padx=10, pady=15, ipady=20)


def make_button(frame, text, command, color="#333333"):
    tk.Button(
        frame,
        text=text,
        font=("Arial", 18, "bold"),
        bg=color,
        fg="white",
        width=5,
        height=2,
        activebackground="#555555",
        command=command
    ).pack(side="left", padx=4, pady=4)




buttons = [
    ["C", "⌫", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=",],
    ["(", ")", "√", "x²"]
]

for row in buttons:
    frame = tk.Frame(root, bg="#1E1E1E")
    frame.pack()

    for btn in row:

        if btn == "C":
            make_button(frame, btn, clear, "#D32F2F")

        elif btn == "⌫":
            make_button(frame, btn, backspace, "#FF9800")

        elif btn == "=":
            make_button(frame, btn, calculate, "#388E3C")

        elif btn == "√":
            make_button(frame, btn, sqrt, "#6A1B9A")

        elif btn == "x²":
            make_button(frame, btn, square, "#6A1B9A")

        elif btn == "%":
            make_button(frame, btn, percent, "#1976D2")

        else:
            make_button(frame, btn, lambda b=btn: press(b))

root.mainloop()