import os
import time
import urllib2
import json

class webviewHunter:
	def hunt(self):
		flag = 0
		cnt = 0
		rt = os.popen('adb shell grep -a webview_devtools_remote /proc/net/unix').readlines()
		print rt
		index = len(rt) - 1
		portindex = 9222
		while index >= 0:
			self.remoteport = rt[index].replace('\r','').replace('\n','').split('_')[-1]
			self.localport = str(portindex)
			os.system('adb forward tcp:'+self.localport+' localabstract:webview_devtools_remote_'+self.remoteport)
			rtt = urllib2.urlopen('http://localhost:'+self.localport+"/json", timeout=1000).read()
			rtjson = json.loads(rtt)
			if len(rtjson) > 0:
				print "WEBVIEW FOUND!!!!!!!!!!!!!!!!!!!!!!!!!"
				flag = 1
				return flag
			else:
				print "no webview"
			index = index - 1
			portindex = portindex + 1
		cnt = cnt + 1
		while True:
			# if cnt == 0:
			# 	rt = os.popen('adb shell grep -a webview_devtools_remote /proc/net/unix').readlines()
			# 	index = len(rt) - 1
			# 	portindex = 9222
			# 	while index >= 0:
			# 		self.remoteport = rt[index].replace('\r','').replace('\n','').split('_')[-1]
			# 		self.localport = str(portindex)
			# 		os.system('adb forward tcp:'+self.localport+' localabstract:webview_devtools_remote_'+self.remoteport)
			# 		rtt = urllib2.urlopen('http://localhost:'+self.localport+"/json", timeout=1000).read()
			# 		rtjson = json.loads(rtt)
			# 		if len(rtjson) > 0:
			# 			print "WEBVIEW FOUND!!!!!!!!!!!!!!!!!!!!!!!!!"
			# 			flag = 1
			# 			break
			# 		index = index - 1
			# 		portindex = portindex + 1
			# else:
			tmp = os.popen('adb shell grep -a webview_devtools_remote /proc/net/unix').readlines()
			newport = [a for a in tmp if a not in rt]
			print newport
			index = len(newport) - 1
			while index >= 0:
				self.remoteport = newport[index].replace('\r','').replace('\n','').split('_')[-1]
				self.localport = str(portindex)
				os.system('adb forward tcp:'+self.localport+' localabstract:webview_devtools_remote_'+self.remoteport)
				rtt = urllib2.urlopen('http://localhost:'+self.localport+"/json", timeout=1000).read()
				rtjson = json.loads(rtt)
				if len(rtjson) > 0:
					print "WEBVIEW FOUND!!!!!!!!!!!!!!!!!!!!!!!!!"
					flag = 1
				else:
					print "no webview"
				index = index - 1
				portindex = portindex + 1
			rt = list(set(rt).union(set(tmp)))
			if flag == 1:
				break
			if cnt > 60:
				print "No WebView in this App"
				break
			# print "no webview"
			time.sleep(2)
			cnt = cnt + 1
		return flag