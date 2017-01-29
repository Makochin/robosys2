#!/usr/bin/env python

"""
MIT License

Copyright (c) 2017 Takuya Nogami

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import rospy
from std_msgs.msg import String

def change(morse_char):
	raw_morse = ""
	if morse_char == "a":
		raw_morse = ".-"
	elif morse_char == "b":
		raw_morse = "-..."
	elif morse_char == "c":
                raw_morse = "-.-."
        elif morse_char == "d":
                raw_morse = "-.."
        elif morse_char == "e":
                raw_morse = "."
        elif morse_char == "f":
                raw_morse = "..-."
        elif morse_char == "g":
                raw_morse = "--."
        elif morse_char == "h":
                raw_morse = "...."
        elif morse_char == "i":
                raw_morse = ".."
        elif morse_char == "j":
                raw_morse = "---."
        elif morse_char == "k":
                raw_morse = "-.-"
        elif morse_char == "l":
                raw_morse = ".-.."
        elif morse_char == "m":
                raw_morse = "--"
        elif morse_char == "n":
                raw_morse = "-."
        elif morse_char == "o":
                raw_morse = "---"
        elif morse_char == "p":
                raw_morse = ".--."
        elif morse_char == "q":
                raw_morse = "--.-"
        elif morse_char == "r":
                raw_morse = ".-."
        elif morse_char == "s":
                raw_morse = "..."
        elif morse_char == "t":
                raw_morse = "-"
        elif morse_char == "u":
                raw_morse = "..-"
        elif morse_char == "v":
                raw_morse = "...-"
        elif morse_char == "w":
                raw_morse = ".--"
        elif morse_char == "x":
                raw_morse = "-..-"
        elif morse_char == "y":
                raw_morse = "-.--"
        elif morse_char == "z":
                raw_morse = "--.."
	return raw_morse

def callback(msg):
	morse_msg = ""
	for char in msg.data:
		morse_msg += change(char.lower())+"   "
	print morse_msg

if __name__ == "__main__":
	rospy.init_node("morse_output")
	sub = rospy.Subscriber("morse_input", String, callback, queue_size=10)
	rospy.spin()
