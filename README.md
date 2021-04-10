# Iot-Project

Setting up the Dragino and Upload data to Thingspeak using MQTT
Step to compile the file : 
1. install  dragino radiohead and add in the arduino library
https://github.com/dragino/RadioHead
2. Install dhtlib in arduino library 
3. Change the board to ardunino uno and port select the port that is currently using



Take Note: file is taken from dragino github 
https://wiki.dragino.com/index.php?title=Through_MQTT_to_upload_data#Updata_data_to_Server.28Through_MQTT.29
https://github.com/dragino/Arduino-Profile-Examples/tree/master/libraries/Dragino/examples/IoTServer/ThingSpeak/MQTT_Client



Following Steps:
1. Log in into the http://10.130.1.1/cgi-bin/luci/admin
2. Configure network access.Network->Internet Access
3. Set up the Thingspeak and set up the fields
4. Get access from Thingspeak and fill in the field in the internet access (Write API)



Step is taken from this https://wiki.dragino.com/index.php?title=Through_MQTT_to_upload_data#Updata_data_to_Server.28Through_MQTT.29 guide 
Dragino User Gateway - http://www.dragino.com/downloads/downloads/LoRa_Gateway/LG01N/LG01N_LoRa_Gateway_User_Manual_v1.1.pdf
