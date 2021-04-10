from network import Bluetooth
import sensor
from sensor import read_sensor
import time

read_val = 0
values = {}


def conn_cb(bt_o):
    events = bt_o.events()
    if events & Bluetooth.CLIENT_CONNECTED:
        print(events)
        print("Client connected")
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print(events)
        print("Client disconnected")


def char1_cb_handler(chr, data):

    # The data is a tuple containing the triggering event and the value if the event is a WRITE event.
    # We recommend fetching the event and value from the input parameter, and not via characteristic.event() and characteristic.value()
    events, value = data
    if events & Bluetooth.CHAR_WRITE_EVENT:
        print("Write request with value = {}".format(value))
    else:
        print('Read request on char 1')


def char2_cb_handler(data):  # (chr, data):
    # The value is not used in this callback as the WRITE events are not processed.
    print('Read request on char 2')
    print(data)
    print(data.events())
    print(data.value())

    #events, value = data
    # if  events & Bluetooth.CHAR_READ_EVENT:
    #     print('Read request on char 2')


bluetooth = Bluetooth()
bluetooth.set_advertisement(
    name='LoPyRandy', service_uuid=b'1234567890123456')  # b'1234567890123456'
print("set adv...")
bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED |
                   Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)
bluetooth.advertise(True)
print("adv done...")

# srv1 = bluetooth.service(uuid=3579, isprimary=True) #b'1234567890123456'
# chr1 = srv1.characteristic(uuid=9753, value='35.2') #b'ab34567890123456'
# print("set write...")
# char1_cb = chr1.callback(trigger=Bluetooth.CHAR_WRITE_EVENT, handler=char1_cb_handler) #| Bluetooth.CHAR_READ_EVENT
#print("read write...")
values = sensor.read_sensor()
temp = values["temperature"]
humidity = values["humidity"]
print("temperature " + str(temp))
srv2 = bluetooth.service(uuid=1234, isprimary=True)
chr2 = srv2.characteristic(
    uuid=4567, value=str(temp)+","+str(humidity))
# srv_humidity = bluetooth.service(uuid=2234, isprimary=True)
# chr_humidity = srv_humidity.characteristic(
#     uuid=4567, value=str(temp+","+humidity))  # 0x1234
print("set read...")

while True:
    time.sleep_ms(2000)
    char2_cb = chr2.callback(
        trigger=Bluetooth.CHAR_READ_EVENT, handler=char2_cb_handler)
    # char_humidity = chr_humidity.callback(
    #     trigger=Bluetooth.CHAR_READ_EVENT, handler=char_humidity_handler)
    print("This is running now")


# while True:
#     time.sleep_ms(5000)
#     read_val += 1
#     chr2.value(str(read_val))
#     print('update='+ str(read_val)) #0x1234

#     chr2 = srv2.characteristic(uuid=4567, value=str(read_val))
#     char2_cb = chr2.callback(trigger=Bluetooth.CHAR_READ_EVENT, handler=char2_cb_handler)
