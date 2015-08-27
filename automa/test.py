# windows GUI test tool
# http://www.getautoma.com/ 
#
import time

while True:
    # control panel
    start("control")
    time.sleep(3) 
    click("Network and Internet")
    time.sleep(3) 
    press(ALT + "F4")
    time.sleep(3) 
    start("control")
    time.sleep(3) 
    click("Programs")
    press(ALT + "F4")
    time.sleep(3) 
    # click my computer directory
    start("computer")
    time.sleep(3) 
    click("Downloads")
    time.sleep(3) 
    click("Documents") 
    time.sleep(3) 
    click("Music") 
    time.sleep(3) 
