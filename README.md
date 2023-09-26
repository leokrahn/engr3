# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```




And here is how you should give image credit to someone if you use their work:





### Wiring
Make an account with your Google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**



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


## CircuitPython_LCD

### Description & Code Snippets
Write a couple sentences here, describing this assignment, and make sure that you hit these two points:
* What was the goal of the assignment?
* How did you accomplish that goal?
  How you accomplished the goal is NOT a reflection, it is you telling the reader how to do this assignment, in broad strokes.

  Your description is the right place to draw the reader's attention to any important chunks of code. Here's how you make code look like code:

```python
Code goes here

```

**Lastly, please end this section with a link to your code or file.**  


### Evidence
Pictures / Gifs of your finished work should go here.  You need to communicate what your thing does.
For making a GIF, I recommend [ezgif.com](https://www.ezgif.com) Remember you can insert pictures using Markdown or HTML to insert an image.


And here is how you should give image credit to someone if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
[tinkercad.com](https://www.tinkercad.com/learn/circuits).  If you can't find the particular part you need, get creative, and just drop a note into the circuit diagram, explaining.
For example, I use an Arduino Uno to represent my Circuitpython device but write a note saying which board I'm actually using.
Then post an image here.   [Here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)


### Reflection
Don't just tell the reader what went wrong or was challenging!  Describe how you figured it out, share the things that helped you succeed (tutorials, other people's repos, etc.), and then share what you learned from that experience.  **Your underlying goal for the reflection, is to concisely pass on the RIGHT knowledge that will help the reader recreate this assignment better or more easily.  Pass on your wisdom!**





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
