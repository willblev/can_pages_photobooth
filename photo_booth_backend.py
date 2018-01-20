#!/usr/bin/python
#Creating Saved Options

#Saved options are supported in CUPS through printer instances. Printer instances are, as their name implies, copies of a printer that have certain options associated with them. Use the lpoptions command to create a printer instance:

#lpoptions -p printer/instance -o name=value ...
#The -p printer/instance option provides the name of the instance, which is always the printer name, a slash, and the instance name which can contain any printable characters except space and slash. The remaining options are then associated with the instance instead of the main queue. For example, the following command creates a duplex instance of the LaserJet queue:

#lpoptions -p LaserJet/duplex -o sides=two-sided-long-edge
#Instances do not inherit lpoptions from the main queue.


import  locale, time, os, subprocess, errno


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
	new_file_name=''
	if mode=="2x2":		
		try:         
			command="mogrify -resize 968x648 %s/*.jpg" % (temp_photos_directory)
			print(command)
			subprocess.check_output("%s" % command, shell=True)
			try:         
				command="montage %s/*.jpg -tile 2x2 -geometry +10+10 %s/temp_montage2.jpg" % (temp_photos_directory,temp_photos_directory)
				print(command)
				subprocess.check_output("%s" % command, shell=True)
				try:         
					command="convert -background white -size 1100x110 -fill black -font goingtodogreatthings -gravity center  label:'%s' -rotate 270 %s/photobooth_label.jpg" % (text,temp_photos_directory)
					print(command)
					subprocess.check_output("%s" % command, shell=True)
					try:         
						command="montage %s/temp_montage2.jpg %s/photobooth_label.jpg -tile 2x1 -geometry +5+5 %s/temp_montage_final.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
						print(command)
						subprocess.check_output("%s" % command, shell=True)
						try:         
							new_file_name="%s/Can_Pages_Photobooth_2x2_%s:%s:%s.jpg" %(photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
							command="cp %s/temp_montage_final.jpg %s" % (temp_photos_directory,new_file_name)
							print(command)
							subprocess.check_output("%s" % command, shell=True)
							try:         
								command="lp %s" % (new_file_name)
								print(command)
								subprocess.check_output("%s" % command, shell=True)
								try:         
									command="rm %s/*.jpg" % (temp_photos_directory)
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
	elif mode=="1x4":
		try:         
			command="mogrify -resize 484x324 %s/*.jpg" % (temp_photos_directory)
			print(command)
			subprocess.check_output("%s" % command, shell=True)
			try:         
				command="montage %s/*.jpg -tile 1x4 -geometry +5+5 %s/temp_montage2.jpg" % (temp_photos_directory,temp_photos_directory)
				print(command)
				subprocess.check_output("%s" % command, shell=True)
				try:         
					command="convert -background white -size 1100x80 -fill black -font Piboto-Bold -gravity center  label:'%s' -rotate 270 %s/photobooth_label.jpg" % (text,temp_photos_directory)
					print(command)
					subprocess.check_output("%s" % command, shell=True)
					try:         
						command="montage %s/temp_montage2.jpg %s/photobooth_label.jpg -tile 2x1 -geometry +5+5 %s/temp_montage3.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
						print(command)
						subprocess.check_output("%s" % command, shell=True)
						try:         
							command="montage %s/temp_montage3.jpg %s/temp_montage3.jpg -tile 2x1 -geometry +5+5 %s/temp_montage_final.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
							print(command)
							subprocess.check_output("%s" % command, shell=True)
							try:         
								new_file_name="%s/Can_Pages_Photobooth_1x4_%s:%s:%s.jpg" %(photos_directory,time.strftime("%H"),time.strftime("%M"),time.strftime("%S"))
								command="cp %s/temp_montage_final.jpg %s" % (temp_photos_directory,new_file_name)
								print(command)
								subprocess.check_output("%s" % command, shell=True)
								try:         
									command="lp %s" % (new_file_name)
									print(command)
									subprocess.check_output("%s" % command, shell=True)
									try:         
										#command="rm %s/*.jpg" % (temp_photos_directory)
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


def send_image_to_printer(file_name):
	try:         
		command="lp %s" % (file_name)
		print(command)
		subprocess.check_output("%s" % command, shell=True)
	except subprocess.CalledProcessError as e:
		print e.output			

#def clear_temp_directory():
	#try:         
		#command="rm %s/*.jpg" % (temp_photos_directory)
		#print(command)
		#subprocess.check_output("%s" % command, shell=True)
	#except subprocess.CalledProcessError as e:
		#print e.output			

		
		
########  Get input for names and language from a configuration file
novios=Novios(['Will','Katie'], 'eng')

######## Create directories
scripts_directory="/home/pi/can_pages_photobooth"
photos_directory="/home/pi/Pictures/"+time.strftime("%d-%m-%Y")+"_"+novios.names[0]+"_"+novios.names[1]
temp_photos_directory="/home/pi/Pictures/temp"

if not os.path.exists(photos_directory):
	os.makedirs(photos_directory)
	print("Created "+photos_directory)

capture_pictures("2x2")
create_photo_montage(novios.photo_string(' & '), '2x2')
