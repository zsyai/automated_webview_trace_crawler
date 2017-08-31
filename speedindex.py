import os
import os.path
import json
import time
import datetime
import sys

rootdir = './TrafficTrace1/'
cnt = 1
num = 1
total = 0
starttime = datetime.datetime(2017,5,14,12,0,0)
havedone = os.listdir('./SpeedIndex')
for i in range(0, len(havedone)):
	(havedone[i], tmp) = os.path.splitext(havedone[i])

for dirname in os.listdir('./TrafficTrace1'):
	print dirname
	# fout = open('shift.txt', 'w')
	# if num < 101:
	# 	num = num + 1
	# 	continue
	if cnt > 20:
		break
	if dirname == ".DS_Store":
		continue
	if dirname in havedone:
		continue
	ctime = time.ctime(os.path.getctime('./TrafficTrace1/'+dirname))
	cdate = time.strptime(ctime,"%a %b %d %H:%M:%S %Y")
	# print cdate
	cdate = datetime.datetime(cdate[0],cdate[1],cdate[2],cdate[3],cdate[4],cdate[5])
	if (cdate - starttime).days > 1:
		os.system('python ./visualmetrics-master/visualmetrics.py --video ./TrafficTrace1/'+dirname+'/test.mp4 --start 0 --end 30 --json >result.json')
		fspeed = open('result.json')
		speedjson = json.load(fspeed)
		fspeed.close()
		delta = speedjson["FirstVisualChange"]
	else:
		delta = -600
	print 'delta = ', delta
	timeline = open('./TrafficTrace1/'+dirname+'/timeLine.json')
	timejson = json.load(timeline)
	timeline.close()
	activities = timejson["times"]
	length = len(activities)
	for i in range(0, length):
		try:
			if i == 0:
				continue
			elif i < length - 2:
				start = int(activities[i]["start"] * 1000 + delta)
				end = int(activities[i]["end"] * 1000 + delta)
				if end < 0:
					end = end - start
					start = 0
				elif start < 0:
					start = 0
				os.system('python ./visualmetrics-master/visualmetrics.py --video ./TrafficTrace1/'+dirname+'/test.mp4 --start '+str(start)+' --end '+str(end)+' --json >result.json')
				fspeed = open('result.json')
				speedjson = json.load(fspeed)
				fspeed.close()
				activities[i]["speedindex"] = speedjson
			elif i == length - 2:
				start = activities[i]["start"]
				end = activities[i]["end"]
				if (activities[i+1]["start"] < start):
					start = activities[i+1]["start"]
				if (activities[i+1]["end"] > end):
					end = activities[i+1]["end"]
				start = int(start * 1000 + delta)
				end = int(end * 1000 + delta)
				os.system('python ./visualmetrics-master/visualmetrics.py --video ./TrafficTrace1/'+dirname+'/test.mp4 --start '+str(start)+' --end '+str(end)+' --json >result.json')
				fspeed = open('result.json')
				speedjson = json.load(fspeed)
				fspeed.close()
				activities[i]["speedindex"] = speedjson
		except:
			info = sys.exc_info()
			print info[0],":",info[1]

	timejson = {}
	timejson["times"] = activities
	timejson = json.dumps(timejson, indent=4)
	with open('./SpeedIndex/'+dirname+'.json', 'w') as f:
		f.write(timejson)

	cnt = cnt + 1