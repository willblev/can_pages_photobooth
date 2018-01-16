#!/usr/bin/python

import  locale, time, os, subprocess, errno

######## Create directories, open log file
scripts_directory="/home/pi/can_pages_photobooth"
photos_directory="/home/pi/Pictures/"+time.strftime("%d-%m-%Y")+"_"+novios.names[0]+"_"+novios.names[1]
temp_photos_directory="/home/pi/Pictures/temp"
log_file=open("%s/logfile.txt" % scripts_directory, 'w')
if not os.path.exists(photos_directory):
	os.makedirs(photos_directory)
	print("Created "+photos_directory)

########  Define global variables, classes, functions
modes=['single','photostrip','2x2']
language_dict={		   # dictionary to set the language/locale for each event	
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
		if combiner=='': # if the variable 'combiner' is left blank, add a space between the names of the novios by default
			 combiner=' ' 
		photo_string="%s%s%s   %s %s %s" % (self.names[0], combiner,self.names[1],time.strftime("%d").lstrip("0"),time.strftime("%B"),time.strftime("%Y"))	
		return photo_string

def capture_pictures(mode):
	"""
	A function which calls gphoto2 to capture the images
	"""
	if mode=="2x2" or mode=="photostrip":
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
		
def create_photo_montage(text,mode):
	"""
	A function which creates a photo montage, either 10x15 or 5x15cm (two strips)
	"""
	if mode=="2x2":		
		try:         
			command="convert -background white -size 1100x110 -fill black -font Piboto-Bold -gravity center  label:'%s' -rotate 270 %s/photobooth_label.jpg" % (text,temp_photos_directory)
			print(command)
			subprocess.check_output("%s" % command, shell=True)
		except subprocess.CalledProcessError as e:
			print e.output
			log_file.write(e.output)
		try:         
			command="mogrify -resize 968x648 %s/*.jpg" % (temp_photos_directory)
			print(command)
			subprocess.check_output("%s" % command, shell=True)
		except subprocess.CalledProcessError as e:
			print e.output
			log_file.write(e.output)
		try:         
			command="montage %s/*.jpg -tile 2x2 -geometry +10+10 %s/temp_montage2.jpg" % (temp_photos_directory,temp_photos_directory)
			print(command)
			subprocess.check_output("%s" % command, shell=True)
		except subprocess.CalledProcessError as e:
			print e.output
			log_file.write(e.output)			
		try:         
			command="montage %s/temp_montage2.jpg %s/photobooth_label.jpg -tile 2x1 -geometry +5+5 %s/temp_montage_final.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
			print(command)
			subprocess.check_output("%s" % command, shell=True)
		except subprocess.CalledProcessError as e:
			print e.output
			log_file.write(e.output)			
		try:         
			command="cp %s/temp_montage_final.jpg %s/Can_Pages_Photobooth_2x2_%s:%s:%s.jpg" % (temp_photos_directory,photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
			print(command)
			subprocess.check_output("%s" % command, shell=True)
		except subprocess.CalledProcessError as e:
			print e.output
			log_file.write(e.output)			
	
	elif mode=="photostrip":
		pass
	elif mode=="single":
		pass
	else: 
		pass		


def send_image_to_printer():
	try:         
		command="lp %s/temp_montage_final.jpg" % (temp_photos_directory)
		print(command)
		subprocess.check_output("%s" % command, shell=True)
	except subprocess.CalledProcessError as e:
		print e.output
		log_file.write(e.output)			

def clear_temp_directory():
	try:         
		command="rm %s/*.jpg" % (temp_photos_directory)
		print(command)
		subprocess.check_output("%s" % command, shell=True)
	except subprocess.CalledProcessError as e:
		print e.output
		log_file.write(e.output)			

		
		
########  Get input for names and language from a configuration file
novios=Novios(['Will','Katie'], 'eng')


capture_pictures("2x2")
create_photo_montage(novios.photo_string(' & '), '2x2')
send_image_to_printer()
#clear_temp_directory()



log_file.close()
