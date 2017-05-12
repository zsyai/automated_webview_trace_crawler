from installer import *

ins = installer()
(apk_name, apk_entry, apk_package) = ins.getCurApp()

ins.uninstallApp(apk_package)