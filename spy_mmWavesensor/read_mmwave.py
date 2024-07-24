import serial
import time

ser = serial.Serial ('/dev/ttyS0' , 115200, timeout=1)
time.sleep(2) 

def read_data(): 
	if ser.in_waiting >0: 
		data = ser.readline().decode('utf-8').rstrip() 
		print(f"Receive data: {data}")


try:
	while True: 
		read_data() 
except KeyboardInterrupt:
	ser.close()
	print("Serial connection closed.")  
