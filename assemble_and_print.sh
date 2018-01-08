#!/bin/bash
temp_photo_dir=~/Pictures/temp

# resize the picture(s)
mogrify -resize 968x648 $temp_photo_dir/*.jpg

# assemble montage
montage $temp_photo_dir/*.jpg -tile 2x2 -geometry +10+10 $temp_photo_dir/temp_montage2.jpg
montage $temp_photo_dir/temp_montage2.jpg /home/pi/photobooth_label.jpg -tile 2x1 -geometry +5+5 $temp_photo_dir/temp_montage3.jpg


# send print job
lp $temp_photo_dir/temp_montage3.jpg

# add timestamp, copy to photo_directory
suffix=$(%H%M%S)
cp $temp_photo_dir/temp_montage3.jpg /home/pi/PB_archive/PB_${suffix}.jpg
rm $temp_photo_dir/*.jpg

