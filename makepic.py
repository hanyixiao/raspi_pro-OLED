# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from PIL import Image
import cv2
import time
import SSD1306 as Adafruit_SSD1306
# Raspberry Pi pin configuration:
RST = 24
#init the device
disp = Adafruit_SSD1306.M096128x64_ssd1306(rst=RST) 
# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

cap = cv2.VideoCapture("test.mp4")

while(cap.isOpened()):
    ret,frame=cap.read()
   # cv2.imshow("vide0",frame)
    cv2.imwrite("temp.jpg",frame)
    img = Image.open("temp.jpg")
    img = img.resize((128,64))
    img = img.convert("1")
    disp.image(img)
    disp.display()
    img.save("temp.jpg")
    time.sleep(0.05)
    #if cv2.waitKey(40) & 0xff==ord('q'):
    #  break
cap.release()
#cv2.destroyAllWindows()

#img = Image.open("temp.jpg")
#img = img.rotate(90)
#img.show()
#img = img.resize((128,68))
#img = img.convert("1")
#img.show()
#img.save("coverted.jpg")
