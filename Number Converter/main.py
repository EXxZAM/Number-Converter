


from tkinter import * 
from tkinter import ttk
from tkinter.font import BOLD
from tkinter import messagebox
import random
import os

root = Tk()
root.title('Number Converter')
root.geometry('400x200')
root.config(bg='#121212')


# TODO => Decimal Number Entry  ✔
# TODO => Binary Number Entry ✔
# TODO => DropDown to decide which way to go (Dec to Bin or the opposite) ✔
# TODO => Convert Button ✔

#! Functions

def convert():
    binary = bin_entry.get()
    decimal = dec_entry.get()
    bin_entry.delete(0,END)
    dec_entry.delete(0,END)
    if input_combobox.get() == 'Binary To Decimal':
        #? Converts Binary To Decimal
        
        
        converted = int(binary,2) 
        dec_entry.insert(0, converted)
    elif input_combobox.get() == 'Decimal To Binary':
        #? Converts Decimal To Binary
        
        converted = bin(int(decimal)).replace("0b","")
        bin_entry.insert(0, converted)
    else:
        messagebox.showinfo('Choose An Option', 'Choose An Option')
    


#! Variables
options = ['Binary To Decimal', 'Decimal To Binary']

#! Widgets
bin_label = Label(root, text='Binary: ', bg='#121212', fg='white')
bin_entry = Entry(root, width=30)

dec_label = Label(root, text='Decimal: ', bg='#121212', fg='white')
dec_entry = Entry(root, width=30)

input_combobox = ttk.Combobox(root, value=options, font=('Calibri',10), justify='center')
input_combobox.set('Choose')


convert_btn = Button(root, text='Convert', bg='#121212', fg='white', borderwidth=3, width=40, font=('Calibri',10,BOLD), command=convert)


#! Griding Widgets
bin_label.grid(row=0, column=0,padx=(0,100),pady=(10,0))
bin_entry.grid(row=1, column=0,padx=10,pady=5)

dec_label.grid(row=0, column=1, padx=(0,100), pady=(10,0))
dec_entry.grid(row=1, column=1)

input_combobox.place(relx=0.5, rely=0.4, anchor='c')

convert_btn.place(relx=0.5, rely=0.6, anchor='c')


root.mainloop()


#? Made By EXxZAM (mahdi Olamaei)
#! Personal Project