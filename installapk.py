#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import re

def reinstall(apkPath, packageName, needUninstall):
	if (needUninstall and len(packageName) > 0 and os.popen('adb shell pm path ' + packageName).readlines()) :
		print '====== 卸载Apk ======'
		os.system('adb uninstall ' + packageName)
	print '====== 安装Apk ======'
	os.system('adb install -r ' + apkPath)

def main():
	if (len(sys.argv) <= 1):
		print 'usage: python installapk.py apkPath'
		exit()
	print '====== 解析Apk ======'
	packageName = ''
	launchActivity = ''
	apkPath = sys.argv[len(sys.argv) - 1]

	justReplace = False
	if len(sys.argv) >= 3 :
		for i in range(1, len(sys.argv) - 1):
			args = sys.argv[i]
	    	if args == '-r':
				justReplace = True

	originPackageInfo = os.popen('aapt d badging ' + apkPath + ' | grep package').readlines()

	pattern = re.compile(r'\'\S*\'')
	match = pattern.search(originPackageInfo[0])
	if match:
		packageName = match.group().replace('\'', '')
		print 'packageName = ' + packageName

	originActivityInfo = os.popen('aapt d badging ' + apkPath + ' | grep launchable-activity').readlines()
	pattern = re.compile(r'\'\S*\'')
	match = pattern.search(originActivityInfo[0])
	if match:
		launchActivity = match.group().replace('\'', '')
		print 'launchActivity = ' + launchActivity

	reinstall(apkPath, packageName, not justReplace)
	if (len(packageName) > 0 and len(launchActivity) > 0):
		print '====== 启动' + packageName + ' ======'
		os.system('adb shell am start -n ' + packageName + '/' + launchActivity)
	else:
		print '解析包名或Activity名失败，无法启动App'

if __name__ == '__main__':
    main()