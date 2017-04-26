import os
from sshcmd import *

class apkRepoMaintainer:
    def prefetch(self,apkname):
	apkrepolist = os.listdir('./ApkRepo/')
	if apkname in apkrepolist:
	    return
	else:
	    return
	    os.system('rm -rf ./ApkRepo/*')
	    index=apkname[0:3]
	    scpcmd('pkusei','162.105.175.15:~/wandoujia-apks/data/'+index+'*.apk','./ApkRepo/','pkucloud')
	    return


#a=apkRepoMaintainer()
#a.prefetch('022009aa19216a174ebb7fd5786c86ec.apk')
