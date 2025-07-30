#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk

def click1():
    entry.insert(tk.END, "1")

def click2():
    entry.insert(tk.END, "2")

def click3():
    entry.insert(tk.END, "3")

def click4():
    entry.insert(tk.END, "4")

def click5():
    entry.insert(tk.END, "5")

def click6():
    entry.insert(tk.END, "6")

def click7():
    entry.insert(tk.END, "7")

def click8():
    entry.insert(tk.END, "8")

def click9():
    entry.insert(tk.END, "9")

def click0():
    entry.insert(tk.END, "0")

def click_add():
    entry.insert(tk.END, "+")

def click_sub():
    entry.insert(tk.END, "-")

def click_mul():
    entry.insert(tk.END, "*")

def click_div():
    entry.insert(tk.END, "/")

def click_dot():
    entry.insert(tk.END, ".")

def clear():
    entry.delete(0, tk.END)

def equal():
    expression = entry.get()
    if expression:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))

root = tk.Tk()
root.title("Calculator")

root.config(bg="black")


entry = tk.Entry(root, bg="gray", fg="white", font=("Arial", 18), bd=5, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

button_bg = "dark gray"
button_fg = "white"
button_font = ("Arial", 14)

button1 = tk.Button(root, text="1", bg=button_bg, fg=button_fg, font=button_font, command=click1)
button1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

button2 = tk.Button(root, text="2", bg=button_bg, fg=button_fg, font=button_font, command=click2)
button2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

button3 = tk.Button(root, text="3", bg=button_bg, fg=button_fg, font=button_font, command=click3)
button3.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

button_add = tk.Button(root, text="+", bg=button_bg, fg=button_fg, font=button_font, command=click_add)
button_add.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")


button4 = tk.Button(root, text="4", bg=button_bg, fg=button_fg, font=button_font, command=click4)
button4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

button5 = tk.Button(root, text="5", bg=button_bg, fg=button_fg, font=button_font, command=click5)
button5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

button6 = tk.Button(root, text="6", bg=button_bg, fg=button_fg, font=button_font, command=click6)
button6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

button_sub = tk.Button(root, text="-", bg=button_bg, fg=button_fg, font=button_font, command=click_sub)
button_sub.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")


button7 = tk.Button(root, text="7", bg=button_bg, fg=button_fg, font=button_font, command=click7)
button7.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")

button8 = tk.Button(root, text="8", bg=button_bg, fg=button_fg, font=button_font, command=click8)
button8.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

button9 = tk.Button(root, text="9", bg=button_bg, fg=button_fg, font=button_font, command=click9)
button9.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")

button_mul = tk.Button(root, text="*", bg=button_bg, fg=button_fg, font=button_font, command=click_mul)
button_mul.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")


button0 = tk.Button(root, text="0", bg=button_bg, fg=button_fg, font=button_font, command=click0)
button0.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

button_dot = tk.Button(root, text=".", bg=button_bg, fg=button_fg, font=button_font, command=click_dot)
button_dot.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")

button_clear = tk.Button(root, text="C", bg=button_bg, fg=button_fg, font=button_font, command=clear)
button_clear.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

button_div = tk.Button(root, text="/", bg=button_bg, fg=button_fg, font=button_font, command=click_div)
button_div.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")


button_equal = tk.Button(root, text="=", bg=button_bg, fg=button_fg, font=button_font, command=equal)
button_equal.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")


for i in range(4):
    root.grid_columnconfigure(i, weight=1)


for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()



# In[ ]:




