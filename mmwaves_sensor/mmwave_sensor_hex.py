import serial
import time

def hex_to_bytes(hex_str):
	return bytes.fromhex(hex_str)

ser = serial.Serial(' /dev/ttyAMA1', 115200, timeout=1)
time.sleep(2)

init_command = '55AAFF00'
ser.write(hex_to_bytes(init_command))

def read_data():
	while True:
		if ser.in_waiting > 0:
			data = ser.read(ser.in_waiting)
			print(f"Received data: {data.hex()}")

try:
	read_data()
except KeyboardInterrupt:
	ser.close()
	print("Serial connection closed.")  
