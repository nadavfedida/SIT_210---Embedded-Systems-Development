import cv2
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
from datetime import date, datetime
from gpiozero import LED 
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from gpiozero import DistanceSensor
import csv

#Global variable MQTT status
flag_conencted = 0

#Distance finder pins
sensor = DistanceSensor(echo=24, trigger=23 ) 

led = LED(17)
AllowedNames = ['nadav', 'will', 'michael', 'tom']

def on_connect(client, userdata, flags, rc):
	global flag_conencted
	flag_conencted = 1

def on_disconnect(client, userdata, rc):
	global flag_conencted
	flag_conencted = 0

try:
	if __name__ == "__main__":
		while True:
			if (flag_conencted == 0):
				client = mqtt.Client()
				client.on_connect = on_connect
				client.on_disconnect = on_disconnect
				client.connect("test.mosquitto.org", 1883, 60)
				client.loop_start()
			Dist= sensor.value
			printDist = f'Distance {Dist :1.2f} M'
			print(printDist)
			
			if Dist < 0.20:
				# set up camera object called Cap
				#which we will use to find OpenCV
				#cam settings
				cap = cv2.VideoCapture(0)
				cap.set(3,640)
				cap.set(4,480)
				# QR code detection Method
				detector = cv2.QRCodeDetector()
				
				
				# Below is the method to get a image of the QR code
				_, img = cap.read()
				data, bbox, _ = detector.detectAndDecode(img)
				if data:
					if data in AllowedNames:
						led.on()
						publish.single("SIT210_nadav", data , 
						hostname="test.mosquitto.org")
						print("Access granted to: ", data)
						time.sleep(1)
						led.off()
						cap.release()
					
						with open('Database.csv', mode='a') as csvfile:
						csvfileWriter = csv.writer(csvfile, delimiter=',', 
						quotechar='"', quoting=csv.QUOTE_ALL)
						csvfileWriter.writerow([data , datetime.today().
						strftime('%Y-%m-%d  %H:%M:%S')])    
					
			#cv2.imshow("code detector", img)
			cv2.waitKey(1)
			cap.release()
			time.sleep(0.5)
			print("Nothing detected")
			time.sleep(2)

except KeyboardInterrupt:
	print("exit")

except cv2.error as error:
	print(error)
	publish.single("SIT210_nadav", "Camera Failed" ,
	hostname="test.mosquitto.org")

finally:
	client.loop_stop()
	GPIO.cleanup()