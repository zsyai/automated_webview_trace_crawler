import os
import os.path
import json

rootdir = './TrafficTrace/'
fout = open ('timelines.csv', 'w')
title = "NO,APK_NAME,ACTIVITY,START,END,HAS WEBVIEW,WEBVIEW START,WEBVIEW END,URL\n"
fout.write(title)
cnt = 1
for dirname in os.listdir('./TrafficTrace'):
	if dirname == ".DS_Store":
		continue
	title = dirname
	dirname = rootdir + dirname
	url = open(dirname+'/url.txt').readline()
	timeline = open(dirname+'/timeLine.json')
	timeline = json.load(timeline)
	result = ""
	for activity in timeline["times"]:
		if activity["fullName"] == "WebView":
			result = result + ",yes," + str(activity["start"]) + "," + str(activity["end"]) + "," + url + "\n"
			fout.write(result)
			break
		elif result != "":
			result = result + ",no,,,\n"
			fout.write(result)
			result = ",," + activity["activity"] + "," + str(activity["start"]) + "," + str(activity["end"])
		else:
			result = str(cnt) + "," + title + "," + activity["activity"] + "," + str(activity["start"]) + "," + str(activity["end"])
	print dirname
	cnt = cnt + 1

fout.close()