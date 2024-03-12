from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1366x768')
root.resizable(0, 0)
root['bg'] = 'royalblue'

'''
img = PhotoImage(file="E:\\Timurcik\\Exam\\translator.png")
root.iconphoto(False,img)
'''

root.title('Awdarmashi')
Label(root, text = "Awdarmashi by Timur", font = 'Arial 30 bold').place(x=450, y=20)

Label(root, text = "Tekstinizdi kiritin", font = 'arial 15 bold', bg = 'white smoke').place(x=220, y=300)

text_enter = Entry(root, width= 60)
text_enter.place(x=110, y=350)
#text_enter.get()

Label(root, text= "Awdarmalang'an teksti", font='arial 15 bold', bg='white smoke').place(x= 850, y= 300)
awdarmalangan = Text(root, font='arial 10', height=5, wrap = WORD, padx= 5, pady= 5, width= 50)
awdarmalangan.place(x= 850, y= 350)

language = list(LANGUAGES.values())

dest_lang= ttk.Combobox(root, values= language, width = 30)
dest_lang.place(x=200, y=400)
dest_lang.set('Tillerdi saylan:')

def Translate():
    translator = Translator()
    translated = translator.translate(text=text_enter.get(), dest = dest_lang.get())
    awdarmalangan.delete(1.0, END)
    awdarmalangan.insert(END, translated.text)

trans_btn= Button(root, text='Awdarmalaw', font= 'arial 12 bold', command= Translate, bg= 'orange')
trans_btn.place(x= 600, y=400)

Label(root, text = "dev: @r_on_in\nPhone: +998 93 849-99-98", font = 'Helvetica 15', bg='royalblue' ).place(x=1100, y=650)

root.mainloop()
