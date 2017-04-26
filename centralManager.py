from apkList import *
from status import *
from apkDecompiler import *
from apkRepoMaintainer import *

apklist = apkList().apks
status = status()
apkrepomaintainer = apkRepoMaintainer()
apkdecompiler = apkDecompiler()


currptr = status.getcurrptr()
apk = apklist[currptr]
print "prefeching "+apk
apkrepomaintainer.prefetch(apk)
print "decompiling"
apkdecompiler.apktool(apk)
apk_package = apkdecompiler.getpackage(apk)
apk_entry = apkdecompiler.getentry(apk)
apk_name = apkdecompiler.getname(apk)
print "apkname: "+apk_name
print "apkpackage: "+apk_package
print "apkentry: "+apk_entry

print "installing"
os.popen("adb install ./ApkRepo/"+apk+" 2>/dev/null")

#start simplewebcrawler
os.system("adb shell am instrument -e target "+apk_package+" -e task record -w com.liang.simpleappcrawler.test/android.support.test.runner.AndroidJUnitRunner")
print "adb shell am instrument -e target "+apk_package+" -e task record -w com.liang.simpleappcrawler.test/android.support.test.runner.AndroidJUnitRunner"
#replay
#os.system("adb shell am instrument -e target "+apk+" -e task replay -w com.liang.simpleappcrawler.test/android.support.test.runner.AndroidJUnitRunner")

os.system('mkdir ./TrafficTrace/'+apk_name)
#first visit
cp = chromePage()
cp.enableNetwork()
cp.clearBrowserCache()
cp.reloadPage(ignoreCache=True)
cp.dumpMessage('./TrafficTrace/'+apk_name+'/first')
#second visit
cp.reloadPage(ignoreCache=False)
cp.dumpMessage('./TrafficTrace/'+apk_name+'/secod')

#enable chrome remote debugger
currptr+=1
status.setcurrptr(currptr)
