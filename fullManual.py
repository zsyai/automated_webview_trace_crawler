from installer import *
from testRunner import *

ins = installer()
(apk_name, apk_entry, apk_package) = ins.installApp()

tr = testRunner()
tr.startTest(apk_entry, apk_name)

ins.uninstallApp(apk_package)