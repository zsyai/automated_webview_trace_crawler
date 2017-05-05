import os
import urllib2
import json
import websocket
import time
import threading
import select

class chromePage:
    def __init__(self):
	rt = os.popen('adb shell grep -a webview_devtools_remote /proc/net/unix').readlines()
	self.remoteport = rt[-1].replace('\r','').replace('\n','').split('_')[-1]
	self.localport = str(9222)
	os.system('adb forward tcp:'+self.localport+' localabstract:webview_devtools_remote_'+self.remoteport)
	rt = urllib2.urlopen('http://localhost:'+self.localport+"/json", timeout=1000).read()
	self.wsurl = json.loads(rt)[-1]['webSocketDebuggerUrl']
	self.ws = websocket.WebSocket()
	self.ws.connect(self.wsurl)

    def pTiming(self):
	self.ws.send('{"id": 1, "method": "Runtime.evaluate", "params": {"expression":"window.performance.timing", "includeCommandLineAPI": true, "returnByValue": true}}')
	result = self.ws.recv()
	# print result
	return result

    def navigate(self,url):
	self.ws.send('{"id": 1, "method": "Page.navigate", "params": {"url": "'+url+'"}}')

    def enableNetwork(self):
	self.ws.send('{"id": 1, "method": "Network.enable"}')

    def clearBrowserCache(self):
	self.ws.send('{"id": 1, "method": "Network.clearBrowserCache"}')

    def reloadPage(self,ignoreCache=False):
	if(ignoreCache):
	    self.ws.send('{"id": 1, "method": "Page.reload","params": {"ignoreCache": true}}')
	else:
	    self.ws.send('{"id": 1, "method": "Page.reload","params": {"ignoreCache": false}}')

    def refreshPage(self):
	self.ws.send('{"id": 1, "method": "Runtime.evaluate", "params": {"expression":"location.replace(location.href)"}}')

    def printdumpMessage(self):
	ready = select.select([self.ws],[],[],5)
	while (ready[0]):
	    print self.ws.recv()
	    ready = select.select([self.ws],[],[],5)

    def dumpMessage(self,path):
	requestlist=[]	
	f = open(path+'_trace', 'w')
	ready = select.select([self.ws],[],[],5)
	while (ready[0]):
	    rs = self.ws.recv()
	    jsonrs = json.loads(rs)
	    if(jsonrs.has_key('method') and jsonrs['method']=='Network.loadingFinished'):
	        requestlist.append(jsonrs['params']['requestId'])
	    f.write(rs)
	    ready = select.select([self.ws],[],[],5)
	
	for requestid in requestlist:
	    self.ws.send('{"id": 1, "method": "Network.getResponseBody", "params": {"requestId": "'+requestid+'"}}')
	    f2 = open(path+'_'+requestid, 'w')
	    f2.write(self.ws.recv())
	    f2.close()
	f.close
	
	
#a = chromePage()
#a.enableNetwork()
#a.reloadPage()
#a.dumpMessage('./TrafficTrace/a.txt')



