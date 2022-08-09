# Code Available at - https://github.com/Valetrix/Wiki
# Coded By Valetrix - Credits: John Elder, Codemy & other Contributors
# This Is my Version of the wiki searchup App.
# ----------------------------------------------------------------------------------
import wikipedia as wiki
from tkinter import *
from customtkinter import *
import textwrap

# Create App
root = Tk()
root.geometry('700x650')
root.title('InfoTarn-VPL')
root.iconbitmap('Info-Tarn-Logo.ico')

# Functions
def search(x):
	out_text.delete('1.0', END)
	results = wiki.summary(x)
	# my_wrap = textwrap.TextWrapper(width = 50)
	# wrap_list = my_wrap.wrap(text=results)
	# y = ''
	# for line in wrap_list:
	# 	y = y + f'{line}\n'
	out_text.insert('0.0', results)

def clear():
	# Clearing Input Entry (e1)
	e1.delete(0, END)

	# Clearing Output Text (out_text)
	out_text.delete('1.0', END)

#Creating Frame for Input
lf1 = LabelFrame(root, text='Search Wikipedia')
lf1.pack(pady=5)

# Adding Entry (e1) as Input to LF1
e1 = Entry(lf1, font=('Agency FB', 20), width=47)
e1.pack(pady=20, padx=20)

# Creating Frame for Output
lf2 = LabelFrame(root)
lf2.pack(pady=5)

# Creating Scrollbar (out_scroll) for Output Text (out_text) & adding to LF2
out_scroll = Scrollbar(lf2)
out_scroll.pack(side=RIGHT, fill=Y)

# Adding Text (out_text) as Output to LF2
out_text = Text(lf2, font=('Agency FB', 18), yscrollcommand=out_scroll.set, wrap=WORD, width=55, height=15)
out_text.pack()

# Configure The ScrollBar (out_scroll)
out_scroll.configure(command=out_text.yview)

# Creating Frame for Input Buttons
lf3 = LabelFrame(root)
lf3.pack(pady=5)

# Adding Button (b1) For Searching Wiki to LF3
b1 = Button(lf3, text='Search', command=lambda: search(e1.get()), font=('Agency FB',20))
b1.grid(row=0, column=0, padx=10, pady=10)

# Adding Button (b1) For Searching Wiki to LF3
b2 = Button(lf3, text='Clear', command=clear, font=('Agency FB', 20))
b2.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
