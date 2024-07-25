import serial
from serial import tools
from serial.tools import list_ports
import binascii
import time
import spy_mmWavesensor.mm_wave as mm_wave
from spy_mmWavesensor.mm_wave import *

# Constants from the manual
FRAME_HEADER = b'\x53\x59'
FRAME_END = b'\x54\x43'

def make_data_frame(command_data):
    header = FRAME_HEADER
    partial = header + bytes(command_data)
    checksum = bytes([sum(partial) & 0xFF])
    return partial + checksum + FRAME_END

# Function to send command and read response
def send_command(ser,command):
    ser.write(command)
    ser.flush()

def read_data(ser):
    response = b''
    while True:
        if ser.in_waiting > 0:
            byte = ser.read(1)
            response += byte
            print(f'partialresponse: {response}')
            if response.endswith(FRAME_END):
                break

    print(f"Received: {response.hex()}")
    return response

    

def send_command_and_read(ser, command):
    # Send command
    send_command(ser,command)
  
    # print(f"Sent: {command.hex()}")
    # print("Ready to receive data...")
    # Read response
    return read_data(ser)
   

# Heartbeat packet query
def heartbeat_query(ser):
    command = make_data_frame(b'\x01\x01\x00\x01\x0F')
    return send_command_and_read(ser, command)

# Module Reset
def module_reset(ser):
    command = make_data_frame(b'\x01\x02\x00\x01\x0F')
    send_command(ser, command)

# Firmware version query
def query_firmware_version(ser):
    command = make_data_frame(b'\x02\xA4\x00\x01\x0F')
    return send_command_and_read(ser, command)

# Set scene mode
def set_scene_mode(ser, mode):
    if mode not in range(1, 5):
        raise ValueError("Mode must be between 1 and 4")
    command = make_data_frame(b'\x05\x07\x00\x01' + bytes([mode]))
    return send_command_and_read(ser, command)

# Set sensitivity
def set_sensitivity(ser, level):
    if level not in range(1, 4):
        raise ValueError("Sensitivity level must be between 1 and 3")
    command = make_data_frame(b'\x05\x08\x00\x01' + bytes([level]))
    return send_command_and_read(ser, command)

# Query person detection status
def query_person_detection(ser):
    command = make_data_frame(b'\x80\x81\x00\x01\x0F')
    response = send_command_and_read(ser, command)
    
    print("Detailed response:")
    for i, byte in enumerate(response):
        print(f"Byte {i}: {byte:02x}")
    
    if len(response) >= 10:  # Ensure the response is long enough
        status = response[7]
        if status == 0x00:
            return "Unoccupied"
        elif status == 0x01:
            return "Occupied"
        else:
            return f"Unknown status: {status}"
    else:
        return "Invalid response"

def query_motion_information(ser):
    command = make_data_frame(b'\x80\x82\x00\x01\x0F')
    response = send_command_and_read(ser, command)
    
    print("Detailed motion information response:")
    for i, byte in enumerate(response):
        print(f"Byte {i}: {byte:02x}")
    
    if len(response) >= 10:  # Ensure the response is long enough
        status = response[7]
        if status == 0x00:
            return "None (No motion detected)"
        elif status == 0x01:
            return "Motionless (Person present but not moving)"
        elif status == 0x02:
            return "Active (Motion detected)"
        else:
            return f"Unknown motion status: {status}"
    else:
        return "Invalid response"

if __name__ == "__main__":


    ser = serial.Serial('/dev/serial0', baudrate=115200, bytesize=serial.EIGHTBITS, timeout=1, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
    print("Serial port opened successfully.")

    try:
        # Perform functions 
        # Perform heartbeat query
        # heartbeat_response = heartbeat_query(ser)
        # print("Heartbeat query response:", heartbeat_response.hex())
        scene_response = set_scene_mode(ser, 1)
        print("Scene mode set response:", scene_response.hex())

        sensitivity_response = set_sensitivity(ser, 2)
        print("Sensitivity set response:", sensitivity_response.hex())

        detection_status = query_person_detection(ser)
        print("Person detection ery_person_detstatus:", detection_status)
        
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
