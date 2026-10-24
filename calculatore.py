import tkinter as tk

def calculate(sequence):
    list_sequence = list(sequence)
    
    if not sequence:
        return ""
    
    operators = "+-*/"
    has_operator = any(op in sequence for op in operators)
    

    if not has_operator:
        try:
           
            num = float(sequence)
            return str(int(num)) if num.is_integer() else str(sequence)
        except ValueError:
             return "Not a number"           

        
    if sequence[-1] in operators:
        return "Syntax Error"

    try:
        list_sequence = list(sequence)

        while "*" in list_sequence or "/" in list_sequence:
        
            if "*" in list_sequence:
                multi_position = list_sequence.index("*")
                multi_num1 = float(list_sequence[multi_position - 1])
                multi_num2 = float(list_sequence[multi_position + 1])
                multi_result = multi_num1 * multi_num2 
                list_sequence[multi_position - 1 : multi_position + 2] = [str(multi_result)]
            
            if "/" in list_sequence:
                def_position = list_sequence.index("/")
                def_num1 = float(list_sequence[def_position - 1])
                def_num2 = float(list_sequence[def_position + 1])
                
                if def_num2 ==0:
                    return "Error: Division by 0"
                
                else:
                    def_result = def_num1 / def_num2     
                    list_sequence[def_position- 1 : def_position + 2] = [str(def_result)]

        while "+" in list_sequence or "-" in list_sequence:
        
            if "+" in list_sequence:
                sub_position = list_sequence.index("+")
                sub_num1 = float(list_sequence[sub_position - 1])
                sub_num2 = float(list_sequence[sub_position + 1])
                sub_result = sub_num1 + sub_num2 
                list_sequence[sub_position - 1 : sub_position + 2] = [str(sub_result)]
            
            if "-" in list_sequence:
                min_position = list_sequence.index("-")
                min_num1 = float(list_sequence[min_position - 1])
                min_num2 = float(list_sequence[min_position + 1])
                min_result = min_num1 - min_num2  
                list_sequence[min_position - 1 : min_position + 2] = [str(min_result)]

        return "".join(list_sequence)
    
    except (IndexError, ValueError):
        return "Syntax Error"

    
def on_equal_press():
    current_text = display.get()       
    result = calculate(current_text)   
    display.delete(0, tk.END)          
    display.insert(0, result)

def press_key(value):  
    display.insert(tk.END, value)

def clear_display():
    display.delete(0, tk.END)

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("My calculator!")
root.geometry("450x400")

label = tk.Label(root, text = "Welcome to my calculator!", font = ("Arial", 12))
label.pack()

display = tk.Entry(root, font= ("Arial", 20))
display. pack(fill="x", padx=10, pady=10, ipady=10)

button_frame = tk.Frame(root)
button_frame.pack()

btn_0 = tk.Button(button_frame, text = "0", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("0") )
btn_0.grid(row=0, column=0, padx=5, pady=5)

btn_1 = tk.Button(button_frame, text = "1", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("1") )
btn_1.grid(row=0, column=1, padx=5, pady=5)

btn_2 = tk.Button(button_frame, text = "2", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("2") )
btn_2.grid(row=0, column=2, padx=5, pady=5)

btn_3 = tk.Button(button_frame, text = "3", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("3") )
btn_3.grid(row=0, column=3, padx=5, pady=5)

btn_eq = tk.Button(button_frame, text = "=", font = ("Arial", 14), width=5, height=2, command=on_equal_press )
btn_eq.grid(row=0, column=4, padx=5, pady=5)


btn_4 = tk.Button(button_frame, text = "4", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("4") )
btn_4.grid(row=1, column=0, padx=5, pady=5)

btn_5 = tk.Button(button_frame, text = "5", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("5") )
btn_5.grid(row=1, column=1, padx=5, pady=5)

btn_6 = tk.Button(button_frame, text = "6", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("6") )
btn_6.grid(row=1, column=2, padx=5, pady=5)

btn_pl = tk.Button(button_frame, text = "+", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("+") )
btn_pl.grid(row=1, column=3, padx=5, pady=5)

btn_mul = tk.Button(button_frame, text = "*", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("*") )
btn_mul.grid(row=1, column=4, padx=5, pady=5)


btn_7 = tk.Button(button_frame, text = "7", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("7") )
btn_7.grid(row=2, column=0, padx=5, pady=5)

btn_8 = tk.Button(button_frame, text = "8", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("8") )
btn_8.grid(row=2, column=1, padx=5, pady=5)

btn_9 = tk.Button(button_frame, text = "9", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("9") )
btn_9.grid(row=2, column=2, padx=5, pady=5)

btn_min = tk.Button(button_frame, text = "-", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("-") )
btn_min.grid(row=2, column=3, padx=5, pady=5)

btn_div = tk.Button(button_frame, text = "/", font = ("Arial", 14), width=5, height=2, command=lambda: press_key("/") )
btn_div.grid(row=2, column=4, padx=5, pady=5)


btn_clear = tk.Button(button_frame, text = "clear", font = ("Arial", 14), width=13, height=2, command= clear_display )
btn_clear.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

btn_exit = tk.Button(button_frame, text = "exit", font = ("Arial", 14), width=13, height=2, command= exit_app )
btn_exit.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
