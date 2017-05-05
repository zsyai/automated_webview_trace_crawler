import os
import time

class webviewHunter:
	def hunt(self):
		flag = 0
		while flag == 0:
			rt = os.popen('adb shell grep -a webview_devtools_remote /proc/net/unix').readlines()
			if len(rt) > 0:
				print "WEBVIEW FOUND!!!!!!!!!!!!!!!!!!!!!!!!!"
				break
			print "no webview"
			time.sleep(1)