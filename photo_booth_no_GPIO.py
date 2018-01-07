#!/usr/bin/python

import  time, os, subprocess

if 1==1:
  if 1==1:
    snap = 0
    while snap < 4:
      print("pose!")
      time.sleep(3.5)
      print("SNAP")
      gpout = subprocess.check_output("gphoto2 --capture-image-and-download --filename /home/pi/photobooth_images/photobooth%H%M%S.jpg", stderr=subprocess.STDOUT, shell=True)
      print(gpout)
      if "ERROR" not in gpout: 
        snap += 1
      time.sleep(0.5)
    print("please wait while your photos print...")
    # build image and send to printer
    subprocess.call("sudo /home/pi/RPi_photobooth/assemble_and_print", shell=True)
