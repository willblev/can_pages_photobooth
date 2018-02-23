import os, subprocess
temp_photos_directory="/home/william/Pictures/font_list"
textString="Can Pagès 1-2-3456 Novio + Novia"
font_list=[
 "Adventure",
 "Adventure-Outline",
 "Alba",
 "Alba-Super",
 "AlexandriaFLF",
 "Allura",
 "Always-In-My-Heart",
 "Another-Typewriter",
 "Austie-Bost-You-Wear-Flowers-Hollow",
 "Bakery",
 "BehrensSchrift-Normalreduced",
 "Black-Rose",
 "Bookman-Demi",
 "Chocolate-Covered-Raindrops",
 "Clicker-Script",
 "CoalhandLukeTRIAL",
 "DancingScript-Bold",
 "DKCosmoStitch",
 "Give-It-Your-Heart",
 "goingtodogreatthings",
 "Impact-Label",
 "Janda-Scrapgirl-Dots",
 "Journey-to-Thailand",
 "justbeautifulsimplicity",
 "KG-A-Little-Swag",
 "Kingthings-Extortion",
 "Lato-Regular",
 "Life-is-goofy",
 "Long-distance-call",
 "Montserrat-Regular",
 "Moon-Flower",
 "Moon-Flower-Bold",
 "Mrs.-Monster-Regular",
 "orange-juice",
 "Playfair-Display-Bold",
 "Prisma",
 "Reality-Sunday",
 "Royal-Acidbath-Outline",
 "SF-Balloons",
 "Shorelines-Script-Bold",
 "Silk-Remington-SBold",
 "Videophreak",
 "YouMurderer-BB"
]

# command="rm %s/*.jpg" % (temp_photos_directory)
# subprocess.check_output("%s" % command, shell=True)

for selectedFont in font_list:
	command1="convert -background white -size 500x30 -fill black -font '%s' -gravity center  label:'%s: %s'  %s/%s.jpg" % (selectedFont,selectedFont, textString, temp_photos_directory,selectedFont)
	subprocess.check_output("%s" % command1, shell=True)

command="montage %s/*.jpg -tile 1x43 -geometry +2+2 %s/text_list.jpg" % (temp_photos_directory,temp_photos_directory)
subprocess.check_output("%s" % command, shell=True)

