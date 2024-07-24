import time
import serial
import binascii
import time
import spy_mmWavesensor.mm_wave as mm_wave
from spy_mmWavesensor.mm_wave import *



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



def make_data_frame(commandData):
    header_data = ["53","59"]
    partial = bytes.fromhex(''.join(header_data + commandData))

    checksum = b'%02X' % (sum(partial) & 0xFF)
    tail_data = ["54","43"]
    return partial + checksum + bytes.fromhex(''.join(tail_data))
    


INITIALIZE_STATUS = make_data_frame(["05","81","00","00","0F"])
FIRMWARE_QUERY = make_data_frame(["02","A4","00","00","01","0F"])





if __name__ == "__main__":


    ser = serial.Serial('/dev/serial0', baudrate=115200, bytesize=serial.EIGHTBITS, timeout=1, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    print("Serial port opened successfully.")

    try:
        # Perform functions 
        # Perform heartbeat query
        # heartbeat_response = heartbeat_query(ser)
        # print("Heartbeat query response:", heartbeat_response.hex())
        # scene_response = set_scene_mode(ser, 1)
        # print("Scene mode set response:", scene_response.hex())

        # sensitivity_response = set_sensitivity(ser, 2)
        # print("Sensitivity set response:", sensitivity_response.hex())

        # detection_status = query_person_detection(ser)
        # print("Person detection ery_person_detstatus:", detection_status)
        
        while True:
            value = read_data(ser)
            print(value)
        # Query person motion status 
        # motion_status = query_motion_information(ser)
        # print("Motion status:", motion_status)
        # while True:
        #     print("Read: ", read_data(ser))
        # # Set scene mode (e.g., to Living Room)
       

        # # Set sensitivity (e.g., to level 2)
     

        # You can add more commands here as needed
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ser.close()
        print("Serial port closed.")

# class HumanStatic():
#     def __init__(self):
#         pass
