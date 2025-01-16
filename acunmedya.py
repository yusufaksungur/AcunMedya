import tkinter as tk 

window = tk.Tk()  
window.title("Cal")  
window.minsize(width=450, height=300) 

entry_var_a = tk.IntVar()
entry_var_b = tk.IntVar()

def addition():
    input_number_a = entry_var_a.get()
    input_number_b = entry_var_b.get()
    Result = input_number_a + input_number_b
    result_label.config(text=f"Result: {Result}")
    
def subtraction():
    input_number_a = entry_var_a.get()
    input_number_b = entry_var_b.get()
    Result = input_number_a - input_number_b
    result_label.config(text=f"Result: {Result}")
    
def division():
    input_number_a = entry_var_a.get()
    input_number_b = entry_var_b.get()
    if input_number_b == 0:
       result_label.config(text="Error: Cannot divide by zero!")
       return
   
    Result = input_number_a / input_number_b
    result_label.config(text=f"Result: {Result}")
    
def multiplication():
    input_number_a = entry_var_a.get()
    input_number_b = entry_var_b.get()
    Result = input_number_a * input_number_b
    result_label.config(text=f"Result: {Result}")
    
    
entry_a = tk.Entry(window, textvariable=entry_var_a)
entry_b = tk.Entry(window, textvariable=entry_var_b)

addition_button = tk.Button(window, text="Addition", command=addition)
subtraction_button = tk.Button(window, text="Subtraction", command=subtraction)
division_button = tk.Button(window, text="Division", command=division)
multiplication_button = tk.Button(window, text="Multiplication", command=multiplication)

result_label = tk.Label(window, text="Result: ")

entry_a.pack()
entry_b.pack()
addition_button.pack()
subtraction_button.pack()
division_button.pack()
multiplication_button.pack()
result_label.pack()

window.mainloop()
