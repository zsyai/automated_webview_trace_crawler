from apkList import *
from status import *
from apkDecompiler import *
from apkRepoMaintainer import *

class installer:
	def __init__(self):
		self.apklist = apkList().apks
		self.status = status()
		self.apkrepomaintainer = apkRepoMaintainer()
		self.apkdecompiler = apkDecompiler()
		self.currptr = 0
		self.apk_name = ''

	def getCurApp(self):
		self.currptr = int(self.status.getcurrptr())
		print "currptr "+ str(self.currptr)
		apk = self.apklist[self.currptr]
		print "prefeching "+apk
		self.apkrepomaintainer.prefetch(apk)
		print "decompiling"
		#apkdecompiler.apktool(apk)
		apk_package = self.apkdecompiler.getpackage(apk)
		apk_entry = self.apkdecompiler.getentry(apk)
		apk_name = self.apkdecompiler.getname(apk)
		print "apkname: "+apk_name
		print "apkpackage: "+apk_package
		print "apkentry: "+apk_entry

		return (apk_name, apk_entry, apk_package)

	def installApp(self):
		(apk_name, apk_entry, apk_package) = self.getCurApp()

		print "installing"
		os.popen("adb install ./ApkRepo/"+apk+" 2>/dev/null")

		return (apk_name, apk_entry, apk_package)


	def uninstallApp(self, apk_package):
		print 'adb uninstall '+apk_package+' 2>/dev/null'
		os.popen('adb uninstall '+apk_package+' 2>/dev/null')
		self.currptr = self.currptr+1
		self.status.setcurrptr(self.currptr)
		self.status.save()

