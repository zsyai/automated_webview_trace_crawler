import os
import time
from subprocess import Popen
from chromePage import *
from timeLog import *
from webviewHunter import *
from installer import *

# apk_entry = "com.example.webview/.MainActivity"
# apk_name = "com.example.webview"
# apk_entry = "pku.sei.restaurants/.MainActivity"
# apk_name = "pku.sei.restaurants"
# apk_entry = "ctrip.android.view/.splash.CtripSplashActivity"
# apk_name = "ctrip.android.view"
# apk_entry = "viva.reader/.activity.GuidanceExActivity"
# apk_name = "viva.reader"
ins = installer()
(apk_name, apk_entry, apk_package) = ins.getCurApp()

print 'clear logcat'
os.system("adb logcat -c")
time.sleep(2)
print 'start screenrecording'
pscshot = Popen("adb shell screenrecord --time-limit 120 /sdcard/test.mp4", shell= True)
print 'start app'
os.popen("adb shell am start -n "+apk_entry)

raw_input()

print 'start evaluateing'
# hunter = webviewHunter()
# flag = hunter.hunt()

os.system('rm -rf ./TrafficTrace/'+apk_name)
os.system('mkdir ./TrafficTrace/'+apk_name)
# time.sleep(2)
pscshot.send_signal(2)
print "pull logcat"
process = Popen("adb logcat -v time -s ActivityManager >./TrafficTrace/"+apk_name+"/log.txt", shell= True)
# process = Popen("adb logcat -v time -s ActivityManager >./log.txt", shell= True)
time.sleep(1)
process.send_signal(2)
time.sleep(1)

# os.popen("adb pull /sdcard/test.mp4")
print "pull screenrecording"
os.popen("adb pull /sdcard/test.mp4 ./TrafficTrace/"+apk_name)

cp = chromePage()
webtiming = cp.pTiming()
# print webtiming
log = timeLog()
# timeline = log.readLog(".", webtiming)
timeLine = log.readLog("./TrafficTrace/"+apk_name, webtiming)
print 'timeLine:', timeline
url = cp.getURL()
with open("./TrafficTrace/"+apk_name+"/url.txt", 'w') as f:
	f.write(url)
print 'url = ', url

print "first visit"
# cp = chromePage()
cp.enableNetwork()
cp.clearBrowserCache()
cp.reloadPage(ignoreCache=True)
cp.dumpMessage('./TrafficTrace/'+apk_name+'/first')
#second visit
print "second visit"
cp.refreshPage()
cp.dumpMessage('./TrafficTrace/'+apk_name+'/second')

os.popen("adb shell am force-stop "+apk_name)