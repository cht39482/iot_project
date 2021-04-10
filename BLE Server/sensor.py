#!/usr/bin/env python
#
# Copyright (c) 2020, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

# See https://docs.pycom.io for more information regarding library specifics

import time
import pycom
from pysense import Pysense
import machine

from SI7006A20 import SI7006A20


py = Pysense(sda='P22', scl='P21')
si = SI7006A20(py)
sleep = False
values = {}


def read_sensor():

    values["temperature"] = si.temperature()
    values["humidity"] = si.humidity()

    print("Temperature: " + str(values["temperature"]) +
          " deg C and Relative Humidity: " + str(values["humidity"]) + " %RH")
#     print("Dew point: " + str(si.dew_point()) + " deg C")
#     t_ambient = 24.4
#     print("Humidity Ambient for " + str(t_ambient) +
#           " deg C is " + str(si.humid_ambient(t_ambient)) + "%RH")

    return values
