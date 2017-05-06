import os
import time

class webviewHunter:
	def hunt(self):
		flag = 0
		cnt = 0
		while True:
			rt = os.popen('adb shell grep -a webview_devtools_remote /proc/net/unix').readlines()
			if len(rt) > 0:
				print "WEBVIEW FOUND!!!!!!!!!!!!!!!!!!!!!!!!!"
				flag = 1
				break
			if cnt > 60:
				print "No WebView in this App"
				break
			# print "no webview"
			time.sleep(1)
			cnt = cnt + 1
		return flag