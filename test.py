import  locale, time, os, subprocess, errno
temp_photos_directory="/home/william/github/can_pages_photobooth/example_images" 
font='goingtodogreatthings'


## copy photos from fresh to example
command="cp  /home/william/github/can_pages_photobooth/example_images/fresh/capture* /home/william/github/can_pages_photobooth/example_images/"  
print(command)
subprocess.check_output("%s" % command, shell=True)

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


photo_text_string=get_text_string_from_user()

## perhaps we don't need to crop
#command="mogrify -gravity Center -crop '70x80%+0+0'  /home/william/github/can_pages_photobooth/example_images/capture*.jpg"  
#print(command)
#subprocess.check_output("%s" % command, shell=True)

#stack and add white border to each photo
command="montage %s/capture*.jpg -tile 1x4 -geometry +20+20 %s/temp_montage2.jpg" % (temp_photos_directory,temp_photos_directory)
print(command)
subprocess.check_output("%s" % command, shell=True)

## create label
command="convert -background white -size 1960x660 -fill black -font '%s' -gravity center  label:'%s'  %s/photobooth_label.jpg" % (font, photo_text_string, temp_photos_directory)
print(command)
subprocess.check_output("%s" % command, shell=True)

## add label + whitespace beneath 4 stacked photos
command="montage %s/temp_montage2.jpg %s/photobooth_label.jpg -tile 1x2 -geometry +30+30 %s/temp_montage3.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
print(command)
subprocess.check_output("%s" % command, shell=True)

## copy strip to photo directory (final image)
command="cp %s/temp_montage3.jpg %s/single_strip_final.jpg" % (temp_photos_directory,temp_photos_directory)
print(command)
subprocess.check_output("%s" % command, shell=True)

## combine 2 strips and rotate for printing (no strip between them in the middle!)
command="montage %s/temp_montage3.jpg %s/temp_montage3.jpg -tile 1x2 -geometry +0+0 -rotate 270 %s/temp_montage_final.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
print(command)
subprocess.check_output("%s" % command, shell=True)
