from apkList import *
from status import *
from apkDecompiler import *
from apkRepoMaintainer import *
from chromePage import *
from timeLog import *
from webviewHunter import *
import time

apklist = apkList().apks
status = status()
apkrepomaintainer = apkRepoMaintainer()
apkdecompiler = apkDecompiler()
currptr = 0

while True:
	apk_name = ''
	try:
		currptr = int(status.getcurrptr())
		print "currptr "+ str(currptr)	
		
		apk = apklist[currptr]
		print "prefeching "+apk
		apkrepomaintainer.prefetch(apk)
		print "decompiling"
		#apkdecompiler.apktool(apk)
		apk_package = apkdecompiler.getpackage(apk)
		apk_entry = apkdecompiler.getentry(apk)
		apk_name = apkdecompiler.getname(apk)
		print "apkname: "+apk_name
		print "apkpackage: "+apk_package
		print "apkentry: "+apk_entry

		print "installing"
		os.popen("adb install ./ApkRepo/"+apk+" 2>/dev/null")
		
		print "clear logcat"
		os.system("adb logcat -c")
		time.sleep(1)
		print "start screenrecording"
		pscshot = Popen("adb shell screenrecord /sdcard/test.mp4", shell= True)
		print "opening app on mobile"
		os.popen("adb shell am start -n "+apk_entry)

		#start simplewebcrawler
		# os.system("adb shell am instrument -e target "+apk_package+" -e task record -w com.liang.simpleappcrawler.test/android.support.test.runner.AndroidJUnitRunner")
		#print "adb shell am instrument -e target "+apk_package+" -e task record -w com.liang.simpleappcrawler.test/android.support.test.runner.AndroidJUnitRunner"
		#replay
		# os.system("adb shell am instrument -e target "+apk+" -e task replay -w com.liang.simpleappcrawler.test/android.support.test.runner.AndroidJUnitRunner")

		# raw_input()
		hunter = webviewHunter()
		hunter.hunt()
		time.sleep(1)

		os.system('rm -rf ./TrafficTrace/'+apk_name)
		os.system('mkdir ./TrafficTrace/'+apk_name)
		# stop screen recording
		pscshot.send_signal(2)
		print "pull logcat"
		process = Popen("adb logcat -v time -s ActivityManager >./TrafficTrace/"+apk_name+"/log.txt", shell= True)
		time.sleep(1)
		process.send_signal(2)
		# pscshot.send_signal(2)
		time.sleep(1)
		print "pull screenrecording"
		os.popen("adb pull /sdcard/test.mp4 ./TrafficTrace/"+apk_name)
		
		cp = chromePage()
		webtiming = cp.pTiming()
		log = timeLog()
		timeLine = log.readLog("./TrafficTrace/"+apk_name, webtiming)
		url = cp.getURL()
		with open("./TrafficTrace/"+apk_name+"/url.txt", 'w') as f:
			f.write(url)
		print 'url = ', url

		#first visit
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

		print "force-stop"
		os.popen("adb shell am force-stop "+apk_name)
		print "uninstalling"
		print 'adb uninstall '+apk_package+' 2>/dev/null'
		os.popen('adb uninstall '+apk_package+' 2>/dev/null')
		currptr=currptr+1
		status.setcurrptr(currptr)
		status.save()
	except:
		if apk_name != '':
			os.system('rm -rf ./TrafficTrace/'+apk_name)
		print "error uninstalling"
		print 'error adb uninstall '+apk_package+' 2>/dev/null'
		os.popen('adb uninstall '+apk_package+' 2>/dev/null')
		currptr=currptr+1
		status.setcurrptr(currptr)
		status.save()

