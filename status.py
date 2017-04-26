import json
import copy

class status:
    def __init__(self):
	f=open('./status.json')
	self.statusinfo = json.load(f)
	f.close()

    def getcurrptr(self):
	return self.statusinfo['currptr']

    def setcurrptr(self,ptr):
	self.statusinfo['currptr']=ptr

    def save(self):
	f=open('./status.json','w')
	f.write(json.dumps(self.statusinfo))
	f.close()


#a=status()
#a.addcurrptr()
#a.save()
	
