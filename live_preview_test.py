import  locale, time, os, subprocess, errno
try:
	command="mkfifo fifo.mjpg"
	subprocess.check_output("%s"% command, shell=True)
except subprocess.CalledProcessError as e:
	print(e.output)	


try:
	command="gphoto2 --capture-movie=50 --stdout> fifo.mjpg & omxplayer fifo.mjpg --live"
	subprocess.check_output("%s"% command, shell=True)
except subprocess.CalledProcessError as e:
	print(e.output)	


