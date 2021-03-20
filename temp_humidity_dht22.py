import adafruit_dht
import time
import board
# from board import GPIO4
dht_device = adafruit_dht.DHT22(board.D4)


# print("Press x to exit program")
# x=input()
while(True):
    time.sleep(60) #Sleep for 60 seconds
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f} degrees  Humidity={1:0.1f}%".format(temperature, humidity))
        else:
            print("Failed to retrieve data from humidity sensor")
    except RuntimeError as error:
        print(error.args[0])
        continue
    except Exception as error:
        raise error
    # if (x=="x"):
    #     break
        
