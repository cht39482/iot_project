from bluepy import btle
import binascii
from bluepy.btle import Scanner
 
scanner = Scanner()
devices = scanner.scan(10.0)

peripheral_id = "30:ae:a4:4e:80:62"

for device in devices:
	if device.addr == peripheral_id:
    		print("DEV = {} RSSI = {}".format(device.addr, device.rssi))

print ("Connecting peripheral")
dev = btle.Peripheral(peripheral_id)
 
print ("Connecting services")
sensor = btle.UUID("04d2")

service = dev.getServiceByUUID(sensor)
char = service.getCharacteristics("11d7")[0]

# Get value    
val = char.read()
array = str(val).split(",")
temp = str(array[0])
humidity = str(array[1])  
print("temp: {} humidity: {}").format(temp, humidity)

# Convert value to hex  
# print(binascii.b2a_hex(val))

# Service <uuid=Generic Attribute handleStart=1 handleEnd=5>
# Service <uuid=Generic Access handleStart=20 handleEnd=28>
# Service <uuid=04d2 handleStart=40 handleEnd=65535>
# print(sensor)  