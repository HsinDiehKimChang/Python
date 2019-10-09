#20190326
#Assignment 9

#import module
import datetime
import urllib.request
import os


def function1(str1):
	fullURL="http://"+str1

	try:
		webUrl=urllib.request.urlopen(fullURL)
		print("URL Valid")
		return fullURL

	except Exception:
		return "ERROR"


def function2(str2):
	webUrl=urllib.request.urlopen(str2)
	file1=open("E:\\python\\Self_practice\\9.txt",'w')
	file1.write(str(webUrl.read()))
	file1.close()

	file1=open("E:\\python\\Self_practice\\9.txt",'a')
	file1.write(str(datetime.datetime.now()))
	file1.close()


def function3(str3):
	webUrl=urllib.request.urlopen(str3)
	file1=open("E:\\python\\Self_practice\\9.txt",'r')
	data=file1.read(10)
	file1.close()
	print(data)
	print("File Successfully Saved")


print("Please input a URL:")
userURL=input()

count=1

flag=function1(userURL)

#print(flag)
while flag=="ERROR" and count<3:
	print("Please input another URL:")
	userURL=input()
	count+=1

if count==3:
	print("Sorry, You have tried 3 times. The program have to end")

elif  flag!="ERROR":
	function2(flag)
	function3(flag)