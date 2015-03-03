#Requires Python 3.X

#The layout of this block of code is based on https://github.com/lepoetemaudit/restack Usage Via ReadMe

from restack import Restack, Device

AUTH TOKEN = input ('Enter Your Restack API Key')

#Dashboard To List All Devices

print ('This is the main dashboard')

print ("All IoT Security Devices")

devices = restack.get_devices()

