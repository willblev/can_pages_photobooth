import  locale, time, os, subprocess, errno,pygame
import RPi.GPIO as GPIO

### Setup GPIO
gpio_pin_number=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)


########  Define global variables


mode='5x15'
language='ESP'
text=''
font=''
language_dict={		   # dictionary to set the language/locale for each event	
				'ENG':'en_US.UTF-8', 
				'ESP':'es_ES.UTF-8', 
				'CAT':'ca_ES.UTF-8'
				}
prompt1_text_dict={
				'ENG':'Press the button to start', 
				'ESP':'Presiona el botón para comenzar', 
				'CAT':'Premeu el botó per començar'
				}
prompt2_text_dict={
				'ENG':'Get ready!', 
				'ESP':'¡Preparate!', 
				'CAT':"Prepara't!"
				}
prompt3_text_dict={
				'ENG':'Get ready!', 
				'ESP':'¡Preparate!', 
				'CAT':"Prepara't!"
				}
prompt4_text_dict={
				'ENG':'Processing photos...', 
				'ESP':'Procesando las fotos...', 
				'CAT':"Processant les fotos..."
				}
prompt5_text_dict={
				'ENG':'Printing...', 
				'ESP':'Imprimiendo...', 
				'CAT':"Imprimint..."
				}
prompt6_text_dict={
				'ENG':'Please take your photo', 
				'ESP':'Por favor recoja su foto', 
				'CAT':"Tria la teva foto"
				}

# directories
scripts_directory="/home/pi/can_pages_photobooth"
photos_directory="/home/pi/Pictures/"+time.strftime("%d-%m-%Y")
temp_photos_directory="/home/pi/Pictures/temp"

#pre-formatted text strings
date_text_string="%s %s %s" % (time.strftime("%d").lstrip("0"),time.strftime("%B"),time.strftime("%Y"))	
date_number_string="%s %s %s" % (time.strftime("%d").lstrip("0"),time.strftime("%B"),time.strftime("%Y"))	

###### Define functions

def wait_for_button_press():
	"""
	A function which listens for button presses, then begins the photobooth series of events"
	"""
	global mode
	global language
	try:
		GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
		prompt_screen(prompt2_text_dict[language],120)
		command0="rm fifo.mjpg"
		subprocess.check_output("%s"% command0, shell=True)    
		command1="mkfifo fifo.mjpg"
		subprocess.check_output("%s"% command1, shell=True)
		command2="gphoto2 --capture-movie=60 --stdout> fifo.mjpg & omxplayer fifo.mjpg --live"
		subprocess.check_output("%s"% command2, shell=True)
		prompt_screen(prompt3_text_dict[language],120)
		time.sleep(1)
		capture_pictures()
	except:
		pass

def import_config_file(config_file):
	"""
	A function which opens a configuration file and imports the settings
	"""
	global mode
	global language
	global text
	global font
	locale.setlocale(locale.LC_ALL, language_dict[language]) # set the preferred language (i.e. locale) for the event
	with open(config_file,'r') as configuration:
		for line in configuration:
			if line.startswith('LANGUAGE:'):
				language=line.split(':')[1].rstrip()
			elif line.startswith('FIRSTLINE:'):
				firstline=line.lstrip('FIRSTLINE:')
			elif line.startswith('SECONDLINE:'):
				secondline=line.lstrip('SECONDLINE:')
			elif line.startswith('FONT:'):
				font=line.split(':')[1].rstrip()
			elif line.startswith('MODE:'):
				mode=line.split(':')[1].rstrip()
		text="%s\n%s"%(firstline,secondline)
	locale.setlocale(locale.LC_ALL, language_dict[language]) # set the preferred language (i.e. locale) for the event
def clear_temp_directory():
	"""
	A function which deletes all the files in the temp directory
	"""
	try:
		command="rm %s/*"%(temp_photos_directory)
		subprocess.check_output("%s"% command, shell=True)
	except subprocess.CalledProcessError as e:
		print(e.output)	

	
def capture_pictures():
	"""
	A function which calls gphoto2 to capture the images from the DSLR
	"""
	global mode
	global language
	clear_temp_directory()
	
	if mode=="5x15":
		num_captures=0	
		while num_captures<4:
			for x in range(3,0,-1):
				print("Taking picture in %s" % x)
				prompt_screen(str(x),600)
				time.sleep(1)
			try:
				command="gphoto2 --capture-image-and-download --filename %s/capture_%s:%s:%s.jpg"%(temp_photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
				subprocess.check_output("%s"% command, shell=True)
				num_captures+=1
			except subprocess.CalledProcessError as e:
				print(e.output)	
	elif mode=="10x15":
		try:
			command="gphoto2 --capture-image-and-download --filename %s/capture_%s:%s:%s.jpg"%(temp_photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
			subprocess.check_output("%s"% command, shell=True)
		except subprocess.CalledProcessError as e:
			print(e.output)
	else: 
		pass

def create_photos_dir():
	photos_directory="/home/pi/Pictures/"+time.strftime("%d-%m-%Y")
	if not os.path.exists(photos_directory):
		try:
			os.makedirs(photos_directory)
			print("Created "+photos_directory)
		except subprocess.CalledProcessError as e:
			print(e.output)

			
def create_photo_montage(font,text,mode):
	"""
	A function which takes the captured images and creates a file (single shot or 1x4 photo strip) in the appropriate directory
	"""
	global language
	prompt_screen(prompt4_text_dict[language],120)					
	if mode=="5x15":
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
									subprocess.check_output("%s" % command, shell=True)	
									prompt_screen(prompt5_text_dict[language],80)					
						
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
	elif mode=="10x15":
		try:         
			new_file_name="%s/Can_Pages_Photobooth_%s:%s:%s.jpg" %(photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
			command="cp %s/capture*.jpg %s" % (temp_photos_directory,new_file_name)
			print(command)
			subprocess.check_output("%s" % command, shell=True)
			try:         
				command="lp %s" % (new_file_name)
				print(command)
				subprocess.check_output("%s" % command, shell=True)
				prompt_screen(prompt5_text_dict[language],80)					

				
			except subprocess.CalledProcessError as e:
				print(e.output)	
		except subprocess.CalledProcessError as e:
			print(e.output)		
	else: 
		print("Please select a correct mode {5x15, 10x15}")



def prompt_screen(inputText,fontSize):
	pygame.font.init()
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	TURQUOISE=(117, 239, 217)
	PINK=(255, 127, 229)
	pygame.display.init()
	size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
	screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
	screen.fill(BLACK)        
	pygame.display.update()

	font = pygame.font.SysFont("DKCosmoStitch", fontSize)
	text_color = TURQUOISE
	led_state = False
	screen.fill(BLACK)
	text = font.render(inputText, 1, text_color)
	textpos = text.get_rect()
	textpos.center = (pygame.display.Info().current_w/2, pygame.display.Info().current_h/2)
	screen.blit(text, textpos)
	pygame.display.flip()



import_config_file("/home/pi/can_pages_photobooth/config.txt")
create_photos_dir()
prompt_screen(prompt1_text_dict[language],80)
wait_for_button_press()
create_photo_montage(font,text, mode)
time.sleep(10)
prompt_screen(prompt6_text_dict[language])

GPIO.cleanup()
