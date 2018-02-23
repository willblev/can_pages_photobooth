import tkinter,os, subprocess
from PIL import Image, ImageTk
config_file="/home/william/github/can_pages_photobooth/config.txt"
temp_photos_directory="/home/william/github/can_pages_photobooth/"

def OK_press():
	# on button press, save config file and print options that were selected
	print("Idioma seleciondado: ",lang.get())
	print("Primera linea de texto: ",firstline.get())
	print("Segunda linea de texto: ",secondline.get())
	print("Fuente seleciondado: ",font.get())

	with open(config_file, 'w') as output_file:
		output_file.write("%s\n%s\n%s\n%s\n"%(lang.get(),firstline.get(),secondline.get(),font.get()))
	window.quit()
	
	
def preview():
#on preview button press, render the font/text with imagemagik
	textString="%s\n%s"%(firstline.get(),secondline.get())
	selectedFont=font.get()
	command1="convert -background white -size 1000x360 -fill black -font '%s' -gravity center  label:'%s'  %s/text_preview.jpg" % (selectedFont, textString, temp_photos_directory)
	subprocess.check_output("%s" % command1, shell=True)
	img2 = ImageTk.PhotoImage(Image.open(temp_photos_directory+"text_preview.jpg"))
	panel.configure(image=img2)
	panel.image = img2
				
#create a new window
window = tkinter.Tk()
#set the window background to hex code '#a1dbcd'
window.configure(background="#a1dbcd")
#set the window title
window.title("Can Pagès Photobooth")
#set the window icon


firstline = tkinter.StringVar(window)
secondline = tkinter.StringVar(window)
font = tkinter.StringVar(window)
lang = tkinter.StringVar(window)


#create a label for the instructions
lblInst = tkinter.Label(window, text="Configuración", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
#and pack it into the window
lblInst.pack()


#create the widgets for entering a Language
lblLanguage = tkinter.Label(window, text="Seleccione el idioma", fg="#383a39", bg="#a1dbcd")

lang.set("Espanol") # default value
entLanguage = tkinter.OptionMenu(window, lang, "Español", "Català", "English")

#and pack them into to the window
lblLanguage.pack()
entLanguage.pack()

#create the widgets for entering a FirstLine
lblFirstLine = tkinter.Label(window, text="Texto primera línea", fg="#383a39", bg="#a1dbcd")
entFirstLine = tkinter.Entry(window, textvariable=firstline)
#and pack them into the window
lblFirstLine.pack()
entFirstLine.pack()

#create the widgets for entering a SecondLine
lblSecondLine = tkinter.Label(window, text="Texto segunda línea", fg="#383a39", bg="#a1dbcd")
entSecondLine = tkinter.Entry(window, textvariable=secondline)
#and pack them into to the window
lblSecondLine.pack()
entSecondLine.pack()

#create the widgets for choosing a font
lblFont = tkinter.Label(window, text="Seleccione la fuente", fg="#383a39", bg="#a1dbcd")

font.set("Helveticia") # default value
entFont = tkinter.OptionMenu(window, font, "Helvetica", "goingtodogreatthings", "Comicsans")

#and pack them into to the window
lblFont.pack()
entFont.pack()

##preview font image
img = ImageTk.PhotoImage(Image.open(temp_photos_directory+"text_preview.jpg"))
panel = tkinter.Label(window, image=img)
panel.pack(side="bottom", fill="both", expand="yes")


#create a button widget called btn
btn = tkinter.Button(window, text="Vista preliminar", fg="#a1dbcd", bg="#383a39", command=preview)
#pack the widget into the window
btn.pack()
#create a button widget called btn
btn = tkinter.Button(window, text="OK", fg="#a1dbcd", bg="#383a39", command=OK_press)
#pack the widget into the window
btn.pack()

#draw the window, and start the 'application'
window.mainloop()


 
