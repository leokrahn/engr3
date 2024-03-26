# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
__
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---


## CircuitPython_Servo

The goal of the assignment was to control a servo motor using 2 buttons. The code was made in CircuitPython. First I wired a servo and got it working with a loop code. Then I wired 2 buttons and got them to talk to the Serial Moniter. Then I combined the 2 codes and added a couple things from online libraries. 

  Here is the code     

```python
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

# create a PWMOut object on the control pin.
pwm = pwmio.PWMOut(board.D5, duty_cycle=0, frequency=50)

btn = DigitalInOut(board.D8)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

btn2 = DigitalInOut(board.D9)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

# To get the full range of the servo you will likely need to adjust the min_pulse and max_pulse to
# match the stall points of the servo.
# This is an example for the Sub-micro servo: https://www.adafruit.com/product/2201
# servo = servo.Servo(pwm, min_pulse=580, max_pulse=2350)
# This is an example for the Micro Servo - High Powered, High Torque Metal Gear:
#   https://www.adafruit.com/product/2307
# servo = servo.Servo(pwm, min_pulse=500, max_pulse=2600)
# This is an example for the Standard servo - TowerPro SG-5010 - 5010:
#   https://www.adafruit.com/product/155
# servo = servo.Servo(pwm, min_pulse=400, max_pulse=2400)
# This is an example for the Analog Feedback Servo: https://www.adafruit.com/product/1404
# servo = servo.Servo(pwm, min_pulse=600, max_pulse=2500)
# This is an example for the Micro servo - TowerPro SG-92R: https://www.adafruit.com/product/169
# servo = servo.Servo(pwm, min_pulse=500, max_pulse=2400)

# The pulse range is 750 - 2250 by default. This range typically gives 135 degrees of
# range, but the default is to use 180 degrees. You can specify the expected range if you wish:
# servo = servo.Servo(board.D5, actuation_range=135)
servo = servo.Servo(pwm)
angle = 90

# We sleep in the loops to give the servo time to move into position.
while True:
    if btn.value:
        angle = angle + 1
        if angle > 180:
            angle = 180
        print(angle)
        servo.angle = angle
        time.sleep(0.01)
        
    if btn2.value:
        angle = angle - 1
        if angle < 0:
            angle = 0
        print(angle)
        servo.angle = angle
        time.sleep(0.01)

```

**Link to my code**  
	[Servo Code](https://github.com/leokrahn/engr3/blob/main/servo.py)
### Evidence
![ezgif-5-a997dfd67c-min](https://github.com/leokrahn/engr3/assets/143544783/7010ea8c-76ee-4462-a460-b1fbd6a6f69b)
Image credit goes to [me]

### Wiring
Note: I'm using a metro m0 with a shield, not an arduino with a breadboard
![Screenshot (1)](https://github.com/leokrahn/engr3/assets/143544783/856c88c2-909a-416e-94f3-243e35c7023c)

### Reflection

Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**

## CircuitPython_Distance_Sensor

The goal of this assignment was to smoothly shift the color of a neopixel based on the distance from a ultrasonic sensor

  
  Here is the code     

```python
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

NUMPIXELS = 1  # Update this to match the number of LEDs.
SPEED = 0.1  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 0.2  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL  # This is the default pin on the 5x5 NeoPixel Grid BFF.

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

while True:
    try:
        print((sonar.distance))
        time.sleep(0.1)
        if (sonar.distance < 5):
            pixels.fill(RED)
            pixels.show()
            time.sleep(0.1)
        elif (5 < sonar.distance < 20):
            x = simpleio.map_range((sonar.distance),5,20,0,255)
            pixels.fill((255-x, 0, x))
            pixels.show()
            time.sleep(0.1)
        elif (sonar.distance == 20):
            pixels.fill(BLUE)
            pixels.show()
            time.sleep(0.1)
        elif (20 < sonar.distance < 35):
            x = simpleio.map_range((sonar.distance),20,35,0,255)
            pixels.fill((0, x, 255-x))
            pixels.show()
            time.sleep(0.1)
        elif (sonar.distance > 35):
            pixels.fill(GREEN)
            pixels.show()
            time.sleep(0.1)
    except RuntimeError:
        print("Retrying!")

```

**Link to my code**  
	[Servo Code]([https://github.com/leokrahn/engr3/blob/main/servo.py](https://github.com/leokrahn/engr3/blob/main/button.py))
### Evidence
![ezgif-4-ed9e11f651-min](https://github.com/leokrahn/engr3/assets/143544783/35811fc8-2ca4-4bb9-af7b-5baff87b59b1)

Image credit goes to [me]


### Wiring
Note: I'm using a metro m0 with a shield, not an arduino with a breadboard
![image](https://github.com/leokrahn/engr3/assets/143544783/164127f4-f676-4b13-9080-2d6a1d622736)


### Reflection
The first thing I did was wire the distance sensor and use an example code to print the distance of the sensor. Then I made the neopixel turn red when it's less then 5 cm, and green when it's less then 35. Then I made it smoothly shift along the spectrum (I got help from a friend on this part). I learned more about circuit python from this assignment.






## Motor Control

### Description & Code Snippets
The goal of the assignment was to wire a motor using a 6V battery pack, a transistor, and a potentiometer. and to write code to make the motor speed up or slow down using the potentiometer. I started by wiring the whole thing using the diagram on the assignment page but not putting in the batteries. Then I wrote code to get a value from the potentiometer. After getting that working I added code to convert the potentiometer values to motor values based on the pwmio module.

```python
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

```

[***Link to my code***](https://github.com/leokrahn/engr3/blob/main/potentiometer.py)

### Evidence
![ezgif-5-a8eef860d4](https://github.com/leokrahn/engr3/assets/143544783/69f277ca-2558-4a82-9023-e6456f96561b)
Image credit goes to me

### Wiring
![Screenshot (4)](https://github.com/leokrahn/engr3/assets/143544783/2a833573-6b55-4e00-b676-60410cb17657)

### Reflection

The wiring part of the assignment was pretty easy, josh showed me how to wire the potentiometer and I got the rest from the assignment page. Getting the code for the potentiometer was easy as well, I just looked up a code for a potentiometer and it worked. Converting the potentiometer values to motor values was the hardest part as a spent too long trying to use different functions that wouldn't work here. Eventually Mr. Dirov showed me the pwmio module and I filled in the rest pretty fast. The last part was that after all that the motor wasn't working, so I got a new battery pack and it worked

## Photointerrupter

### Description & Code Snippets

```python
from digitalio import DigitalInOut, Direction, Pull
import time
import board

interrupter = DigitalInOut(board.D7)
interrupter.direction = Direction.INPUT
interrupter.pull = Pull.UP

counter = 0

photo = False
state = False

max = 4
start = time.time()
while True:
    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo

    remaining = max - time.time()

    if remaining <= 0:
        print("the number of photointerrupts is:", str(counter))
        max = time.time() + 4
        counter = 0

```

[***Link to my code***](https://github.com/leokrahn/engr3/blob/main/photointerrupter.py)

### Evidence
![Screenshot (5)](https://github.com/leokrahn/engr3/assets/143544783/c149f798-be4b-414d-89a9-eca753009bcd)

Image credit goes to me

### Wiring
![Screenshot (4)](https://github.com/leokrahn/engr3/assets/143544783/2a833573-6b55-4e00-b676-60410cb17657)

### Reflection

The wiring part of the assignment was pretty easy, josh showed me how to wire the potentiometer and I got the rest from the assignment page. Getting the code for the potentiometer was easy as well, I just looked up a code for a potentiometer and it worked. Converting the potentiometer values to motor values was the hardest part as a spent too long trying to use different functions that wouldn't work here. Eventually Mr. Dirov showed me the pwmio module and I filled in the rest pretty fast. The last part was that after all that the motor wasn't working, so I got a new battery pack and it worked

## Hanger

### Assignment Description

The goal of the assignment was to design the hanger in onshape from the drawing. It's practice for the certification test. 

### Evidence


![Screenshot (9)](https://github.com/leokrahn/engr3/assets/143544783/0ee413c6-9b3d-4db5-ab07-4aa2165a8db5)
![Screenshot (8)](https://github.com/leokrahn/engr3/assets/143544783/32879ec6-2d21-4ef2-a492-259ffe92332e)
![Screenshot (7)](https://github.com/leokrahn/engr3/assets/143544783/270c770e-ed00-4abb-8283-2ddec89e2f12)
![Screenshot (6)](https://github.com/leokrahn/engr3/assets/143544783/df5910ab-1dae-47fc-ac3f-2be0a41b3353)

### Part Link 


](https://cvilleschools.onshape.com/documents/00ecd1636b105a177daf0a85/w/ff0b1cdb7f029664d12037af/e/deca9313680e6e75c29814b1?renderMode=0&uiState=651c64f535a14d2ada3c9064)
### Reflection


This assignment reminded me on how to do a lot of CAD stuff that I maybe forgot. It was pretty easy and I was almost done on friday (the day I started) and finished on monday before the bell even rang. There were some things I was confused about like the arch but other than that I remembered how to do it.
&nbsp;

 

## Swing arm

### Assignment Description

The goal of the assignment was to create the swing arm from the drawings in a way that you can change 3 different variables freely. There were 4 drawings to go off of and 2 questions with different variable settings and material. The mass of the part should be witihin 1% of the right answer.

### Evidence
![image](https://github.com/leokrahn/engr3/assets/143544783/cce72765-f10b-4a72-a894-302919e07fd4)
![image](https://github.com/leokrahn/engr3/assets/143544783/88d6ca8a-6604-4a86-8e00-7c739a2b764e)
![image](https://github.com/leokrahn/engr3/assets/143544783/7f21691d-5a84-4dea-ad85-ff48690395b7)
![image](https://github.com/leokrahn/engr3/assets/143544783/37bfba2c-d972-4c92-9258-75647e1e90b0)


### Part Link 

[link](https://cvilleschools.onshape.com/documents/e57e2b944236825246ddfa70/w/32f5b939a9de66a2a0d833e2/e/c87cbfca08facb2f44d174fb)

### Reflection

I started by drawing the main circle and then the 2 parts that protrude from it. After finishing the sketch of the front plane I extruded everything and continued with the other extrudes, fillets, and sketches. With the variable settings of the first question, origininally my part was well within 1%, but when I changed the variables everything broke. I defined everything that wasn't defined and made it so that the end circles are defined 20mm from the edge instead of centered on the edge and that fixed mostly everything. For some reason my measurements still aren't exact but everything is within 1%.

&nbsp;

<<<<<<< HEAD
## Rotary Encoder & LCD

### Description & Code Snippets
The goal of the assignemtn was to use a rotary encoder to control an lcd screen and a neopixel and to use them as a kind of traffic light. I started by wiring the Rotary Encoder and getting it to say stop caution go to the serial monitor. Then I got the LCD working, and then wrote code to get the neopixel working.

Here is the code
```python
import rotaryio
import board
import neopixel
import digitalio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor=2)
lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), num_rows=2, num_cols=16)

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3
led[0] = (255, 0, 0)

button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None

menu = ["stop", "caution", "go"]
last_index = None
menu_index = 0

while True:
    menu_index_lcd = menu_index % 3
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Button is pressed")
        button_state = None
    menu_index = enc.position
    menu[menu_index_lcd]
    lcd.set_cursor_pos(1,0)
    lcd.print("       ")
    lcd.set_cursor_pos(1,0)
    lcd.print(menu[menu_index_lcd])
    if menu_index_lcd == 0:
        led[0] = (255, 0, 0)
    if menu_index_lcd == 1:
        led[0] = (255, 255, 0)
    if menu_index_lcd == 2:
        led[0] = (0, 255, 0)
```

[***Link to my code***]

### Evidence

![ezgif-6-f989b1b6f1](https://github.com/leokrahn/engr3/assets/143544783/6b319e0c-8a11-4856-9a2c-b6cffbdf08c7)


### Wiring

![Screenshot 2024-02-08 152518](https://github.com/leokrahn/engr3/assets/143544783/952c1820-80b0-4a25-a717-f9a15bb208ba)

### Reflection
the assign ment was pretty easy, i followed the instructions on the slides for both the wiring and the first part of the code, and then did the rest on my own.

 
=======
 ## IR Sensor

### Description & Code Snippets

The goal of the assigment was to use an IR sensor to decide if there is an object close to it or not, and then to change the color of an LCD based on that.

Here is the code
```python
import board
import neopixel
import digitalio

ir_sensor = digitalio.DigitalInOut(board.D2)
ir_sensor.direction = digitalio.Direction.INPUT
ir_sensor.pull = digitalio.Pull.UP

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3

while True:
    if ir_sensor.value:
        print("not close")
        led[0] = (255, 0, 0)
    if not ir_sensor.value:
        print("close")
        led[0] = (0, 255, 0)
```
### Evidence
![ezgif-6-98ac4fb2bd](https://github.com/leokrahn/engr3/assets/143544783/531213c2-3866-4fe4-964d-4a492b0e0ec2)


### Wiring
![Screenshot 2024-02-13 143208](https://github.com/leokrahn/engr3/assets/143544783/e4ce5ba9-f68d-4b90-8a00-2bce66e01d55)

### Reflection
The wiring was obvious so I did that first and then started following the slideshow for most of the code. The final part I got stuck for a little but I looked through old code assignments to figure it out.
 ## Stepper Motors & Limit Switch
### Description and Code Snippets

The goal of this assignment was to use a limit switch to control a stepper motor so that the motor continually spins, and reverses briefly when you press the switch.

Here is the code
```python
import asyncio
import board
import keypad
import time
import digitalio
from adafruit_motor import stepper

DELAY = 0.01
STEPS = 100

coils = (
    digitalio.DigitalInOut(board.D9), #A!
    digitalio.DigitalInOut(board.D10), #A2
    digitalio.DigitalInOut(board.D11), #B1
    digitalio.DigitalInOut(board.D12), #B2
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT
    
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

for step in range(STEPS):
    motor.onestep(style=stepper.DOUBLE)
    time.sleep(DELAY)

for step in range(STEPS):
    motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    time.sleep(DELAY)

async def catch_pin_transitions(pin):
    # Print a message when pin goes low and when it goes high.
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Limit Switch was pressed.")
                    for step in range(STEPS):
                        motor.onestep(direction=stepper.BACKWARD)
                        time.sleep(DELAY)
                elif event.released:
                    print("Limit Switch was released.")

            await asyncio.sleep(0)

async def run_motor():
    while(True):
        for step in range(STEPS):
            motor.onestep()
            time.sleep(DELAY)
        await asyncio.sleep(0)

async def main():
    interrupt_task = asyncio.create_task(catch_pin_transitions(board.D2))

    motor_task = asyncio.create_task(run_motor())
    await asyncio.gather(interrupt_task)

asyncio.run(main())
```

### Evidence
![ezgif-3-055fb318dc](https://github.com/leokrahn/engr3/assets/143544783/1c851b95-d796-4a17-9105-6075890ab432)

### Wiring
![Screenshot 2024-02-20 144958](https://github.com/leokrahn/engr3/assets/143544783/9319e1d9-c74d-4366-b751-fd1fa094c3fb)

 ## Single Part

### Assignment Description

The goal of the assignment was to create the part using the given drawing and then change the variables and other values to find the mass of the part for different questions. It's prep for our certification test.

### Evidence
![image](https://github.com/leokrahn/engr3/assets/143544783/a303604b-a193-42bd-b610-79463689536c)
![image](https://github.com/leokrahn/engr3/assets/143544783/93e57ce5-466e-4b9d-aecb-c03bd1dd3c24)
![image](https://github.com/leokrahn/engr3/assets/143544783/f5dc51d0-a7e2-4156-9733-229c312af014)
![image](https://github.com/leokrahn/engr3/assets/143544783/10a8d8f9-8295-4aa4-a35b-09f20bfdc17d)
![image](https://github.com/leokrahn/engr3/assets/143544783/e6aed3c8-f889-4bf3-a04c-b56cb9691a9e)


### Part Link 
>>>>>>> b2c6691c70b55c8fec7cb572825c5b9739ec4550

[link](https://cvilleschools.onshape.com/documents/67a89f844e7b3bc0f27c27c0/w/a7ba080924b4764f867ba6f5/e/e3884aed1916ed9001078dfe?renderMode=0&uiState=6543f734fce0961b6edc4664)

### Reflection

This one was pretty easy I just followed the steps in the drawings and got question one done, although it wasn't right. My sketch 1 wasn't defined right so I redid it and it worked. After that everything went smoothly.

&nbsp;

 ## Multi Part

### Assignment Description

The goal of the assignment was to create the parts using the given drawings and then change the variables and other values to find the mass of the part for different questions. It's prep for our certification test.

### Evidence
![Screenshot 2024-03-25 151345](https://github.com/leokrahn/engr3/assets/143544783/9198ca63-5b54-477e-a80e-fb7bc4f61d49)


### Part Link 

[link](https://cvilleschools.onshape.com/documents/67a89f844e7b3bc0f27c27c0/w/a7ba080924b4764f867ba6f5/e/e3884aed1916ed9001078dfe?renderMode=0&uiState=6543f734fce0961b6edc4664)

### Reflection

This one was pretty easy I just followed the steps in the drawings and got question one done, although it wasn't right. My sketch 1 wasn't defined right so I redid it and it worked. After that everything went smoothly.

&nbsp;

 ## Mic Stand

### Assignment Description

This was multi part practice assignment for the certification exam where you had to create the parts using the given drawings.

### Evidence
![Screenshot 2024-03-25 154022](https://github.com/leokrahn/engr3/assets/143544783/8f05be9e-3f0f-4c24-ac9e-a8f9c91b6292)



### Part Link 

[link](https://cvilleschools.onshape.com/documents/01d1da9243e1f143c9256174/w/a32e6cf67fb014620bcc626e/e/fe8e5b58cfbce666d5279b72)
### Reflection

The mic stand was pretty easy I spent the most time on the first question but I just followed the drawings and changes the values and got it done.

&nbsp;

 ## Assemblies

### Assignment Description

For this assignment there were already made parts in onshape and the goal was to assemble them so that the pliers work properly and answer the questions on canvas.

### Evidence

![ezgif-3-36ffbde276](https://github.com/leokrahn/engr3/assets/143544783/04ccd679-f9d5-406e-8f23-c21e6643fc9c)


### Part Link 

[link](https://cvilleschools.onshape.com/documents/d77f64b8d9c70d3b1ccb3665/w/6ace413eee81a368e0fa0a50/e/c128dfcb7127ef76f9353c90)

### Reflection

Tbh I don't remember exactly what I did for this assignment but I think I just added the proper mates to all the right parts and it worked fine. 

&nbsp;

 ## Robot gripper

### Assignment Description

The goal of the assignment was to make a robot gripper in onshape and animate it.

### Evidence
![ezgif-7-b2c5aaedee](https://github.com/leokrahn/engr3/assets/143544783/16b62d07-00a6-4fff-901c-5b37325515bf)
![Screenshot 2024-03-04 152948](https://github.com/leokrahn/engr3/assets/143544783/bf6b479b-6c05-4a8b-b68b-ddbcf2b29809)

### Part Link 
>>>>>>> b2c6691c70b55c8fec7cb572825c5b9739ec4550

[link](https://cvilleschools.onshape.com/documents/d7fce35cd364549cedf687c6/w/ec2bc0f2931aebb817e0e55b/e/fe40fcb2fa841ed0304e27cc)

### Reflection

For this assignment I took inspiration from the example and made a similar design. I also got help from my classmate. 

&nbsp;
 
 
 
 

 
