import time
import serial
import binascii
import time
import mm_wave as mm_wave
from mm_wave import *


##Initial code courtesy of Andrew McGuire @https://echogatetech.com/

########definitions:
MESSAGE_HEADER_1 = bytes.fromhex('53')
MESSAGE_HEADER_2 = bytes.fromhex('59')
MESSAGE_END_1 = bytes.fromhex('54')
MESSAGE_END_2 = bytes.fromhex('43')
HUMANSTATUS = bytes.fromhex('80')

HUMANSTATUS = bytes.fromhex('80')       #Human Presence Information
HUMANEXIST = bytes.fromhex('01')       #Presence of the human body
HUMANMOVE = bytes.fromhex('02')       #Human movement information
HUMANSIGN = bytes.fromhex('03')       #Body Signs Parameters
HUMANDIRECT = bytes.fromhex('0B')       #Human movement trends

SOMEBODY = bytes.fromhex('01')       #Somebody move
NOBODY = bytes.fromhex('00')       #No one here

NONE = bytes.fromhex('00')
SOMEBODY_STOP = bytes.fromhex('01')       #Somebody stop
SOMEBODY_MOVE = bytes.fromhex('02')       #Somebody move

CA_CLOSE = bytes.fromhex('01')       #Someone approaches
CA_AWAY = bytes.fromhex('02')       #Some people stay away


DETAILSTATUS = bytes.fromhex('08')       #Underlying parameters of the human state
DETAILINFO = bytes.fromhex('01')       #Detailed data on the state of human movement
DETAILDIRECT = bytes.fromhex('06')       #Human movement trends
DETAILSIGN = bytes.fromhex('07')       #Body Signs Parameters


SOMEONE = bytes.fromhex('01')       #There are people
NOONE = bytes.fromhex('02')       #No one
NOTHING = bytes.fromhex('03')       #No message
SOMEONE_STOP = bytes.fromhex('04')       #Somebody stop
SOMEONE_MOVE = bytes.fromhex('05')       #Somebody move
HUMANPARA = bytes.fromhex('06')       #Body Signs Parameters
SOMEONE_CLOSE = bytes.fromhex('07')       #Someone approaches
SOMEONE_AWAY = bytes.fromhex('08')       #Some people stay away
DETAILMESSAGE = bytes.fromhex('09')       #Underlying parameters of the human state

RESET_FRAME_LENGTH = 10       #Reset data frame length

SEEED_HUMAN_UNIT = 0.5     #Calculate unit steps

RESET_FRAME_STRINGS = ["53", "59", "01", "02", "00", "01", "0F", "BF", "54", "43"]
RESET_FRAME = bytes.fromhex(''.join(RESET_FRAME_STRINGS))

#Various commands that can be moved around at discretion: 

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



#Dataframes for sending and receiving 
def make_data_frame(commandData):
    header_data = ["53","59"]
    partial = bytes.fromhex(''.join(header_data + commandData))

    checksum = b'%02X' % (sum(partial) & 0xFF)
    tail_data = ["54","43"]
    return partial + checksum + bytes.fromhex(''.join(tail_data))
    


INITIALIZE_STATUS = make_data_frame(["05","81","00","00","0F"])
FIRMWARE_QUERY = make_data_frame(["02","A4","00","00","01","0F"])


class HumanStatic():
    def __init__(self):
        pass
