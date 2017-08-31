import os
import os.path
import json

rootdir = './TrafficTrace/'
cnt = 1
total = 0
for dirname in os.listdir('./TrafficTrace'):
	if cnt > 10:
		break
	if dirname == ".DS_Store":
		continue
	timeline = open('./TrafficTrace'+dirname+'/timeLine.json')
	timejson = json.load(timeline)
	timeline.close()
	activitys = timejson["times"]
	if activitys[1]["fullName"] != "WebView":
		start = activitys[1]["start"] * 1000
		end = activitys[1]["end"] * 1000
		minindex = 1000000
		for i in range(0,8):
			print start, end
			os.system('python ./visualmetrics-master/visualmetrics.py --video ./TrafficTrace/'+dirname+'/test.mp4 --start '+str(start)+' --end '+str(end)+' --json >result.json')
			fspeed = open('result.json')
			speedjson = json.load(fspeed)
			fspeed.close()
			print speedjson
			speedindex = speedjson["SpeedIndex"]
			if speedindex < minindex:
				minindex = speedindex
				shift = i
			start = start - 200
			end = end - 200
	print 'App Name:', dirname
	print 'min index:', speedindex
	print 'shift', str(shift * 200)
	total = total + shift
	cnt = cnt + 1

print 'average shift:', 200*total/(cnt-1)