#!/usr/bin/python
#-*-coding:utf-8-*-

#检测百度百科重名条目

import re
import os
import sys



def process_repeatname(mat,out):
	#biaoti1=open("biaoti.txt",'w')
	#biaoti2=open("biaoti_rest.txt",'w')
	#loop=0
	global loop1
	loop1=0
	for i in mat:
		str_mat=re.compile('\|##').split(i)
		if re.compile('歌手|歌唱家|乐队|组合|成员|艺人|明星|音乐人|演奏家|钢琴师|音乐家|童星|快乐女声|超级女声|快乐男声|演奏员|歌唱演员').search(str_mat[0]):
			loop1+=1
			str_mat1=re.compile('\|').split(str_mat[0])
			outstr=str_mat1[0]+"|##"+str_mat[1]
			#biaoti1.write(str_mat[0]+'\n')
			out.append(outstr)
	#print loop
	#biaoti1.close()
	#biaoti2.close()
	return out










def main_process(baikedata,filename):
	global out
	out=[]
	out_repeat=[]
	out_pick=[]
	outfile=open(filename,'w')
	loop=0

	for eachbaike in baikedata:
		eachbaike=eachbaike.strip('\n')
		if re.compile('<biaoti>').search(eachbaike):
			loop+=1
			out_repeat.append(eachbaike)
			outfile.write(eachbaike+'\n')
		else:
			out.append(eachbaike)
	out=process_repeatname(out_repeat,out)



	print "%d duoyici occured,%d were appended"%(loop,loop1)

	outfile.close()
	return out








if __name__=='__main__':
	baikedata=open('jiexibaike.txt','r')
	shuchu=main_process(baikedata,'repeatName.txt')

