#!/usr/bin/python
<<<<<<< HEAD
#Creating Saved Options


=======
>>>>>>> 68fb8fbc57e0db61d02b3f638eba5b3d2c22f49d
import  locale, time, os, subprocess, errno


########  Define global variables
<<<<<<< HEAD
<<<<<<< HEAD
modes=['single','1x4','2x2']
fonts_list=['goingtodogreatthings', 'Moon Flower Bold:style=Regular']
=======
modes=['1x4','single']
fonts_list=['goingtodogreatthings']
>>>>>>> 68fb8fbc57e0db61d02b3f638eba5b3d2c22f49d
language_dict={		   # dictionary to set the language/locale for each event	
				'eng':'en_US.UTF-8', 
				'esp':'es_ES.UTF-8', 
				'cat':'ca_ES.UTF-8'
				}
######## Create text strings



locale.setlocale(locale.LC_ALL, language_dict[self.language]) # set the preferred language (i.e. locale) for the event
=======
#lists
modes=['1x4','single']
fonts_list=['goingtodogreatthings']
# directories
scripts_directory="/home/pi/can_pages_photobooth"
photos_directory="/home/pi/Pictures/"+time.strftime("%d-%m-%Y")
temp_photos_directory="/home/pi/Pictures/temp"
>>>>>>> d53ca6e325032359de40a1288e95eef6434e7033

#pre-formatted text strings
date_text_string="%s %s %s" % (time.strftime("%d").lstrip("0"),time.strftime("%B"),time.strftime("%Y"))	
date_number_string="%s %s %s" % (time.strftime("%d").lstrip("0"),time.strftime("%B"),time.strftime("%Y"))	
photo_text_string=''

###### Define functions
def get_text_string_from_user():
	confirmation1=''
	confirmation2=''
	user_input1 = raw_input("\n\n\nPor favor, introduce el texto (30 caracteres max) que aparecera en la primera linea. Cuando este, pulse ENTER\n\n")

	while len(user_input1) >30 or confirmation1!='SI':
		if len(user_input1) >30:
			user_input1 = raw_input("\nOops- has introducido mas de 30 caracteres (eran %s)! Por favor, vuelve a introduce el texto para la primera linea. Cuando este, pulse ENTER\n\n" % len(user_input1))
		elif len(user_input1) <=30 and confirmation1!='SI':
			print("\nEl texto que has introducido es (%s caracteres):\n%s\n" % (len(user_input1),user_input1))
			confirmation1=raw_input("\nEsta todo correcto? Introduce SI si todo esta correcto y quieres seguir, o introduce NO si quieres volver a introducir el texto.\n\n")
			confirmation1=confirmation1.upper()
			if confirmation1!='SI':
				user_input1 = raw_input("\n\n\nPor favor, introduce el texto (30 caracteres max) que aparecera en la primera linea. Cuando este, pulse ENTER\n\n")
	user_input2 = raw_input("\n\n\nPor favor, introduce el texto (30 caracteres max) que aparecera en la segunda linea. Cuando este, pulse ENTER\n\n")
	while len(user_input2) >30 or confirmation2!='SI':
		if len(user_input2) >30:
			user_input2 = raw_input("\nOops- has introducido mas de 30 caracteres (eran %s)! Por favor, vuelve a introduce el texto para la segunda linea. Cuando este, pulse ENTER\n\n" % len(user_input2))
		elif len(user_input2) <=30 and confirmation2!='SI':
			print("\nEl texto que has introducido es (%s caracteres):\n%s\n" % (len(user_input2),user_input2))
			confirmation2=raw_input("\nEsta todo correcto? Introduce SI si todo esta correcto y quieres seguir, o introduce NO si quieres volver a introducir el texto.\n\n")
			confirmation2=confirmation2.upper()
			if confirmation2!='SI':
				user_input2 = raw_input("\n\n\nPor favor, introduce el texto (30 caracteres max) que aparecera en la segunda linea. Cuando este, pulse ENTER\n\n")

	photo_text_string="%s\n%s" % (user_input1,user_input2)
	return photo_text_string
def clear_temp_directory():
	"""
	A function which deletes all the files in the temp directory
	"""
	try:
		command="rm %s/*"%(temp_photos_directory)
		subprocess.check_output("%s"% command, shell=True)
		num_captures+=1
	except subprocess.CalledProcessError as e:
		print e.output	


def capture_pictures(mode):
	"""
	A function which calls gphoto2 to capture the images from the DSLR
	"""
	clear_temp_directory()
	if mode=="1x4":
		num_captures=0	
		while num_captures<4:
			for x in range(3,0,-1):
				print("Taking picture in %s" % x)
				time.sleep(1)
			try:
				command="gphoto2 --capture-image-and-download --filename %s/capture_%s:%s:%s.jpg"%(temp_photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
				subprocess.check_output("%s"% command, shell=True)
				num_captures+=1
			except subprocess.CalledProcessError as e:
				print e.output	
	elif mode=="single":
		try:
			command="gphoto2 --capture-image-and-download --filename %s/capture_%s:%s:%s.jpg"%(temp_photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
			subprocess.check_output("%s"% command, shell=True)
		except subprocess.CalledProcessError as e:
			print e.output
	else: 
		pass

		
def create_photo_montage(font,text,mode):
	"""
	A function which takes the captured images and creates a file (single shot or 1x4 photo strip) in the appropriate directory
	"""
						
	if mode=="1x4":
		try:         
			command="montage %s/capture*.jpg -tile 1x4 -geometry +5+5 %s/temp_montage2.jpg" % (temp_photos_directory,temp_photos_directory)
			print(command)
			subprocess.check_output("%s" % command, shell=True)
			try:         
				command="convert -background white -size 1960x660 -fill black -font '%s' -gravity center  label:'%s'  %s/photobooth_label.jpg" % (font, text, temp_photos_directory)
				print(command)
				subprocess.check_output("%s" % command, shell=True)
				try:         
					command="montage %s/temp_montage2.jpg %s/photobooth_label.jpg -tile 1x2 -geometry +30+30 %s/temp_montage3.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
					print(command)
					subprocess.check_output("%s" % command, shell=True)
					try:         
						command="montage %s/temp_montage3.jpg %s/temp_montage3.jpg -tile 1x2 -geometry +0+0 -rotate 270 %s/temp_montage_final.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
						print(command)
						subprocess.check_output("%s" % command, shell=True)
						try:         
							new_file_name="%s/Can_Pages_Photobooth_%s:%s:%s.jpg" %(photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
							command="cp %s/temp_montage3.jpg %s" % (temp_photos_directory,new_file_name)
							print(command)
							subprocess.check_output("%s" % command, shell=True)
							try:         
								command="lp %s" % (new_file_name)
								print(command)
								subprocess.check_output("%s" % command, shell=True)
<<<<<<< HEAD
								try:         
<<<<<<< HEAD
									command="lp -d Dai_Nippon_Printing_DS40/1x4 %s" % (new_file_name)
=======
									new_file_name="%s/Can_Pages_Photobooth_1x4_%s:%s:%s.jpg" %(photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
									command="cp %s/temp_montage3.jpg %s" % (temp_photos_directory,new_file_name)
>>>>>>> 68fb8fbc57e0db61d02b3f638eba5b3d2c22f49d
									print(command)
									subprocess.check_output("%s" % command, shell=True)
									try:         
										command="lp %s" % (new_file_name)
										print(command)
										subprocess.check_output("%s" % command, shell=True)
										
									except subprocess.CalledProcessError as e:
										print e.output	
								except subprocess.CalledProcessError as e:
									print e.output	
=======
								
>>>>>>> d53ca6e325032359de40a1288e95eef6434e7033
							except subprocess.CalledProcessError as e:
								print e.output	
						except subprocess.CalledProcessError as e:
							print e.output		
					except subprocess.CalledProcessError as e:
						print e.output			
				except subprocess.CalledProcessError as e:
					print e.output		
			except subprocess.CalledProcessError as e:
				print e.output				
		except subprocess.CalledProcessError as e:
			print e.output	
			
	elif mode=="single":
		try:         
			new_file_name="%s/Can_Pages_Photobooth_%s:%s:%s.jpg" %(photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
			command="cp %s/capture*.jpg %s" % (temp_photos_directory,new_file_name)
			print(command)
			subprocess.check_output("%s" % command, shell=True)
			try:         
				command="lp %s" % (new_file_name)
				print(command)
				subprocess.check_output("%s" % command, shell=True)
				
			except subprocess.CalledProcessError as e:
				print e.output	
		except subprocess.CalledProcessError as e:
			print e.output		
	else: 
		print("Please select a correct mode {single, 1x4}")


text=get_text_string_from_user()	

<<<<<<< HEAD
capture_pictures("2x2")
create_photo_montage(fonts_list[1],novios.photo_string(' & '), '2x2')
=======
capture_pictures("1x4")

<<<<<<< HEAD
create_photo_montage(fonts_list[0],"J+M", '1x4')
>>>>>>> 68fb8fbc57e0db61d02b3f638eba5b3d2c22f49d
=======
create_photo_montage(fonts_list[0],text, '1x4')
>>>>>>> d53ca6e325032359de40a1288e95eef6434e7033
