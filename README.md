# raspi_pro-OLED
this is a project you can drive the oled by using the rasberry pi 4 and oled M096128x64 which you can buy very chip in China
which I use can be buy in tabao 
# how to start
you can watch the https://shumeipai.nxez.com/2019/04/29/use-the-ssd1306-oled-display-on-the-raspberry-pi.html 
the method is very like the blogs says but actully I changed the source code to fix my platform 
that blog is just suitable for its plat
# frist
make sure you IO connet is corect you can see https://shumeipai.nxez.com/raspberry-pi-pins-version-40 
in my project my IO connect is 

                          OLED's | vcc |gnd |SDA  |SCL
                 rasberry pi 4's | 3v3 |gnd |SDA1 |SCL1
# second
make sure you rasberry pi 4 's IIC function is enabled 
you can do like this

   sudo apt-get install -y python-smbus
   sudo apt-get install -y i2c-tools
   sudo raspi-config
more details you can see the blog https://shumeipai.nxez.com/2019/04/29/use-the-ssd1306-oled-display-on-the-raspberry-pi.html
# third
install the PIL library by using 
  sudo apt-get install python-pil python3-pil 
which is needed for all codes
then
install the opencv-python by using
    
    sudo apt-get update
    sudo apt-get install libjpeg-dev
    
    sudo apt-get install libatlas-base-dev
    sudo apt-get install libjpeg-dev
    
    sudo apt-get install libtiff5-dev
    sudo apt-get install li.jpg12-dev
    
    sudo apt-get install libqtgui4 libqt4-test
    sudo apt-get install libjasper-dev

    sudo apt-get install libopencv-dev
    sudo apt-get install opencv-python

if you stil have troubles you can see this https://www.jianshu.com/p/56929416b4a1

# how to run it
make sure your enviroment is ok
git clone the code 
cd raspi_pro-OLED
python ***.py
*** is which app you want 
# introduce
animate.py:comes some chars in you screen
shapes.py:some shapes like RECT triangle 
image.py:you can load any img in your screen 
makepic.py:you can add a video test.mp4 to play on you screen
stats.py:this can show some messsage about you rasberrypi4 such as time cpu temperature disk
 
