#!/usr/bin/python
<<<<<<< HEAD
#Creating Saved Options


=======
>>>>>>> 68fb8fbc57e0db61d02b3f638eba5b3d2c22f49d
import  locale, time, os, subprocess, errno


########  Define global variables
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

date_text_string="%s %s %s" % (time.strftime("%d").lstrip("0"),time.strftime("%B"),time.strftime("%Y"))	
date_number_string="%s %s %s" % (time.strftime("%d").lstrip("0"),time.strftime("%B"),time.strftime("%Y"))	
photo_text_string="%s" % 


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
			command="mogrify -gravity Center -crop '70x80%+0+0'  %s/capture*.jpg" % (temp_photos_directory)
			print(command)
			subprocess.check_output("%s" % command, shell=True)
			try:         
				command="mogrify -resize 484x324 %s/capture*.jpg" % (temp_photos_directory)
				print(command)
				subprocess.check_output("%s" % command, shell=True)
				try:         
					command="montage %s/capture*.jpg -tile 1x4 -geometry +5+5 %s/temp_montage2.jpg" % (temp_photos_directory,temp_photos_directory)
					print(command)
					subprocess.check_output("%s" % command, shell=True)
					try:         
						command="convert -background white -size 1100x80 -fill black -font '%s' -gravity center  label:'%s' -rotate 270 %s/photobooth_label.jpg" % (font, text, temp_photos_directory)
						print(command)
						subprocess.check_output("%s" % command, shell=True)
						try:         
							command="montage %s/temp_montage2.jpg %s/photobooth_label.jpg -tile 2x1 -geometry +5+5 %s/temp_montage3.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
							print(command)
							subprocess.check_output("%s" % command, shell=True)
							try:         
								command="montage %s/temp_montage3.jpg %s/temp_montage3.jpg -tile 1x2 -geometry +5+5 -rotate 270 %s/temp_montage_final.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
								print(command)
								subprocess.check_output("%s" % command, shell=True)
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

<<<<<<< HEAD
capture_pictures("2x2")
create_photo_montage(fonts_list[1],novios.photo_string(' & '), '2x2')
=======
capture_pictures("1x4")

create_photo_montage(fonts_list[0],"J+M", '1x4')
>>>>>>> 68fb8fbc57e0db61d02b3f638eba5b3d2c22f49d
