from installer import *

ins = installer()
(apk_name, apk_entry, apk_package) = ins.getCurApp()

uninstallApp(apk_package)