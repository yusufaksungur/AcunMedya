import tkinter as tk 

window = tk.Tk()  
window.title("Calculator")  
window.minsize(width=450, height=300) 

entry_var_a = tk.IntVar()
entry_var_b = tk.IntVar()

def addition():
    input_number_a = entry_var_a.get()
    input_number_b = entry_var_b.get()
    Result = input_number_a + input_number_b
    result_label.config(text=f"Result: {Result:.2f}", fg="black")
    
def subtraction():
    input_number_a = entry_var_a.get()
    input_number_b = entry_var_b.get()
    Result = input_number_a - input_number_b
    result_label.config(text=f"Result: {Result:.2f}", fg="black")
    
def division():
    input_number_a = entry_var_a.get()
    input_number_b = entry_var_b.get()
    if input_number_b == 0:
       result_label.config(text="Error: Cannot divide by zero!", fg="red")
       return
    Result = input_number_a / input_number_b
    result_label.config(text=f"Result: {Result:.2f}", fg="black")
    
def multiplication():
    input_number_a = entry_var_a.get()
    input_number_b = entry_var_b.get()
    Result = input_number_a * input_number_b
    result_label.config(text=f"Result: {Result:.2f}", fg="black")

def clear():
    entry_var_a.set(0)
    entry_var_b.set(0)
    result_label.config(text="Result: ", fg="black")

entry_a = tk.Entry(window, textvariable=entry_var_a)
entry_b = tk.Entry(window, textvariable=entry_var_b)

addition_button = tk.Button(window, text="Addition", command=addition)
subtraction_button = tk.Button(window, text="Subtraction", command=subtraction)
division_button = tk.Button(window, text="Division", command=division)
multiplication_button = tk.Button(window, text="Multiplication", command=multiplication)
clear_button = tk.Button(window, text="Clear", command=clear)

result_label = tk.Label(window, text="Result: ", font=("Arial", 12))

entry_a.grid(row=0, column=0, padx=10, pady=10)
entry_b.grid(row=1, column=0, padx=10, pady=10)

addition_button.grid(row=0, column=1, padx=10, pady=10)
subtraction_button.grid(row=1, column=1, padx=10, pady=10)
multiplication_button.grid(row=2, column=1, padx=10, pady=10)
division_button.grid(row=3, column=1, padx=10, pady=10)

clear_button.grid(row=2, column=0, padx=10, pady=10)

result_label.grid(row=4, column=0, columnspan=2, pady=20)

window.mainloop()
