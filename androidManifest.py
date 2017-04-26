import xml.dom.minidom 

class androidManifest:
    def __init__(self, path):
	self.DOMTree = xml.dom.minidom.parse(path) 
	self.manifest = self.DOMTree.documentElement

    def getpackage(self):
	return self.manifest.getAttribute('package')

    def getversioncode(self):
	return self.manifest.getAttribute('android:versionCode')

    def getversionname(self):
	return self.manifest.getAttribute('android:versionName')

    def getmainactivity(self):
	activitylist = self.manifest.getElementsByTagName('application')[0].getElementsByTagName('activity')
	for activity in activitylist:
	    intentfilterlist = activity.getElementsByTagName('intent-filter')
	    if(len(intentfilterlist))==0:
		continue
	    for intentfilter in intentfilterlist:
		if len(intentfilter.getElementsByTagName('category'))>0 and intentfilter.getElementsByTagName('category')[0].getAttribute('android:name')=="android.intent.category.LAUNCHER":
	    	    return activity.getAttribute('android:name')


  
#a=androidManifest('/home/liang/Desktop/500app/ApkRepo/022b1fa29e9e13fcfb64cec3d4e3e892/AndroidManifest.xml')
#print a.getmainactivity()
