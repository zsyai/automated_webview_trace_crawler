class apkList:
    def __init__(self):
	self.apks=[]

	f = open("./apklist.txt")
	while True:
    	    line = f.readline()
    	    if not line:
        	break
	    self.apks.append(line.replace('\r','').replace('\n',''))


#print len(apkList().apks)
