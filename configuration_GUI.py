import Tkinter

def OK_press():
	global entFirstLine
	print("Primera linea de texto: ",entFirstLine.get)
	print("Segunda linea de texto: ",entSecondLine.get)
	print("Idioma seleciondado: ",lang.get)
	window.quit()
#create a new window
window = Tkinter.Tk()
#set the window background to hex code '#a1dbcd'
window.configure(background="#a1dbcd")
#set the window title
window.title("Menu de configuracion")
#set the window icon




#create a label for the instructions
lblInst = Tkinter.Label(window, text="Por favor, introduce el texto", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
#and pack it into the window
lblInst.pack()

#create the widgets for entering a FirstLine
lblFirstLine = Tkinter.Label(window, text="Texto primera linea", fg="#383a39", bg="#a1dbcd")
entFirstLine = Tkinter.Entry(window)
#and pack them into the window
lblFirstLine.pack()
entFirstLine.pack()

#create the widgets for entering a SecondLine
lblSecondLine = Tkinter.Label(window, text="Texto segunda linea", fg="#383a39", bg="#a1dbcd")
entSecondLine = Tkinter.Entry(window)
#and pack them into to the window
lblSecondLine.pack()
entSecondLine.pack()

#create the widgets for entering a Language
lblLanguage = Tkinter.Label(window, text="Idioma", fg="#383a39", bg="#a1dbcd")

lang = Tkinter.StringVar(window)
lang.set("Espanol") # default value
entLanguage = Tkinter.OptionMenu(window, lang, "Espanol", "Catala", "English")

#entLanguage = apply(OptionMenu, (window, lang) + tuple(OPTIONS))
#entLanguage = Tkinter.Entry(window)
#and pack them into to the window
lblLanguage.pack()
entLanguage.pack()


#create a button widget called btn
btn = Tkinter.Button(window, text="OK", fg="#a1dbcd", bg="#383a39", command=OK_press)
#pack the widget into the window
btn.pack()

#draw the window, and start the 'application'
window.mainloop()


 
