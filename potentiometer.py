# SPDX-FileCopyrightText: 2018 Anne Barela for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
from analogio import AnalogIn
import time
import pwmio
import board

pwm = pwmio.PWMOut(board.D3)


potentiometer = AnalogIn(board.A0)  # potentiometer connected to A1, power & ground

while True:

    print((potentiometer.value,))      # Display value

    time.sleep(0.25)                   # Wait a bit before checking all again
    
    pwm.duty_cycle = potentiometer.value
    time.sleep(0.1)