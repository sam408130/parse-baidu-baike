#!/usr/bin/python
#-*-coding:utf-8-*-

#实现解析一键完成


import re
import os
import sys
import string
#---------------personal----------------#
import addinfo
import repeat_name
import baike
import statistic
#---------------------------------------#




#outfile=open('test.txt','w')
filelist='filename.txt'
url_base='./baikedata/'
print "program is processing ,please be patient - -!"


#baikedata=baike.main_process(filelist,url_base,'jiexibaike.txt')
baikedata=open('jiexidata.txt','r')


baike_processed=repeat_name.main_process(baikedata,'repeatName.txt')
print "system is adding information to database"
out=addinfo.main_process('singerlist1.txt',baike_processed,'outfile_total.txt')

statistic.main_process(out)
print "processing end"
