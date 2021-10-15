import serial
import time
import string
import pynmea2
import datetime
import saver

TODAY_DATE = str(datetime.datetime.now())

while True:
	port="/dev/ttyAMA0"
	ser=serial.Serial(port, baudrate=9600, timeout=0.5)
	dataout = pynmea2.NMEAStreamReader()
	newdata=ser.readline()

	if newdata[0:6] == "$GPRMC":
		newmsg=pynmea2.parse(newdata)
		lat=newmsg.latitude
		lng=newmsg.longitude
		date = str(datetime.datetime.now())
		gps = "Date= " + date + " and Latitude=" + str(lat) + " and Longitude=" + str(lng)
		saver.save_to_file(TODAY_DATE[:10], saver.data_to_save(date[11:19], lat, lng))
		print(gps)