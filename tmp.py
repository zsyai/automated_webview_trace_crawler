from apkList import *
from status import *
from apkDecompiler import *
from apkRepoMaintainer import *
from chromePage import *
import time

apklist = apkList().apks
apkdecompiler = apkDecompiler()

for i in range(480,600):
	print i
	apk = apklist[i]
	apkdecompiler.apktool(apk)
