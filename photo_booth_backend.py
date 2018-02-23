import  locale, time, os, subprocess, errno
import RPi.GPIO as GPIO

### Setup GPIO
gpio_pin_number=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)


########  Define global variables

modes=['1x4','single']
fonts_list=['goingtodogreatthings']
language_dict={		   # dictionary to set the language/locale for each event	
				'eng':'en_US.UTF-8', 
				'esp':'es_ES.UTF-8', 
				'cat':'ca_ES.UTF-8'
				}
#locale.setlocale(locale.LC_ALL, language_dict[self.language]) # set the preferred language (i.e. locale) for the event

# directories
scripts_directory="/home/pi/can_pages_photobooth"
photos_directory="/home/pi/Pictures/"+time.strftime("%d-%m-%Y")
temp_photos_directory="/home/pi/Pictures/temp"

#pre-formatted text strings
date_text_string="%s %s %s" % (time.strftime("%d").lstrip("0"),time.strftime("%B"),time.strftime("%Y"))	
date_number_string="%s %s %s" % (time.strftime("%d").lstrip("0"),time.strftime("%B"),time.strftime("%Y"))	

###### Define functions

def wait_for_button_press():
	try:
		GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
		
		command0="rm fifo.mjpg"
		subprocess.check_output("%s"% command0, shell=True)    
		command1="mkfifo fifo.mjpg"
		subprocess.check_output("%s"% command1, shell=True)
		command2="gphoto2 --capture-movie=60 --stdout> fifo.mjpg & omxplayer fifo.mjpg --live"
		subprocess.check_output("%s"% command2, shell=True)
		capture_pictures("1x4")
	except:
		pass

def clear_temp_directory():
	"""
	A function which deletes all the files in the temp directory
	"""
	try:
		command="rm %s/*"%(temp_photos_directory)
		subprocess.check_output("%s"% command, shell=True)
	except subprocess.CalledProcessError as e:
		print(e.output)	


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
				print(e.output)	
	elif mode=="single":
		try:
			command="gphoto2 --capture-image-and-download --filename %s/capture_%s:%s:%s.jpg"%(temp_photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
			subprocess.check_output("%s"% command, shell=True)
		except subprocess.CalledProcessError as e:
			print e.output
	else: 
		pass

def create_photos_dir():
	photos_directory="/home/pi/Pictures/"+time.strftime("%d-%m-%Y")
	if not os.path.exists(photos_directory):
		try:
			os.makedirs(photos_directory)
			print("Created "+photos_directory)
		except subprocess.CalledProcessError as e:
			print e.output
			
			
def create_photo_montage(font,text,mode):
	"""
	A function which takes the captured images and creates a file (single shot or 1x4 photo strip) in the appropriate directory
	"""
						
	if mode=="1x4":
		try:         
			command="mogrify -resize 960x640 %s/capture*.jpg" % temp_photos_directory
			print(command)
			subprocess.check_output("%s" % command, shell=True)
			try:         
				command="montage %s/capture*.jpg -tile 1x4 -geometry +20+20 %s/temp_montage2.jpg" % (temp_photos_directory,temp_photos_directory)
				print(command)
				subprocess.check_output("%s" % command, shell=True)
				try:         
					command="convert -background white -size 1000x360 -fill black -font '%s' -gravity center  label:'%s'  %s/photobooth_label.jpg" % (font, text, temp_photos_directory)
					print(command)
					subprocess.check_output("%s" % command, shell=True)
					try:         
						command="montage %s/temp_montage2.jpg %s/photobooth_label.jpg -tile 1x2 -geometry +30+30 %s/temp_montage3.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
						print(command)
						subprocess.check_output("%s" % command, shell=True)
						try:         
							command="montage %s/temp_montage3.jpg %s/temp_montage3.jpg -tile 1x2 -geometry +30+30 -rotate 270 %s/temp_montage_final.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
							print(command)
							subprocess.check_output("%s" % command, shell=True)
							try:         
								new_file_name="%s/Can_Pages_Photobooth_%s:%s:%s.jpg" %(photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
								command="cp %s/temp_montage3.jpg %s" % (temp_photos_directory,new_file_name)
								print(command)
								subprocess.check_output("%s" % command, shell=True)
								try:         
									command="lp -d Dai_Nippon_Printing_DS40/1x4 %s/temp_montage_final.jpg" % (temp_photos_directory)
									print(command)
									#subprocess.check_output("%s" % command, shell=True)							
								except subprocess.CalledProcessError as e:
									print(e.output)	
							except subprocess.CalledProcessError as e:
								print(e.output)		
						except subprocess.CalledProcessError as e:
							print(e.output)			
					except subprocess.CalledProcessError as e:
						print(e.output)		
				except subprocess.CalledProcessError as e:
					print(e.output)				
			except subprocess.CalledProcessError as e:
				print(e.output)	
		except subprocess.CalledProcessError as e:
			print(e.output)		
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
				print(e.output)	
		except subprocess.CalledProcessError as e:
			print(e.output)		
	else: 
		print("Please select a correct mode {single, 1x4}")



create_photos_dir()
wait_for_button_press()

create_photo_montage(fonts_list[0],text, '1x4')


GPIO.cleanup()
