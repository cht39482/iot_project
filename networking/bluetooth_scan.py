from network import Bluetooth
import time

read_val = 0


def conn_cb(bt_o):
    events = bt_o.events()
    if events & Bluetooth.CLIENT_CONNECTED:
        print(events)
        print("Client connected")
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        print(events)
        print("Client disconnected")


def char2_cb_handler(data):  # (chr, data):
    print('Read request on char 2')
    print(data)
    print(data.events())
    print(data.value())

bluetooth = Bluetooth()
bluetooth.set_advertisement(
    name='LoPyRandy', service_uuid=b'1234567890123456')  # b'1234567890123456'
print("set adv...")
bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED |
                   Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)
bluetooth.advertise(True)
print("adv done...")

srv2 = bluetooth.service(uuid=1234, isprimary=True)
chr2 = srv2.characteristic(uuid=4567, value='35.2')  # 0x1234
print("set read...")
char2_cb = chr2.callback(
    trigger=Bluetooth.CHAR_READ_EVENT, handler=char2_cb_handler)
print("read done...")

while True:
    time.sleep_ms(5000)
    read_val += 1
    chr2.value(str(read_val))
    print('update=' + str(read_val))  # 0x1234

chr2 = srv2.characteristic(uuid=4567, value=str(read_val))
char2_cb = chr2.callback(
    trigger=Bluetooth.CHAR_READ_EVENT, handler=char2_cb_handler)


# 30:ae:a4:4e:76:6e (public), -66 dBm
# Flags: < 06 >
# Tx Power: < eb >
# 0x12: < 20004000 >
# Complete Local Name: 'LoPyRandy'
# Device (new): 50:19:fd:81:f1:08 (random), -85 dBm
# Flags: <1a>
# Complete 16b Services: <0000ffff-0000-1000-8000-00805f9b34fb>
# 16b Service Data: <ffffea670e0ef3b0046005876c8ec8db894a57cab140>
# Device (new): 30:ae:a4:4e:6c:ea (public), -78 dBm
# Flags: <06>
