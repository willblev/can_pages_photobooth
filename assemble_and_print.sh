#!/bin/bash
temp_photo_dir=/home/pi/Pictures/temp
photo_label_text="Sal + Berta January 9 2018"

#replace spaces with unicode spaces (need to do this for imagemagick label to work)
photo_label_text=$(sed 's| |\\u2002|g' <<< $photo_label_text)
# create the text strip
convert -background white -size 1100x110 -fill black -font FreeSerif \
          -gravity center  label:$(echo -e "$photo_label_text") \
          -rotate 270 \
         $temp_photo_dir/photobooth_label.jpg 
         
### resize the picture(s) that were uploaded from the camera
#mogrify -resize 968x648 $temp_photo_dir/snap*.jpg

### assemble montage
#montage $temp_photo_dir/*.jpg -tile 2x2 -geometry +10+10 $temp_photo_dir/temp_montage2.jpg
#montage $temp_photo_dir/temp_montage2.jpg $temp_photo_dir/photobooth_label.jpg -tile 2x1 -geometry +5+5 $temp_photo_dir/temp_montage3.jpg


# send print job
#lp $temp_photo_dir/temp_montage3.jpg

# add timestamp, copy to photo_directory
#suffix=$(date + %H%M%S)
#cp $temp_photo_dir/temp_montage3.jpg /home/pi/PB_archive/PB_${suffix}.jpg
#rm $temp_photo_dir/*.jpg

