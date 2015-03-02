#Requires Python 3.X
#More info at http://restack.io for api docs

from restack import Restack, Device

#User Must Provide Their Restack API Key
AUTH TOKEN = input ('Please Enter Your Restack API Key')

device = Device(conn=restack)

print('Add A Device')

device.name = input ('Enter A Name For Your Device')
print(device.name)
device.description = input('Enter A Descrption For Your Device')
print(device.description)

print ('Here Is All The Device Info You Just Entered')
print(device.name, device.description)

device.save()