"""
Author: Cameron Scheet
Date:   2024/04/10

Drivers for OS2G's Number Pad Project
This program uses Circuit Python on a
Raspberry Pi Pico.

This is not done yet. It can only press
things that can be pressed when the
number pad is on.
(it turns numlock on for you)
"""

import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#define constants
sleep_time = 0.05


#define keyboard
keyboard = Keyboard(usb_hid.devices)


#define keypins
btn_0_pin = board.GP0
btn_1_pin = board.GP1
btn_2_pin = board.GP2
btn_3_pin = board.GP3
btn_4_pin = board.GP4
btn_5_pin = board.GP5
btn_6_pin = board.GP6
btn_7_pin = board.GP7
btn_8_pin = board.GP8
btn_9_pin = board.GP9
btn_period_pin = board.GP10
btn_plus_pin = board.GP11
btn_minus_pin = board.GP12
btn_star_pin = board.GP13
btn_forward_slash_pin = board.GP14
btn_enter_pin = board.GP15
btn_num_lock_pin = board.GP16


#use the keypins to make buttons
#make every button recieve an input
#make every button able to be pressed down
btn_0 = digitalio.DigitalInOut(btn_0_pin)
btn_0.direction = digitalio.Direction.INPUT
btn_0.pull = digitalio.Pull.DOWN

btn_1 = digitalio.DigitalInOut(btn_1_pin)
btn_1.direction = digitalio.Direction.INPUT
btn_1.pull = digitalio.Pull.DOWN

btn_2 = digitalio.DigitalInOut(btn_2_pin)
btn_2.direction = digitalio.Direction.INPUT
btn_2.pull = digitalio.Pull.DOWN

btn_3 = digitalio.DigitalInOut(btn_3_pin)
btn_3.direction = digitalio.Direction.INPUT
btn_3.pull = digitalio.Pull.DOWN

btn_4 = digitalio.DigitalInOut(btn_4_pin)
btn_4.direction = digitalio.Direction.INPUT
btn_4.pull = digitalio.Pull.DOWN

btn_5 = digitalio.DigitalInOut(btn_5_pin)
btn_5.direction = digitalio.Direction.INPUT
btn_5.pull = digitalio.Pull.DOWN

btn_6 = digitalio.DigitalInOut(btn_6_pin)
btn_6.direction = digitalio.Direction.INPUT
btn_6.pull = digitalio.Pull.DOWN

btn_7 = digitalio.DigitalInOut(btn_7_pin)
btn_7.direction = digitalio.Direction.INPUT
btn_7.pull = digitalio.Pull.DOWN

btn_8 = digitalio.DigitalInOut(btn_8_pin)
btn_8.direction = digitalio.Direction.INPUT
btn_8.pull = digitalio.Pull.DOWN

btn_9 = digitalio.DigitalInOut(btn_9_pin)
btn_9.direction = digitalio.Direction.INPUT
btn_9.pull = digitalio.Pull.DOWN

btn_period = digitalio.DigitalInOut(btn_period_pin)
btn_period.direction = digitalio.Direction.INPUT
btn_period.pull = digitalio.Pull.DOWN

btn_plus = digitalio.DigitalInOut(btn_plus_pin)
btn_plus.direction = digitalio.Direction.INPUT
btn_plus.pull = digitalio.Pull.DOWN

btn_minus = digitalio.DigitalInOut(btn_minus_pin)
btn_minus.direction = digitalio.Direction.INPUT
btn_minus.pull = digitalio.Pull.DOWN

btn_star = digitalio.DigitalInOut(btn_star_pin)
btn_star.direction = digitalio.Direction.INPUT
btn_star.pull = digitalio.Pull.DOWN

btn_forward_slash = digitalio.DigitalInOut(btn_forward_slash_pin)
btn_forward_slash.direction = digitalio.Direction.INPUT
btn_forward_slash.pull = digitalio.Pull.DOWN

btn_enter = digitalio.DigitalInOut(btn_enter_pin)
btn_enter.direction = digitalio.Direction.INPUT
btn_enter.pull = digitalio.Pull.DOWN

btn_num_lock = digitalio.DigitalInOut(btn_num_lock_pin)
btn_num_lock.direction = digitalio.Direction.INPUT
btn_num_lock.pull = digitalio.Pull.DOWN


#start loop to check when keys are presses
keyboard.press(Keycode.KEYPAD_NUMLOCK)
while True:
    if btn_0.value:
        keyboard.press(Keycode.KEYPAD_ZERO)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_ZERO)
        
    if btn_1.value:
        keyboard.press(Keycode.KEYPAD_ONE)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_ONE)
        
    if btn_2.value:
        keyboard.press(Keycode.KEYPAD_TWO)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_TWO)
        
    if btn_3.value:
        keyboard.press(Keycode.KEYPAD_THREE)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_THREE)
        
    if btn_4.value:
        keyboard.press(Keycode.KEYPAD_FOUR)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_FOUR)
        
    if btn_5.value:
        keyboard.press(Keycode.KEYPAD_FIVE)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_FIVE)
        
    if btn_6.value:
        keyboard.press(Keycode.KEYPAD_SIX)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_SIX)
        
    if btn_7.value:
        keyboard.press(Keycode.KEYPAD_SEVEN)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_SEVEN)
        
    if btn_8.value:
        keyboard.press(Keycode.KEYPAD_EIGHT)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_EIGHT)
        
    if btn_9.value:
        keyboard.press(Keycode.KEYPAD_NINE)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_NINE)
        
    if btn_period.value:
        keyboard.press(Keycode.KEYPAD_PERIOD)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_PERIOD)
        
    if btn_plus.value:
        keyboard.press(Keycode.KEYPAD_PLUS)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_PLUS)
        
    if btn_minus.value:
        keyboard.press(Keycode.KEYPAD_MINUS)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_MINUS)
        
    if btn_star.value:
        keyboard.press(Keycode.KEYPAD_ASTERISK)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_ASTERISK)
        
    if btn_forward_slash.value:
        keyboard.press(Keycode.KEYPAD_FORWARD_SLASH)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_FORWARD_SLASH)
        
    if btn_enter.value:
        keyboard.press(Keycode.KEYPAD_ENTER)
        time.sleep(sleep_time)
        keyboard.release(Keycode.KEYPAD_ENTER)

    time.sleep(sleep_time)
