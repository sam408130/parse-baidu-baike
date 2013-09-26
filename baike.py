#!/usr/bin/python
#-*-coding:utf-8-*-




import re
import os
import sys
import string
import pachong_baike


def combine(str_baike,str_web):
	mat_baike=re.compile('\|##').split(str_baike)
	mat_web=re.compile('\|##').split(str_web)
	mat_web2=re.compile('##').split(mat_web[1])
	mat_baike2=re.compile('##').split(mat_baike[1])
	hash_baike={}
	for iweb in mat_web2:
		mat_iweb=re.compile('：').split(iweb)
		hash_baike[mat_web[0]]=mat_web[1]
	for ibaike in mat_baike2:
		mat_ibaike=re.compile('：').split(ibaike)
		hash_baike[mat_ibaike[0]]=mat_ibaike[1]
	str_out=mat_baike[0]+'|'
	for eachkey in hash_baike.keys():
		str_out+='##'+eachkey+'：'+hash_baike[eachkey]

	return str_out






def process_filename(name):
	print name
	name=name.decode('gbk').encode('utf-8')
	match=name.split('.txt')
	newname=match[0]+'|'	
	return newname

def process_content(content,eachfile):
	mingpian_reg=r'<div class="card-summary-content">(.*?)</p>'
	part_reg=r'<h2 class="b-h2-3 bk-sidecatalog-title">(.*?)</div></div></div> <div class="clear"></div>'
	part_reg1=r'<span class="headline-index">.*?</span><span class="headline-content">(.*?)</span></h2>'
	biaoqian_reg1=r'<td class="cardFirstTd">(.*?)</td>'
	biaoqian_reg2=r'<td class="cardSecondTd">(.*?)</td>'
	biaoqian_reg3=r'<div class="para">(.*?：.*?)</div>'
	
	str_out=""
	mingpian=re.compile(mingpian_reg).findall(content)
	biaoqian1=re.compile(biaoqian_reg1).findall(content)
	biaoqian2=re.compile(biaoqian_reg2).findall(content)
	biaoqian3=re.compile(biaoqian_reg3).findall(content)
	biaoti=re.compile(part_reg1).findall(content)
	if len(biaoqian1)>0:
		if len(biaoti)>0:
			biaoti=re.sub(r'<[^>]*?>', '',biaoti[0])
			str_out+=process_filename(eachfile)+'<biaoti>'+biaoti+'|'
			#outfile.write('\n'+process_filename(eachfile))
		else:
			str_out+=process_filename(eachfile)
		#if len(mingpian)>0:
			#mingpian[0]=re.sub(r'<[^>]*?>', '',mingpian[0])
			#str_out+='##'+'introduction：'+mingpian[0]
		length=len(biaoqian1)
		for i in range(0,length-1):
			biaoqian1[i]=re.sub(r'<[^>]*?>', '', biaoqian1[i])
			biaoqian2[i]=re.sub(r'<[^>]*?>', '', biaoqian2[i])
			str_out+='##'+biaoqian1[i]+biaoqian2[i]


			#outfile.write('#'+biaoqian1[i]+biaoqian2[i])
		#outfile.write('-------------'+'\n')
	#if len(biaoqian3)>0:
		#loop=0
		#for j in biaoqian3:
			#j=re.sub(r'<[^>]*?>', '',j)
			#if len(j)<15:
				#loop+=1
				#print len(j)
				#outfile.write('#'+j)
		#if (loop>0):
			#outfile.write('--------------------------------'+'\n\n');
	return str_out
	



#filename=os.listdir("./singerlist")
#print len(filename)

def main_process(filelist,url_base,filename1):
	loop=0
	outfile=open(filename1,'w')
	filename=open(filelist,'r')
	mingpian_reg=r'<div class="card-summary-content">(.*?)</p>'
	part_reg=r'<h2 class="b-h2-3 bk-sidecatalog-title">(.*?)</div></div></div> <div class="clear"></div>'
	biaoqian_reg1=r'<td class="cardFirstTd">(.*?)</td>'
	biaoqian_reg2=r'<td class="cardSecondTd">(.*?)</td>'
	biaoqian_reg3=r'<div class="para">(.*?：.*?)</div>'
	part=0
	out=[]
	#outfile=open('result.txt','w')
	for eachfile in filename:
		eachfile=eachfile.strip('\n|\r')
		name_mat=re.compile('\.').split(eachfile)
		singername=name_mat[0]
		singername=singername.decode('gbk').encode('utf-8')
		pachongContent=pachong_baike.main_process(singername)
		url=url_base+eachfile
		#print url
		content=open(url,'r')
		content=''.join(content)
		content=re.compile('\n|\r').sub('',content)
		if re.search(biaoqian_reg1,content,re.M):
			if re.search(part_reg,content):
				sub_content=re.compile(part_reg).findall(content)
				for i in sub_content:
					str_out=process_content(i,eachfile)
					if len(str_out)>2:
						if re.search('：',pachongContent):
							str_out=combine(str_out,pachongContent)
						loop+=1
						outfile.write(str_out+'\n')
						out.append(str_out)
			else:
				str_out=process_content(content,eachfile)
				if len(str_out)>2:
					if re.search('：',pachongContent):
						str_out=combine(str_out,pachongContent)
					loop+=1
					outfile.write(str_out+'\n')
					out.append(str_out)
		elif re.search('：',pachongContent):
				loop+=1
				outfile.write(pachongContent+'\n')
				out.append(pachongContent)			
	#print str_final
	
	print "%d personal information from baike was added"%loop
	filename.close()
	outfile.close()
	return out



	#if len(mingpian)>0:
		#mingpian[0]=re.sub(r'<[^>]*?>', '', mingpian[0])
		#outfile.write(mingpian[0]+'\n')
	#else:
		#outfile.write('\n\n\n')


if __name__ == '__main__':
	filelist='filename1.txt'
	url_base='./baikedata/'
	baikedata=main_process(filelist,url_base,'jiexibaike1.txt')
