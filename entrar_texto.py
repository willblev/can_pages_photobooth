#import tkinter,time

#scripts_directory="/home/pi/can_pages_photobooth"

#def get_text_string_from_user():
	#user_input1 = raw_input("\n\n\nPor favor, introduce el texto (30 caracteres max) que aparecera en la primera linea. Cuando este, pulse ENTER\n\n")
	#if length(user_input)>=30:
		#print("\nAVISO! Has introducido mas de 30 caracteres (eran %s)! Puede que no se puede leer bien la foto n\n" % len(user_input1))
	#print("\nEl texto que has introducido es (%s caracteres):\n%s\n" % (len(user_input1),user_input1))
	#time.sleep(5)
			
	#photo_text_string="%s\n%s" % (user_input1,user_input2)
	#return photo_text_string
	
#with open(scripts_directory+"configuration.txt", 'w') as config_file:
	#config_file.write(get_text_string_from_user)

#import the 'tkinter' module
import Tkinter as tkinter

#create a new window
window = tkinter.Tk()
#set the window background to hex code '#a1dbcd'
window.configure(background="#a1dbcd")
#set the window title
window.title("Introducir texto")
#set the window icon



#create a label for the instructions
lblInst = tkinter.Label(window, text="Por favor, introduce el texto", fg="#383a39", bg="#a1dbcd", font=("Helvetica", 16))
#and pack it into the window
lblInst.pack()

#create the widgets for entering a username
lblUsername = tkinter.Label(window, text="Primera linea:", fg="#383a39", bg="#a1dbcd")
entUsername = tkinter.Entry(window)
#and pack them into the window
lblUsername.pack()
entUsername.pack()

#create the widgets for entering a username
lblPassword = tkinter.Label(window, text="Segunda linea:", fg="#383a39", bg="#a1dbcd")
entPassword = tkinter.Entry(window)
#and pack them into to the window
lblPassword.pack()
entPassword.pack()

#create a button widget called btn
btn = tkinter.Button(window, text="Login", fg="#a1dbcd", bg="#383a39", command=press())
#pack the widget into the window
btn.pack()

#draw the window, and start the 'application'
window.mainloop()


