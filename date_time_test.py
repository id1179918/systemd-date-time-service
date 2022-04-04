from datetime import date, datetime
import os

os.umask(0)

today = date.today()
time = datetime.now()

try:
	with open(os.open('/home/pi/gen2-software-package/gen2-readout/ThomasTest/TEST.txt', os.O_CREAT | os.O_WRONLY, 0o777), 'w') as file:
		file.write("--------------------- " + today.strftime("%d/%m/%Y") + " " + time.strftime("%H:%M:%S") + "---------------------\n")
except FileNotFoundError:
	print("--------------------- " + FileNotFoundError  + "  ---------------------")