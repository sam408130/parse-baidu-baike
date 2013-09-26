#!/usr/bin/python
#-*-coding:utf-8-*-


import re
import os
import sys
import string



def cal_percent(num1,num2,type1):
  per=float(num1)/float(num2)
  percent=format(per, '.2%')
  #outfile.write("%s      %s"%(type1,percent)+'\n')
  print "%s      %s"%(type1,percent)


def main_process(outmat):
	global out
	out=[]
	global loop_hasname
	loop_hasname=0
	global loop_hasbirthday
	loop_hasbirthday=0
	global loop_hasnickname
	loop_hasnickname=0
	global loop_creatdate
	loop_creatdate=0
	global loop_hasgender
	loop_hasgender=0
	global loop_hasenglishname
	loop_hasenglishname=0
	global loop_belongregion
	loop_belongregion=0
	global loop_hasusedname
	loop_hasusedname=0 
	global loop_haslanguage
	loop_haslanguage=0   
	global loop_hasgenera
	loop_hasgenera=0  
	global loop_belongcompany
	loop_belongcompany=0
	global loop_career
	loop_career=0
	global loop_nation
	loop_nation=0
	global loop_school
	loop_school=0
	global loop_achievement
	loop_achievement=0  
	global loop_height
	loop_height=0  
	global loop_constellation
	loop_constellation=0
	global loop_weight
	loop_weight=0
	global loop_bloodtype
	loop_bloodtype=0
	global loop_zodiac
	loop_zodiac=0 
	global loop_specialty
	loop_specialty=0
	global loop_belief
	loop_belief=0
	global loop_ancestralhome
	loop_ancestralhome=0
	global loop_hobby
	loop_hobby=0
	global loop_fansname
	loop_fansname=0
	global loop_size
	loop_size=0
	global loop_location
	loop_location=0
	global loop_familymembers
	loop_familymembers=0
	global loop_introduction
	loop_introduction=0
	loop1=len(outmat)
	for each in outmat:
		if re.compile('hasName').search(each):
			loop_hasname+=1
		if re.compile('hasBirthday').search(each):
			loop_hasbirthday+=1
		if re.compile('hasNickName').search(each):
			loop_hasnickname+=1
		if re.compile('hasGender').search(each):
			loop_hasgender+=1
		if re.compile('hasEnglishName').search(each):
			loop_hasenglishname+=1
		if re.compile('belongRegion').search(each):
			loop_belongregion+=1		
		if re.compile('hasUsedName').search(each):
			loop_hasusedname+=1
		if re.compile('hasLanguage').search(each):
			loop_haslanguage+=1
		if re.compile('hasGenera').search(each):
			loop_hasgenera+=1
		if re.compile('belongCompany').search(each):
			loop_belongcompany+=1
		if re.compile('career').search(each):
			loop_career+=1
		if re.compile('nation').search(each):
			loop_nation+=1
		if re.compile('school').search(each):
			loop_school+=1
		if re.compile('achievement').search(each):
			loop_achievement+=1
		if re.compile('height').search(each):
			loop_height+=1
		if re.compile('constellation').search(each):
			loop_constellation+=1
		if re.compile('weight').search(each):
			loop_weight+=1
		if re.compile('bloodType').search(each):
			loop_bloodtype+=1
		if re.compile('zodiac').search(each):
			loop_zodiac+=1
		if re.compile('specialty').search(each):
			loop_specialty+=1
		if re.compile('belief').search(each):
			loop_belief+=1
		if re.compile('ancestralHome').search(each):
			loop_ancestralhome+=1
		if re.compile('hobby').search(each):
			loop_hobby+=1
		if re.compile('fansname').search(each):
			loop_fansname+=1
		if re.compile('size').search(each):
			loop_size+=1
		if re.compile('location').search(each):
			loop_location+=1
		if re.compile('familyMembers').search(each):
			loop_familymembers+=1
		if re.compile('introduction').search(each):
			loop_introduction+=1
	cal_percent(loop_hasname,loop1,'hasName')
	cal_percent(loop_hasbirthday,loop1,'hasBirthday')
	cal_percent(loop_hasnickname,loop1,'hasNickName')
	cal_percent(loop_creatdate,loop1,'creatDate')
	cal_percent(loop_hasgender,loop1,'hasGender')
	cal_percent(loop_hasenglishname,loop1,'hasEnglishName')
	cal_percent(loop_belongregion,loop1,'belongRegion')
	cal_percent(loop_hasusedname,loop1,'hasUsedName')
	cal_percent(loop_haslanguage,loop1,'hasLanguage')
	cal_percent(loop_hasgenera,loop1,'hasGenera')
	cal_percent(loop_belongcompany,loop1,'belongCompany')
	cal_percent(loop_career,loop1,'career')
	cal_percent(loop_nation,loop1,'nation')
	cal_percent(loop_school,loop1,'school')
	cal_percent(loop_achievement,loop1,'achievement')
	cal_percent(loop_height,loop1,'height')
	cal_percent(loop_constellation,loop1,'constellation')
	cal_percent(loop_weight,loop1,'weight')
	cal_percent(loop_bloodtype,loop1,'bloodType')
	cal_percent(loop_zodiac,loop1,'zodiac')
	cal_percent(loop_specialty,loop1,'specialty')
	cal_percent(loop_belief,loop1,'belief')
	cal_percent(loop_ancestralhome,loop1,'ancestralHome')
	cal_percent(loop_hobby,loop1,'hobby')
	cal_percent(loop_fansname,loop1,'fansname')
	cal_percent(loop_size,loop1,'size')
	cal_percent(loop_location,loop1,'location')
	cal_percent(loop_familymembers,loop1,'familyMembers')
	cal_percent(loop_introduction,loop1,'introduction')

if __name__=='__main__':
	inputfile=open('outfile_total.txt','r')
	outfile=open('statistic.txt','w')
	outmat=inputfile.readlines()
	print len(outmat)
	main_process(outmat)
	inputfile.close()
	outfile.close()
