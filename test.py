import  locale, time, os, subprocess, errno
temp_photos_directory="/home/william/github/can_pages_photobooth/example_images" 
font='goingtodogreatthings'
text="Katie + Will 4 evaaaa!"


## copy photos from fresh to example
command="cp  /home/william/github/can_pages_photobooth/example_images/fresh/capture* /home/william/github/can_pages_photobooth/example_images/"  
print(command)
subprocess.check_output("%s" % command, shell=True)
## crop
command="mogrify -gravity Center -crop '70x80%+0+0'  /home/william/github/can_pages_photobooth/example_images/capture*.jpg"  
print(command)
subprocess.check_output("%s" % command, shell=True)

#stack and add white border to each photo
command="montage %s/capture*.jpg -tile 1x4 -geometry +5+5 %s/temp_montage2.jpg" % (temp_photos_directory,temp_photos_directory)
print(command)
subprocess.check_output("%s" % command, shell=True)

## create label
command="convert -background white -size 1100x80 -fill black -font '%s' -gravity center  label:'%s' -rotate 270 %s/photobooth_label.jpg" % (font, text, temp_photos_directory)
print(command)
subprocess.check_output("%s" % command, shell=True)

## add label to 4 stacked photos
command="montage %s/temp_montage2.jpg %s/photobooth_label.jpg -tile 2x1 -geometry +5+5 %s/temp_montage3.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
print(command)
subprocess.check_output("%s" % command, shell=True)

## copy strip to photo directory (final image)


## double photos for printing (need to add white strip in middle!)
command="montage %s/temp_montage3.jpg %s/temp_montage3.jpg -tile 1x2 -geometry +5+5 -rotate 270 %s/temp_montage_final.jpg" % (temp_photos_directory,temp_photos_directory,temp_photos_directory)
print(command)
subprocess.check_output("%s" % command, shell=True)
