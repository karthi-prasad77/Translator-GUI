from tkinter import *
from translate import Translator

# translator function
def translate():
    translator = Translator(from_lang=lang_1.get(), to_lang=lang_2.get())
    translation = translator.translate(var.get())
    var1.set(translation)

# tkinter root element
root = Tk()
root.title("Translator Desktop")
root.geometry("750x250")

# create frame and grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

#variables for dropdown list
lang_1 = StringVar(root)
lang_2 = StringVar(root)

#choices to show in dropdown menu
choices = { 'English','Tamil','Hindi','Spanish','German'}
#default selection for dropdownlists
lang_1.set('English')
lang_2.set('Tamil')

#creating dropdown and arranging in the grid
lan1menu = OptionMenu( mainframe, lang_1, *choices)
Label(mainframe,text="Select a language").grid(row = 0, column = 1)
lan1menu.grid(row = 1, column =1)

lan2menu = OptionMenu( mainframe, lang_2, *choices)
Label(mainframe,text="Select a language").grid(row = 0, column = 2)
lan2menu.grid(row = 1, column =2)

#Text Box to take user input
Label(mainframe, text = "Enter text").grid(row=2,column=0)
var = StringVar()
textbox = Entry(mainframe, textvariable=var).grid(row=2,column=1)

#textbox to show output
#label can also be used
Label(mainframe, text = "Output").grid(row=2,column=2)
var1 = StringVar()
textbox = Entry(mainframe, textvariable=var1).grid(row=2,column=3)

#creating a button to call Translator function
b=Button(mainframe,text='Translate',command=translate).grid(row=3,column=1,columnspan=3)

root.mainloop()