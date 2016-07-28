#!/bin/bash

# 获取第一个参数为apk名
if [ x$1 == x ];then
	echo "please input apk file name."
	exit
fi
ApkName=$1

# 获取当前绝对目录
rootpath=$(cd "$(dirname "$0")"; pwd)

# 设置压缩软件目录，去掉apk文件扩展名
OutputDir=$rootpath/output/${ApkName%.apk}/

if [ -d $OutputDir ];then
	rm -R $OutputDir
fi

echo "********************************"
echo "正在反编译资源..."

java -jar $rootpath/Apktool/apktool.jar d -f -o $OutputDir $ApkName

echo "********************************"
echo "正在解压缩classes.dex文件..."

unzip $ApkName classes.dex -d $OutputDir

echo "********************************"
echo "正在反编译classes.dex文件..."

cd dex2jar
./d2j-dex2jar.sh ${OutputDir}classes.dex -o ${OutputDir}src.jar -f

# 打开反编译后的目录
open $OutputDir
echo "输出目录："$OutputDir