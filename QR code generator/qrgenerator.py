#! /usr/bin/python3

import qrcode
import image
import datetime

# Pretty Banner
print("`````````````````````````````````````````````````````````````````````````````````````````````")
print("-----------------------------------QR Code Generator-----------------------------------------")
print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

curr_datetime = datetime.datetime.now().strftime('%Y-%m-%d-%H.%M.%S')

msg = input("\nInput your message to encode as QR image: ")
img = qrcode.make(msg)
imgname = "QR-Code-" + str(curr_datetime)
img.save(str(imgname))