# # hex that worked online FDFCFBFA0800120000006400000004030201

######################################################################
#Original code:

# import serial
# import binascii
# import time
# import mm_wave
# from mm_wave import *

# def send_hex_string(serial_port, hex_string):
#     hex_bytes = binascii.unhexlify(hex_string)
#     print(f"Sending hex: {hex_string}")  # Debug: show what is being sent
#     serial_port.write(hex_bytes)
#     print("Data sent successfully.")  # Confirm data was sent

# def read_serial_data(serial_port):
#     print("Ready to receive data...")
#     while True:
#         if serial_port.in_waiting > 0:
#             first_byte = serial_port.read()
#             print(f"First byte {first_byte.hex()}")
#             if first_byte == MESSAGE_HEADER_2:
#                 #if serial_port.read() == MESSAGE_HEADER_2:
#                     data = 0
#                     while data != MESSAGE_END_2:
#                         #
#                         data = serial_port.read()
#                         print(f"{data.hex()}")
                    
#             #data = serial_port.readline().decode('utf-8', errors='ignore').strip()
#             #if data:
#             #    print(f"Received: {data}")  # Debug: print received data
#             #else:
#             #    print("Received data, but it's empty.")
#         else:
#             print("No data waiting.")
#         time.sleep(1)  # Pause briefly, adjust as necessary for your context

# if __name__ == "__main__":
#     ser = serial.Serial('/dev/serial0', baudrate = 9600,bytesize = serial.EIGHTBITS, timeout = None, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE)
#     print("Serial port opened successfully.")
    

#     #query_firmware_hex = "535902A400010F625443"
#     #hex_to_send = "FDFCFBFA0800FF0100000100400004030201"
#     #send_hex_string(ser, hex_to_send)
    

#     written = ser.write(FIRMWARE_QUERY)
#     print(f"wrote {written} bytes") 
#     try:
#         read_serial_data(ser)
#     except KeyboardInterrupt:
#         print("Stopped by User")
#     finally:
#         ser.close()








####################################################################



# ########################################################################

# import serial
# import binascii
# import time
# import mm_wave
# from mm_wave import *

# def send_hex_string(serial_port, hex_string):
#     hex_bytes = binascii.unhexlify(hex_string)
#     print(f"Sending hex: {hex_string}")  # Debug: show what is being sent
#     serial_port.write(hex_bytes)
#     print("Data sent successfully.")  # Confirm data was sent

# def read_serial_data(serial_port):
#     print("Ready to receive data...")
#     buffer = bytearray()
#     while True:
#         if serial_port.in_waiting > 0:
#             buffer.extend(serial_port.read(serial_port.in_waiting))
#             if len(buffer) >= 2:
#                 if buffer[0] == MESSAGE_HEADER_1 and buffer[1] == MESSAGE_HEADER_2:
#                     print(f"Header detected: {buffer[:2].hex()}")
#                     buffer = buffer[2:]
#                     while True:
#                         if serial_port.in_waiting > 0:
#                             buffer.extend(serial_port.read(serial_port.in_waiting))
#                             if MESSAGE_END_1 in buffer and MESSAGE_END_2 in buffer:
#                                 end_index = buffer.index(MESSAGE_END_2) + 1
#                                 message = buffer[:end_index]
#                                 print(f"Received complete message: {message.hex()}")
#                                 buffer = buffer[end_index:]
#                                 break
#                         else:
#                             print("Waiting for more data...")
#                         time.sleep(0.1)
#                 else:
#                     print(f"Unexpected header: {buffer[:2].hex()}")
#                     buffer = buffer[2:]  # Discard incorrect header
#         else:
#             print("No data waiting.")
#         time.sleep(1)  # Pause briefly, adjust as necessary for your context

# if __name__ == "__main__":
#     ser = serial.Serial('/dev/serial0', baudrate=9600, bytesize=serial.EIGHTBITS, timeout=None, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
#     print("Serial port opened successfully.")
    
#     # Make sure you have defined FIRMWARE_QUERY properly
#     written = ser.write(FIRMWARE_QUERY)
#     print(f"Wrote {written} bytes")
    
#     try:
#         read_serial_data(ser)
#     except KeyboardInterrupt:
#         print("Stopped by User")
#     finally:
#         ser.close()



# #########################################################################
# code using buffer: which has issues with unexpected header, so smth wrong
## trying claude now. 

# import serial
# import binascii
# import time
# import mm_wave
# from mm_wave import *

# # Example values, replace with actual values from your mmWave sensor documentation
# MESSAGE_HEADER_1 = 0x53
# MESSAGE_HEADER_2 = 0x59
# MESSAGE_END_1 = 0x54
# MESSAGE_END_2 = 0x43

# def send_hex_string(serial_port, hex_string):
#     hex_bytes = binascii.unhexlify(hex_string)
#     print(f"Sending hex: {hex_string}")  # Debug: show what is being sent
#     serial_port.write(hex_bytes)
#     print("Data sent successfully.")  # Confirm data was sent

# def read_serial_data(serial_port):
#     print("Ready to receive data...")
#     buffer = bytearray()
#     while True:
#         if serial_port.in_waiting > 0:
#             buffer.extend(serial_port.read(serial_port.in_waiting))
#             print(f"Buffer: {buffer.hex()}")  # Debug: Show buffer contents

#             while len(buffer) >= 2:
#                 if buffer[0] == MESSAGE_HEADER_1 and buffer[1] == MESSAGE_HEADER_2:
#                     print(f"Header detected: {buffer[:2].hex()}")
#                     buffer = buffer[2:]
#                     while True:
#                         if serial_port.in_waiting > 0:
#                             buffer.extend(serial_port.read(serial_port.in_waiting))
#                             if MESSAGE_END_1 in buffer and MESSAGE_END_2 in buffer:
#                                 end_index = buffer.index(MESSAGE_END_2) + 1
#                                 message = buffer[:end_index]
#                                 print(f"Received complete message: {message.hex()}")
#                                 buffer = buffer[end_index:]
#                                 break
#                         else:
#                             print("Waiting for more data...")
#                         time.sleep(0.1)
#                 else:
#                     print(f"Unexpected header: {buffer[:2].hex()}")
#                     buffer = buffer[1:]  # Discard incorrect byte
#         else:
#             print("No data waiting.")
#         time.sleep(1)  # Pause briefly, adjust as necessary for your context

# if __name__ == "__main__":
#     ser = serial.Serial('/dev/serial0', baudrate=9600, bytesize=serial.EIGHTBITS, timeout=None, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
#     print("Serial port opened successfully.")
    
#     # Example of sending a firmware query command
#     send_hex_string(ser, "FDFCFBFA0800120000006400000004030201")
    
#     try:
#         read_serial_data(ser)
#     except KeyboardInterrupt:
#         print("Stopped by User")
#     finally:
#         ser.close()

############################################################################
#claude2.0
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

# import time
# import serial
# import binascii
# import time
# import mm_wave as mm_wave
# from mm_wave import *

# # Constants
# MESSAGE_HEADER = b'\x53\x59'
# MESSAGE_END = b'\x54\x43'

# HUMANSTATUS = b'\x80'
# HUMANEXIST = b'\x01'
# HUMANMOVE = b'\x02'
# HUMANSIGN = b'\x03'
# HUMANDIRECT = b'\x0B'

# SOMEBODY = b'\x01'
# NOBODY = b'\x00'

# NONE = b'\x00'
# SOMEBODY_STOP = b'\x01'
# SOMEBODY_MOVE = b'\x02'

# CA_CLOSE = b'\x01'
# CA_AWAY = b'\x02'

# DETAILSTATUS = b'\x08'
# DETAILINFO = b'\x01'
# DETAILDIRECT = b'\x06'
# DETAILSIGN = b'\x07'

# SOMEONE = b'\x01'
# NOONE = b'\x02'
# NOTHING = b'\x03'
# SOMEONE_STOP = b'\x04'
# SOMEONE_MOVE = b'\x05'
# HUMANPARA = b'\x06'
# SOMEONE_CLOSE = b'\x07'
# SOMEONE_AWAY = b'\x08'
# DETAILMESSAGE = b'\x09'

# RESET_FRAME_LENGTH = 10
# SEEED_HUMAN_UNIT = 0.5

# RESET_FRAME = b'\x53\x59\x01\x02\x00\x01\x0F\xBF\x54\x43'


# RESET_FRAME_STRINGS = ["53", "59", "01", "02", "00", "01", "0F", "BF", "54", "43"]
# RESET_FRAME = bytes.fromhex(''.join(RESET_FRAME_STRINGS))



# def make_data_frame(commandData):
#     header_data = ["53","59"]
#     partial = bytes.fromhex(''.join(header_data + commandData))

#     checksum = b'%02X' % (sum(partial) & 0xFF)
#     tail_data = ["54","43"]
#     return partial + checksum + bytes.fromhex(''.join(tail_data))


# class HumanStatic():
#     def __init__(self):
#         pass

    
# def make_data_frame(command_data):
#     header = MESSAGE_HEADER
#     partial = header + bytes(command_data)
#     checksum = bytes([sum(partial) & 0xFF])
#     return partial + checksum + MESSAGE_END



# INITIALIZE_STATUS = make_data_frame([0x05, 0x81, 0x00, 0x00, 0x0F])
# FIRMWARE_QUERY = make_data_frame([0x02, 0xA4, 0x00, 0x00, 0x01, 0x0F])

# class HumanStatic:
#     def __init__(self, port='/dev/serial0', baudrate=9600):
#         self.ser = serial.Serial(port, baudrate, timeout=1)

#     def send_command(self, command):
#         self.ser.write(command)
#         time.sleep(0.1)  # Give some time for the device to respond
#         return self.read_response()

#     def read_response(self):
#         response = b''
#         while True:
#             if self.ser.in_waiting:
#                 byte = self.ser.read(1)
#                 response += byte
#                 if response.endswith(MESSAGE_END):
#                     break
#         return response

#     def initialize(self):
#         return self.send_command(INITIALIZE_STATUS)

#     def query_firmware(self):
#         return self.send_command(FIRMWARE_QUERY)

#     def set_scene_mode(self, mode):
#         if mode not in range(1, 5):
#             raise ValueError("Mode must be between 1 and 4")
#         command = make_data_frame([0x05, 0x07, 0x00, 0x01, mode])
#         return self.send_command(command)

#     def set_sensitivity(self, level):
#         if level not in range(1, 4):
#             raise ValueError("Sensitivity level must be between 1 and 3")
#         command = make_data_frame([0x05, 0x08, 0x00, 0x01, level])
#         return self.send_command(command)

#     def query_person_detection(self):
#         command = make_data_frame([0x80, 0x81, 0x00, 0x01, 0x0F])
#         response = self.send_command(command)
#         if len(response) >= 10:
#             status = response[7]
#             if status == 0x00:
#                 return "Unoccupied"
#             elif status == 0x01:
#                 return "Occupied"
#             else:
#                 return f"Unknown status: {status}"
#         else:
#             return "Invalid response"

#     def query_motion_information(self):
#         command = make_data_frame([0x80, 0x82, 0x00, 0x01, 0x0F])
#         response = self.send_command(command)
#         if len(response) >= 10:
#             status = response[7]
#             if status == 0x00:
#                 return "None (No motion detected)"
#             elif status == 0x01:
#                 return "Motionless (Person present but not moving)"
#             elif status == 0x02:
#                 return "Active (Motion detected)"
#             else:
#                 return f"Unknown motion status: {status}"
#         else:
#             return "Invalid response"



#     def close(self):
#         self.ser.close()

# if __name__ == "__main__":
#     sensor = HumanStatic()
#     try:
#         print("Initializing...")
#         print(sensor.initialize().hex())
        
#         print("Querying firmware version...")
#         print(sensor.query_firmware().hex())
        
#         print("Setting scene mode to Living Room...")
#         print(sensor.set_scene_mode(1).hex())
        
#         print("Setting sensitivity to level 2...")
#         print(sensor.set_sensitivity(2).hex())
        
#         print("Querying person detection status...")
#         print(sensor.query_person_detection())
        
#         print("Querying motion information...")
#         print(sensor.query_motion_information())
        
#     except Exception as e:
#         print(f"An error occurred: {e}")
#     finally:
#         sensor.close()
#         print("Sensor connection closed.")

