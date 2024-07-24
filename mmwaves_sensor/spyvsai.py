#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2024  <pgss@spyai2>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
import serial
import binascii
import time

def send_hex_string(serial_port, hex_string):
    hex_bytes = binascii.unhexlify(hex_string)
    print(f"Sending hex: {hex_string}")  # Debug: show what is being sent
    serial_port.write(hex_bytes)
    print("Data sent successfully.")  # Confirm data was sent

def read_serial_data(serial_port):
    print("Ready to receive data...")
    while True:
        if serial_port.in_waiting > 0:
            data = serial_port.readline().decode('utf-8', errors='ignore').strip()
            if data:
                print(f"Received: {data}")  # Debug: print received data
            else:
                print("Received data, but it's empty.")
        else:
            print("No data waiting.")
        time.sleep(1)  # Pause briefly, adjust as necessary for your context

if __name__ == "__main__":
    try:
        ser = serial.Serial('/dev/serial0', 115200, timeout=1)
        print("Serial port opened successfully.")
    except Exception as e:
        print(f"Failed to open serial port: {e}")

    hex_to_send = "FDFCFBFA0800120000006400000004030201"
    send_hex_string(ser, hex_to_send)

    try:
        read_serial_data(ser)
    except KeyboardInterrupt:
        print("Stopped by User")
    finally:
        ser.close()
        print("Serial port closed.")
        
