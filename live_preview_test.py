import  locale, time, os, subprocess, errno
import RPi.GPIO as GPIO


gpio_pin_number=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING)
    
    command0="rm fifo.mjpg"
    subprocess.check_output("%s"% command0, shell=True)    
    command1="mkfifo fifo.mjpg"
    subprocess.check_output("%s"% command1, shell=True)
    command2="gphoto2 --capture-movie=60 --stdout> fifo.mjpg & omxplayer fifo.mjpg --live"
    subprocess.check_output("%s"% command2, shell=True)
except:
	pass

GPIO.cleanup()
