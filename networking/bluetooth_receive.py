from bluepy import btle
import binascii

print ("Bluetooth Receive Connecting..")
dev = btle.Peripheral("30:ae:a4:4e:7e:fe")
 
print ("Bluetooth Receive Connected Successfully.")

sensor = btle.UUID("04d2")
data_service = dev.getServiceByUUID(sensor)
data_char = data_service.getCharacteristics(sensor)
print(f"Service: {data_service}, Char: {data_char}")

val = data_char.read()
print(f"Value: {val}")  




