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
entry.pack(padx=10, pady=10, fill=tk.BOTH)


button_bg = "dark gray"
button_fg = "white"
button_font = ("Arial", 14)

button1 = tk.Button(root, text="1", bg=button_bg, fg=button_fg, font=button_font, command=click1)
button1.pack(side=tk.LEFT, padx=5, pady=5)

button2 = tk.Button(root, text="2", bg=button_bg, fg=button_fg, font=button_font, command=click2)
button2.pack(side=tk.LEFT, padx=5, pady=5)

button3 = tk.Button(root, text="3", bg=button_bg, fg=button_fg, font=button_font, command=click3)
button3.pack(side=tk.LEFT, padx=5, pady=5)

button4 = tk.Button(root, text="4", bg=button_bg, fg=button_fg, font=button_font, command=click4)
button4.pack(side=tk.LEFT, padx=5, pady=5)

button5 = tk.Button(root, text="5", bg=button_bg, fg=button_fg, font=button_font, command=click5)
button5.pack(side=tk.LEFT, padx=5, pady=5)

button6 = tk.Button(root, text="6", bg=button_bg, fg=button_fg, font=button_font, command=click6)
button6.pack(side=tk.LEFT, padx=5, pady=5)

button7 = tk.Button(root, text="7", bg=button_bg, fg=button_fg, font=button_font, command=click7)
button7.pack(side=tk.LEFT, padx=5, pady=5)

button8 = tk.Button(root, text="8", bg=button_bg, fg=button_fg, font=button_font, command=click8)
button8.pack(side=tk.LEFT, padx=5, pady=5)

button9 = tk.Button(root, text="9", bg=button_bg, fg=button_fg, font=button_font, command=click9)
button9.pack(side=tk.LEFT, padx=5, pady=5)

button0 = tk.Button(root, text="0", bg=button_bg, fg=button_fg, font=button_font, command=click0)
button0.pack(side=tk.LEFT, padx=5, pady=5)

button_add = tk.Button(root, text="+", bg=button_bg, fg=button_fg, font=button_font, command=click_add)
button_add.pack(side=tk.LEFT, padx=5, pady=5)

button_sub = tk.Button(root, text="-", bg=button_bg, fg=button_fg, font=button_font, command=click_sub)
button_sub.pack(side=tk.LEFT, padx=5, pady=5)
button_mul = tk.Button(root, text="*", bg=button_bg, fg=button_fg, font=button_font, command=click_mul)
button_mul.pack(side=tk.LEFT, padx=5, pady=5)
button_div = tk.Button(root, text="/", bg=button_bg, fg=button_fg, font=button_font, command=click_div)
button_div.pack(side=tk.LEFT, padx=5, pady=5)
button_dot = tk.Button(root, text=".", bg=button_bg, fg=button_fg, font=button_font, command=click_dot)
button_dot.pack(side=tk.LEFT, padx=5, pady=5)
button_clear = tk.Button(root, text="C", bg=button_bg, fg=button_fg, font=button_font, command=clear)
button_clear.pack(side=tk.LEFT, padx=5, pady=5)
button_equal = tk.Button(root, text="=", bg=button_bg, fg=button_fg, font=button_font, command=equal)
button_equal.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()



# In[ ]:




