import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error")

# Create main window
root = tk.Tk()
root.title("Martins Calculator")
root.geometry("300x200")
root.eval('tk::PlaceWindow . center')  # Center the window (works on some OS)

# Create a frame in the center
frame = tk.Frame(root)
frame.pack(expand=True)

# Entry box for user input
entry = tk.Entry(frame, width=20, font=("Arial", 14))
entry.pack(pady=20)

# Button to calculate
calc_button = tk.Button(frame, text="Calculate", command=calculate)
calc_button.pack()

# Label to show result
result_label = tk.Label(frame, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
