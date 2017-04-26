import os
from androidManifest import *

class apkDecompiler:
    def apktool(self, apkname):
	print './Tools/apktool d -f -s ./ApkRepo/'+apkname+' -o ./ApkRepo/'+apkname.split('.')[0]
	if(apkname.split('.')[0] == 'com' or apkname.split('.')[0]=='cn'):
		os.system('./Tools/apktool d -f -s ./ApkRepo/'+apkname+' -o ./ApkRepo/'+apkname.split('.')[0]+apkname.split('.')[1]+apkname.split('.')[2])
	else:
		os.system('./Tools/apktool d -f -s ./ApkRepo/'+apkname+' -o ./ApkRepo/'+apkname.split('.')[0])

    def getentry(self, apkname):
	if(apkname.split('.')[0] == 'com' or apkname.split('.')[0]=='cn'):
		am = androidManifest('./ApkRepo/'+apkname.split('.')[0]+apkname.split('.')[1]+apkname.split('.')[2]+'/AndroidManifest.xml')
	else:
		am = androidManifest('./ApkRepo/'+apkname.split('.')[0]+'/AndroidManifest.xml')
	return am.getpackage()+'/'+am.getmainactivity()

    def getpackage(self, apkname):
	if(apkname.split('.')[0] == 'com' or apkname.split('.')[0]=='cn'):
		am = androidManifest('./ApkRepo/'+apkname.split('.')[0]+apkname.split('.')[1]+apkname.split('.')[2]+'/AndroidManifest.xml')
	else:
		am = androidManifest('./ApkRepo/'+apkname.split('.')[0]+'/AndroidManifest.xml')
	return am.getpackage()

    def getname(self,apkname):
	if(apkname.split('.')[0] == 'com' or apkname.split('.')[0]=='cn'):
		am = androidManifest('./ApkRepo/'+apkname.split('.')[0]+apkname.split('.')[1]+apkname.split('.')[2]+'/AndroidManifest.xml')
	else:
		am = androidManifest('./ApkRepo/'+apkname.split('.')[0]+'/AndroidManifest.xml')
	return am.getpackage()+'_'+am.getmainactivity()+'_'+am.getversioncode()+'_'+am.getversionname()
	



#a=apkDecompiler()
#print a.getname('022b1fa29e9e13fcfb64cec3d4e3e892.apk')
