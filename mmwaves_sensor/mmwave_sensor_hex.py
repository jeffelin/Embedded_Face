##Code snippets of initial testing case to see whether or not mmwave is connected to serial

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


###

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

#############

import serial
import binascii
import time
import mm_wave as mm_wave
from mm_wave import *

def send_hex_string(serial_port, hex_string):
    hex_bytes = binascii.unhexlify(hex_string)
    print(f"Sending hex: {hex_string}")  # Debug: show what is being sent
    serial_port.write(hex_bytes)
    print("Data sent successfully.")  # Confirm data was sent

def read_serial_data(serial_port):
    print("Ready to receive data...")
    while True:
        if serial_port.in_waiting > 0:
            first_byte = serial_port.read()
            print(f"First byte {first_byte.hex()}")
            if first_byte == MESSAGE_HEADER_2:
                #if serial_port.read() == MESSAGE_HEADER_2:
                    data = 0
                    while data != MESSAGE_END_2:
                        #
                        data = serial_port.read()
                        print(f"{data.hex()}")
                    
            #data = serial_port.readline().decode('utf-8', errors='ignore').strip()
            #if data:
            #    print(f"Received: {data}")  # Debug: print received data
            #else:
            #    print("Received data, but it's empty.")
        else:
            print("No data waiting.")
        time.sleep(1)  # Pause briefly, adjust as necessary for your context

if __name__ == "__main__":
    ser = serial.Serial('/dev/serial0', baudrate = 9600,bytesize = serial.EIGHTBITS, timeout = None, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
    print("Serial port opened successfully.")
    

    #query_firmware_hex = "535902A400010F625443"
    #hex_to_send = "FDFCFBFA0800FF0100000100400004030201"
    #send_hex_string(ser, hex_to_send)
    

    written = ser.write(FIRMWARE_QUERY)
    print(f"wrote {written} bytes") 
    try:
        read_serial_data(ser)
    except KeyboardInterrupt:
        print("Stopped by User")
    finally:
        ser.close()
