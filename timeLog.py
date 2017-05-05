import os
import datetime
import time
import json

class timeLog:
	def readLog(self, dictname, webjson):
		result = []
		item = {}
		sstart = 0
		with open(dictname+'/log.txt') as f:
			lines = f.readlines()
			for line in lines:
				onelog = line.split(' ')
				if len(onelog) < 5:
					continue
				if 'START' in onelog:
					for log in onelog:
						if log.find('cmp=') >= 0:
							activity = log.replace('cmp=', '')
							activity = activity.replace('{', '')
							activity = activity.replace('}', '')
							tmp = activity.split('/')
							item["fullName"] = activity
							item['package'] = tmp[0]
							item['activity'] = tmp[1].strip('.')
							break
					now = datetime.datetime.strptime('2017-'+onelog[0]+' '+onelog[1],'%Y-%m-%d %H:%M:%S.%f')
					start = now
					# if sstart == 0:
					# 	sstart = now
					# item["start"] = (start - sstart).total_seconds()
				elif 'Displayed' in onelog:
					now = datetime.datetime.strptime('2017-'+onelog[0]+' '+onelog[1],'%Y-%m-%d %H:%M:%S.%f')
					for log in onelog:
						if log.find('+') >= 0:
							during = log.replace('\n','').replace('\r', '')
							during = during.replace('+', '').replace('ms', '')
							if during.find('s') > 0:
								print 'hhhhhh'
								during = during.replace('s', '.')
								during = float(during)
							else:
								during = float(during) / 1000
					if sstart == 0:
						sstart = start
					item["start"] = (start - sstart).total_seconds()
					item["end"] = (now - sstart).total_seconds()
					item["sysDuring"] = during
					result.append(item)
					item = {}

		weblog = json.loads(webjson)
		weblog = weblog["result"]
		weblog = weblog["result"]
		value = weblog["value"]

		start = value["fetchStart"]
		mstart = start % 1000
		start = start / 1000
		start = datetime.datetime.fromtimestamp(start) + datetime.timedelta(microseconds=mstart*1000)
		end = value["loadEventEnd"]
		mend = end % 1000
		end = end / 1000
		end = datetime.datetime.fromtimestamp(end) + datetime.timedelta(microseconds=mend*1000)

		item = {}
		item["fullName"] = "WebView"
		item["start"] = (start - sstart).total_seconds()
		item["end"] = (end - sstart).total_seconds()
		item["sysDuring"] = (end - start).total_seconds()
		result.append(item)

		timejson = {}
		timejson["times"] = result
		timejson = json.dumps(timejson, indent=4)
		with open(dictname+'/timeLine.json', 'w') as f:
			f.write(timejson)
		return result

