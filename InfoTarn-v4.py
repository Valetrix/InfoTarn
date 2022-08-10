# Code Available at - https://github.com/Valetrix/Wiki
# Coded By Valetrix - Credits: John Elder, Codemy & other Contributors
# This Is my Version of the wiki searchup App.
# ----------------------------------------------------------------------------------
import wikipedia as wiki
from tkinter import *
import customtkinter
# from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

# Create App
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.geometry('700x650')
root.title('InfoTarn-VPL')
root.iconbitmap('Info-Tarn-Logo.ico')

# Asking Client If they agree to T&C
m1 = messagebox.askyesno("IMPORTANT Message", "While using this app, Do you agree to all the Terms and conditions that apply and relate to this application?\n\nThank you for choosing InfoTarn From VPL\n(Valetrix Programming Limited.)")
if m1 == 0:
	root.destroy()
else:
	pass

# Functions
def search(x):
	global results
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

def theme():
	if out_text['background'] == '#292929':
		out_text.config(bg='#ebebeb', fg='black')
	# elif out_text['background'] == '#ebesbeb':
	else:
		out_text.config(bg='#292929', fg="silver")

def save_info():
	global results
	file = filedialog.asksaveasfilename(defaultextension='.*', initialdir="C:/", title='Save Information', filetypes=(('Text Files', '*.txt'), ('ODT Files', '*.odt'), ('Doc files', '*docx')))
	if file:
		file = open(file, 'w')
		file.write(out_text.get('1.0', END))
		file.close
#Creating Frame for Input
lf1 = customtkinter.CTkFrame(root, border_width=1, border_color='blue', corner_radius=20, width=620, height=40)
lf1.pack(pady=10)

# Adding Entry (e1) as Input to LF1
e1 = customtkinter.CTkEntry(lf1, width=400, height=30, text_font=('Agency FB', 19), corner_radius=20, placeholder_text='Enter What You Want To Search')
e1.grid(row=0, column=0, padx=10, pady=10)

# Adding Label for Beauty
# l1 = customtkinter.CTkLabel(lf1, text="INFOLINK-VPL", text_font=('Transformers Movie', 18))
# l1.grid(row=0, column=1, padx=2)

# Adding Option Menu for Theme Selection
om1 = customtkinter.CTkOptionMenu(lf1,values=["Dark", "light"],command=customtkinter.set_appearance_mode)
om1.grid(row=0, column=1, padx=10)

# Creating Frame for Output
lf2 = customtkinter.CTkFrame(root, border_width=1, border_color='blue', corner_radius=20, width=500, height=40)
lf2.pack(pady=10)

# Creating Scrollbar (out_scroll) for Output Text (out_text) & adding to LF2
# out_scroll = Scrollbar(lf2)
# out_scroll.pack(side=RIGHT, fill=Y, pady=10, padx=10)

# Adding Text (out_text) as Output to LF2
z = customtkinter.get_appearance_mode()
if z == "light":
	out_text = Text(lf2, font=('Agency FB', 18), wrap=WORD, width=55, height=15, bg='grey', fg='black', border=0)
elif z == "dark":
	out_text = Text(lf2, font=('Agency FB', 18), wrap=WORD, width=55, height=15, bg='#292929', fg='silver', border=0)
elif z == "System":
	out_text = Text(lf2, font=('Agency FB', 18), wrap=WORD, width=55, height=15, bg='#292929', fg='white', border=0)
out_text = Text(lf2, font=('Agency FB', 18), wrap=WORD, width=55, height=15, bg='#292929', fg='white', border=0)
out_text.pack(pady=10, padx=10)


# Configure The ScrollBar (out_scroll)
# out_scroll.configure(command=out_text.yview)

# Creating Frame for Input Buttons
lf3 = customtkinter.CTkFrame(root, border_width=1, border_color='blue', corner_radius=20, width=500, height=40)
lf3.pack(pady=10)

# Adding Button (b1) For Searching Wiki to LF3
b1 = customtkinter.CTkButton(lf3, text='Search', command=lambda: search(e1.get()), height=30, corner_radius=20, text_font=('Agency FB',20))
b1.grid(row=0, column=0, padx=10, pady=10)

# Adding Button (b2) For Clearing Everything to LF3
b2 = customtkinter.CTkButton(lf3, text='Clear', command=clear, height=30, corner_radius=20, text_font=('Agency FB',20))
b2.grid(row=0, column=1, padx=10, pady=10)

b3 = customtkinter.CTkButton(lf3, text='Save', command=save_info, height=30, corner_radius=20, text_font=('Agency FB',20))
b3.grid(row=0, column=2, padx=10, pady=10)

# Adding Button (b3) For Correcting theme to LF3
b4 = customtkinter.CTkButton(lf3, text='THEME', command=theme, height=30, corner_radius=20, text_font=('Agency FB',20))
b4.grid(row=0, column=3, padx=10, pady=10)

root.mainloop()
