import os
import os.path
import json

rootdir = './TrafficTrace/'
fout = open ('timelines.csv', 'w')
title = "NO,APK_NAME,ACTIVITY,START,END,SPEEDINDEX,HAS WEBVIEW,WEBVIEW START,WEBVIEW END,URL\n"
fout.write(title)
cnt = 1
for dirname in os.listdir('./TrafficTrace'):
	if dirname == ".DS_Store":
		continue
	print dirname
	title = dirname
	timeline = open('SpeedIndex/'+dirname+'.json')
	timeline = json.load(timeline)
	dirname = rootdir + dirname
	url = open(dirname+'/url.txt').readline()
	result = ""
	for activity in timeline["times"]:
		if "fullName" in activity and activity["fullName"] == "WebView":
			result = result + ",yes," + str(activity["start"]) + "," + str(activity["end"]) + "," + url + "\n"
			fout.write(result)
			break
		elif result != "" and "activity" in activity:
			result = result + ",no,,,\n"
			fout.write(result)
			result = ",," + activity["activity"] + "," + str(activity["start"]) + "," + str(activity["end"]) + ","
			if "speedindex" in activity:
				result = result + str(activity["speedindex"]["SpeedIndex"]) 
		else:
			result = str(cnt) + "," + title + ","
			if "activity" in activity:
				result = result + activity["activity"]
			result = result + "," + str(activity["start"]) + "," + str(activity["end"]) + ","
	cnt = cnt + 1

fout.close()