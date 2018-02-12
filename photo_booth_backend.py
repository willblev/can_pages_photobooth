#!/usr/bin/python
import  locale, time, os, subprocess, errno


########  Define global variables
modes=['1x4','single']
fonts_list=['goingtodogreatthings']
language_dict={		   # dictionary to set the language/locale for each event	
				'eng':'en_US.UTF-8', 
				'esp':'es_ES.UTF-8', 
				'cat':'ca_ES.UTF-8'
				}
######## Create text strings



locale.setlocale(locale.LC_ALL, language_dict[self.language]) # set the preferred language (i.e. locale) for the event

date_text_string="%s %s %s" % (time.strftime("%d").lstrip("0"),time.strftime("%B"),time.strftime("%Y"))	
date_number_string="%s %s %s" % (time.strftime("%d").lstrip("0"),time.strftime("%B"),time.strftime("%Y"))	
photo_text_string="%s" % "hahaha"


def capture_pictures(mode):
	"""
	A function which calls gphoto2 to capture the images
	"""
	try:         
		print(command)
		command="rm %s/*.jpg" % (temp_photos_directory)
	except subprocess.CalledProcessError as e:
		print e.output	
		
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
	A function which creates a photo montage, either 10x15 or 5x15cm (two strips)
	"""
			

						
	if mode=="1x4":
		try:  
			command="rm %s/*.jpg" % (temp_photos_directory)
			print(command)
			subprocess.check_output("%s" % command, shell=True)
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
		except subprocess.CalledProcessError as e:
			print e.output					
	elif mode=="single":
		pass
	else: 
		pass		


def clear_temp_directory():
	try:         
		command="rm %s/*.jpg" % (temp_photos_directory)
		print(command)
		subprocess.check_output("%s" % command, shell=True)
	except subprocess.CalledProcessError as e:
		print e.output			

		
######## Create directories
scripts_directory="/home/pi/can_pages_photobooth"
photos_directory="/home/pi/Pictures/"+time.strftime("%d-%m-%Y")+"_"+novios.names[0]+"_"+novios.names[1]
temp_photos_directory="/home/pi/Pictures/temp"

if not os.path.exists(photos_directory):
	os.makedirs(photos_directory)
	print("Created "+photos_directory)

capture_pictures("1x4")

create_photo_montage(fonts_list[0],"J+M", '1x4')
