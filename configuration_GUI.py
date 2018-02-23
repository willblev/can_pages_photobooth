import tkinter,os, subprocess
from PIL import Image, ImageTk
config_file="/home/pi/can_pages_photobooth/config.txt"
temp_photos_directory="/home/pi/Pictures/temp/"
scripts_directory="/home/pi/can_pages_photobooth/"

def OK_press():
	# on button press, save config file and print options that were selected
	print("Idioma seleciondado: ",lang.get())
	print("Modo seleciondado: ",mode.get())
	print("Primera linea de texto: ",firstline.get())
	print("Segunda linea de texto: ",secondline.get())
	print("Fuente seleciondado: ",usrfont.get())

	with open(config_file, 'w') as output_file:
		output_file.write("LANGUAGE:%s\nMODE:%s\nFIRSTLINE:%s\nSECONDLINE:%s\nFONT:%s\n"%(lang.get(),mode.get(),firstline.get(),secondline.get(),usrfont.get()))
	window.quit()
	
	
def preview():
#on preview button press, render the font/text with imagemagik
	textString="%s%s"%(firstline.get(),secondline.get())
	selectedFont=usrfont.get()
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
usrfont = tkinter.StringVar(window)
lang = tkinter.StringVar(window)
mode = tkinter.StringVar(window)


#create a label for the instructions
lblInst = tkinter.Label(window, text="Configuración", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
#and pack it into the window
lblInst.pack()


#create the widgets for entering a Language
lblLanguage = tkinter.Label(window, text="Seleccione el idioma", fg="#383a39", bg="#a1dbcd",font=("Helvetica", 16))

lang.set("Espanol") # default value
entLanguage = tkinter.OptionMenu(window, lang, "Español", "Català", "English")
entLanguage.config(font=("Helvetica", 14))
#and pack them into to the window
lblLanguage.pack()
entLanguage.pack()

#create the widgets for entering a Mode
lblMode = tkinter.Label(window, text="Seleccione el modo", fg="#383a39", bg="#a1dbcd",font=("Helvetica", 16))

mode.set("5x15") # default value
entMode = tkinter.OptionMenu(window, mode, "5x15", "10x15")
entMode.config(font=("Helvetica", 14))
#and pack them into to the window
lblMode.pack()
entMode.pack()

#create the widgets for entering a FirstLine
lblFirstLine = tkinter.Label(window, text="Texto primera línea", fg="#383a39", bg="#a1dbcd",font=("Helvetica", 16))
entFirstLine = tkinter.Entry(window, textvariable=firstline)
entFirstLine.config(font=("Helvetica", 14))
#and pack them into the window
lblFirstLine.pack()
entFirstLine.pack()

#create the widgets for entering a SecondLine
lblSecondLine = tkinter.Label(window, text="Texto segunda línea", fg="#383a39", bg="#a1dbcd",font=("Helvetica", 16))
entSecondLine = tkinter.Entry(window, textvariable=secondline)
entSecondLine.config(font=("Helvetica", 14))
#and pack them into to the window
lblSecondLine.pack()
entSecondLine.pack()

#create the widgets for choosing a font
lblFont = tkinter.Label(window, text="Seleccione la fuente", fg="#383a39", bg="#a1dbcd",font=("Helvetica", 16))

usrfont.set("goingtodogreatthings") # default value
entFont = tkinter.OptionMenu(window, usrfont,  
   "Adventure",
 "Adventure-Outline",
 "Alba",
 "Alba-Super",
 "AlexandriaFLF",
 "Allura",
 "Always-In-My-Heart",
 "Another-Typewriter",
 "Austie-Bost-You-Wear-Flowers-Hollow",
 "Bakery",
 "BehrensSchrift-Normalreduced",
 "Black-Rose",
 "Bookman-Demi",
 "Chocolate-Covered-Raindrops",
 "Clicker-Script",
 "CoalhandLukeTRIAL",
 "DancingScript-Bold",
 "DKCosmoStitch",
 "Give-It-Your-Heart",
 "goingtodogreatthings",
 "Impact-Label",
 "Janda-Scrapgirl-Dots",
 "Journey-to-Thailand",
 "justbeautifulsimplicity",
 "KG-A-Little-Swag",
 "Kingthings-Extortion",
 "Lato-Regular",
 "Life-is-goofy",
 "Long-distance-call",
 "Montserrat-Regular",
 "Moon-Flower",
 "Moon-Flower-Bold",
 "Mrs.-Monster-Regular",
 "orange-juice",
 "Playfair-Display-Bold",
 "Prisma",
 "Reality-Sunday",
 "Royal-Acidbath-Outline",
 "SF-Balloons",
 "Shorelines-Script-Bold",
 "Silk-Remington-SBold",
 "Videophreak",
 "YouMurderer-BB"
)
entFont.config(font=("Helvetica", 14))

#and pack them into to the window
lblFont.pack()
entFont.pack()

##preview font image
img = ImageTk.PhotoImage(Image.open(scripts_directory+"font_list.jpg"))
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


 
