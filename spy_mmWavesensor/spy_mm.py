import serial
import binascii
import time
import spy_mmWavesensor.mm_wave as mm_wave
from spy_mmWavesensor.mm_wave import *

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
