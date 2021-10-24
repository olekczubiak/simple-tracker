import serial
import time
import string
import pynmea2
import datetime
import saver
import requester

TODAY_DATE = str(datetime.datetime.now())
URL = "https://tracker.toadres.pl/add"

def print_data(date, lat, lng, speed):
	print("Date=\x1b[2;34;40m" + date + "\x1b[0m and Latitude=\x1b[3;31;40m" + str(lat) + "\x1b[0m and Longitude=\x1b[3;31;40m" + str(lng) + "\x1b[0m Speed=\x1b[1;33;40m" + str(speed) + "\x1b[0m")

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
		requester.send_data(date[11:19], lat, lng)
		print "\n"
		print_data(date, lat, lng, speed)