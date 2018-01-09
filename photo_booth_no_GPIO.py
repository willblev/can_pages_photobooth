#!/usr/bin/python

# May need to run these commands in the bash terminal first, selecting ca_ES.UTF-8 manually 
# export LC_ALL="en_US.UTF-8"
# export LC_CTYPE="en_US.UTF-8"
# sudo dpkg-reconfigure locales
import  locale, time, os, subprocess, errno

language_dict={				
				'eng':'en_US.UTF-8', 
				'esp':'es_ES.UTF-8', 
				'cat':'ca_ES.UTF-8'
				}

class Novios:
	"""
	A class with the following attributes:
	names: An array containing the names of the novios, as they wish for them to appear on the printed photos
	language: a string representing the language of the novios [eng, esp, cat]
	"""
	def __init__(self, names, language):
		self.names = names
		self.language = language
		locale.setlocale(locale.LC_ALL, language_dict[self.language]) # set the preferred language (i.e. locale) for the event

	def photo_string(self,combiner=''):
		if combiner=='': # if it is left blank, add a space
			 combiner=' ' 
		photo_string="%s%s%s %s %s %s" % (self.names[0], combiner,self.names[1],time.strftime("%B").capitalize(),time.strftime("%d").lstrip("0"),time.strftime("%Y"))	
		return photo_string

# Get input for names and language from a configuration file
novios=Novios(['Sal','Berta'], 'eng')

print(novios.photo_string(' + '))
scripts_directory="/home/pi/can_pages_photobooth"
photos_directory="/home/pi/Pictures/"+time.strftime("%d-%m-%Y")+"_"+novios.names[0]+"_"+novios.names[1]
temp_photos_directory="/home/pi/Pictures/temp"

if not os.path.exists(photos_directory):
	os.makedirs(photos_directory)
print("Created "+photos_directory)

if not os.path.exists(temp_photos_directory):
	os.makedirs("/home/pi/Pictures/temp")
	print("Created "+temp_photos_directory)
    


# snap=0
# while snap < 4:
  # print("pose!")
  # time.sleep(3.5)
  # print("SNAP")
  # gpout = subprocess.check_output("gphoto2 --capture-image-and-download --filename %s/snap%H%M%S.jpg"%(temp_photo_directory), stderr=subprocess.STDOUT, shell=True)
  # print(gpout)
  # if "ERROR" not in gpout: 
	# snap += 1
  # time.sleep(0.5)
# print("please wait while your photos print...")
# # build image and send to printer
# subprocess.call("sudo %s/assemble_and_print.sh" % (scripts_directory), shell=True)
