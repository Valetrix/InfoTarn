# Code Available at - https://github.com/Valetrix/Wiki
# Coded By Valetrix - Credits: John Elder, Codemy & other Contributors
# This Is my Version of the wiki searchup App.
# ----------------------------------------------------------------------------------
import wikipedia as wiki
from tkinter import *
import customtkinter

# Create App
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
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
lf1 = customtkinter.CTkFrame(root, border_width=1, border_color='blue', corner_radius=20, width=620, height=40)
lf1.pack(pady=10)

# Adding Entry (e1) as Input to LF1
e1 = customtkinter.CTkEntry(lf1, width=400, height=30, text_font=('Agency FB', 19), corner_radius=20, placeholder_text='Enter What You Want To Search')
e1.grid(row=0, column=0, padx=10, pady=10)

# Adding Label for Beauty
l1 = customtkinter.CTkLabel(lf1, text="INFOLINK-VPL", text_font=('Transformers Movie', 18))
l1.grid(row=0, column=1, padx=2)

# Adding Option Menu for Theme Selection
om1 = customtkinter.CTkOptionMenu(master=self.frame_left,values=["Light", "Dark", "System"],command=self.change_appearance_mode)

# Creating Frame for Output
lf2 = customtkinter.CTkFrame(root, border_width=1, border_color='blue', corner_radius=20, width=500, height=40)
lf2.pack(pady=10)

# Creating Scrollbar (out_scroll) for Output Text (out_text) & adding to LF2
# out_scroll = Scrollbar(lf2)
# out_scroll.pack(side=RIGHT, fill=Y, pady=10, padx=10)

# Adding Text (out_text) as Output to LF2
out_text = Text(lf2, font=('Agency FB', 18), wrap=WORD, width=55, height=15, bg='#292929', fg='silver', border=0) # , yscrollcommand=out_scroll.set
out_text.pack(pady=10, padx=10)

# Configure The ScrollBar (out_scroll)
# out_scroll.configure(command=out_text.yview)

# Creating Frame for Input Buttons
lf3 = customtkinter.CTkFrame(root, border_width=1, border_color='blue', corner_radius=20, width=500, height=40)
lf3.pack(pady=10)

# Adding Button (b1) For Searching Wiki to LF3
b1 = customtkinter.CTkButton(lf3, text='Search', command=lambda: search(e1.get()), height=30, corner_radius=20, text_font=('Agency FB',20))
b1.grid(row=0, column=0, padx=10, pady=10)

# Adding Button (b1) For Searching Wiki to LF3
b2 = customtkinter.CTkButton(lf3, text='Clear', command=clear, height=30, corner_radius=20, text_font=('Agency FB',20))
b2.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()
