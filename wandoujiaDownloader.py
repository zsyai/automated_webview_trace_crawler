import os
import urllib2
import json
import websocket
import time
import threading
import select


rt = urllib2.urlopen('http://localhost:9111/json/new', timeout=1000).read()

wsurl = json.loads(rt)['webSocketDebuggerUrl']
ws = websocket.WebSocket()
ws.connect(wsurl)

ws.send('{"id": 1, "method": "Page.navigate", "params": {"url": "http://www.wandoujia.com/top/app"}}')
for i in range(0,50):
	time.sleep(5)
	ws.send('{"id": 1, "method": "Runtime.evaluate", "params": {"expression":"document.getElementById(\'j-refresh-btn\').click()"}}')
for i in range(500,536):
	if i % 6 == 5:	
		time.sleep(180)
	ws.send('{"id": 1, "method": "Runtime.evaluate", "params": {"expression":"document.getElementById(\'j-top-list\').children['+str(i)+'].getElementsByTagName(\'a\')[5].click()"}}')





