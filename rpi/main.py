import serial
import time
import string
import pynmea2
import datetime
import saver
import requester
import schemas

TODAY_DATE = str(datetime.datetime.now())
URL = "https://tracker.toadres.pl/api/add"
ACCESS_TOKEN = '48cdcb6f7300a42157e9a78db71b7cc103609b7584dcffc12ca20605110b8e67'

def print_data(date, lat, lng, speed):
	print("Date=\x1b[2;34;40m" + date + "\x1b[0m and Latitude=\x1b[3;31;40m" + str(lat) + "\x1b[0m and Longitude=\x1b[3;31;40m" + str(lng) + "\x1b[0m Speed=\x1b[1;33;40m" + str(speed) + "\x1b[0m")

def single_send():
	requester.send_data(URL, ACCESS_TOKEN, TODAY_DATE[:10], "XX:XX:XX", 0 , 0)
	while True:
		port="/dev/ttyAMA0"
		ser=serial.Serial(port, baudrate=9600, timeout=0.5)
		dataout = pynmea2.NMEAStreamReader()
		newdata=ser.readline()
		if newdata[0:6] == "$GPRMC":
			newmsg=pynmea2.parse(newdata)
			lat=newmsg.latitude
			lng=newmsg.longitude
			speed = newmsg.spd_over_grnd
			date = str(datetime.datetime.now())

			saver.save_to_file(TODAY_DATE[:10], saver.data_to_save(date[11:19], lat, lng))
			if speed == None:
				pass
			else:
				requester.send_data(URL, ACCESS_TOKEN, TODAY_DATE[:10], date[11:19], lat, lng)
			print "\n"
			print_data(date, lat, lng, speed)


def sixty_send():
	requester.send_data(URL, ACCESS_TOKEN, TODAY_DATE[:10], "XX:XX:XX", 0 , 0)
	n = 0
	my_fake_db = []
	while True:
		port="/dev/ttyAMA0"
		ser=serial.Serial(port, baudrate=9600, timeout=0.5)
		dataout = pynmea2.NMEAStreamReader()
		newdata=ser.readline()
		if newdata[0:6] == "$GPRMC":
			newmsg=pynmea2.parse(newdata)
			lat=newmsg.latitude
			lng=newmsg.longitude
			speed = newmsg.spd_over_grnd
			date = str(datetime.datetime.now())

			saver.save_to_file(TODAY_DATE[:10], saver.data_to_save(date[11:19], lat, lng))
			if speed == None:
				pass
			else:
				my_fake_db.append(schemas.my_dict(TODAY_DATE[:10], date[11:19], lat, lng))
				n += 1
				if n >= 60:
					n = 0
					requester.send_more_data(URL + "/more", ACCESS_TOKEN, my_fake_db)
					my_fake_db = []
				# requester.send_data(URL, ACCESS_TOKEN, TODAY_DATE[:10], date[11:19], lat, lng)
			print "\n"
			print_data(date, lat, lng, speed)

print "Turn on interactive python with -i flag (python -i main.py)"
print "single_send() - to single start"
print "sixty_send() - to multiply start"