import os
import time
from subprocess import Popen
from chromePage import *
from timeLog import *
from webviewHunter import *

# apk_entry = "com.example.webview/.MainActivity"
# apk_name = "com.example.webview"
apk_entry = "pku.sei.restaurants/.MainActivity"
apk_name = "pku.sei.restaurants"

os.system("adb logcat -c")
time.sleep(2)
# pscshot = Popen("adb shell screenrecord /sdcard/test.mp4", shell= True)
os.popen("adb shell am start -n "+apk_entry)

# raw_input()
hunter = webviewHunter()
hunter.hunt()

process = Popen("adb logcat -v time -s ActivityManager >./log.txt", shell= True)
time.sleep(1)
process.send_signal(2)
# pscshot.send_signal(2)
time.sleep(1)

# os.popen("adb pull /sdcard/test.mp4")

cp = chromePage()
webtiming = cp.pTiming()
# print webtiming
log = timeLog()
timeline = log.readLog(".", webtiming)
print timeline

os.popen("adb shell am force-stop "+apk_name)