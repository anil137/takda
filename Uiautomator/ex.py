from uiautomator import Device
d = Device('emulator-5554')
print(d.info)
#d.press.home()
#d(0).up(0)
#d.orientation = "r"
#d(scrollable=True).scroll(steps=10)
#d.swipe(0,0,1440, 2392)
d.press.down()
d.press.back()