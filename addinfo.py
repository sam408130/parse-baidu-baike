#!/usr/bin/python
#-*-coding:utf-8-*-




import re
import os
import sys
import string
import pachong_baike

#增加人物属性信息

#建立
def creat_hash(str_baike,name):
  #printname=name.decode('utf-8').encode('gbk')
  #print printname
  str_mat=re.compile('##').split(str_baike)
  myhash={}
  for each_str in str_mat:
    each_str_mat=re.compile('：').split(each_str)
    key=name+each_str_mat[0]
    myhash[key]=each_str_mat[1]
  return myhash


def judge_baikestr(name):
  if hash_baike.has_key(name):
    baike_str=hash_baike[name]
  #else:
    #str_content=pachong_baike.main_process(name)
    #if re.compile('：').search(str_content):
      #print name.decode('utf-8').encode('gbk')
      #baike_mat2=re.compile('\|##').split(str_content)
      #if len(baike_mat2)>0:
        #baike_str=baike_mat2[1]
      #else:
        #baike_str='null'

  else:
      baike_str='null'
  return baike_str




def addinfo(name):
  hash_out={}

  info_hasname_1_0=name+"中文名"
  info_hasname_1_1=name+"姓名"
  info_hasbirthday_1_0=name+"出生日期"
  info_hasbirthday_1_1=name+"生日"
  info_hasbirthday_1_2=name+"出生年月"
  info_hasnickname_1_0=name+"昵称"
  info_hasnickname_1_1=name+"别称"
  info_creatdate_1_0=name+"出品时间"
  info_hasgender_1_0=name+"性别"
  info_hasgender_1_1=name+"性 别"
  info_hasenglishname_1_0=name+"外文名"
  info_belongregion_1_0=name+"所属地区"
  info_hasusedname_1_0=name+"别名"
  info_location_1_0=name+"现居地"
  info_hasusedname_1_1=name+"原名"
  info_haslanguage_1_0=name+"语言"
  info_hasgenera_1_0=name+"类型"
  info_belongcompany_1_0=name+"经纪公司"
  info_belongcompany_1_1=name+"唱片公司"
  info_career_1_0=name+"职业"
  info_nation_1_0=name+"国籍"
  info_school_1_0=name+"毕业学校"
  info_achievement_1_0=name+"主要成就"
  info_height_1_0=name+"身高"
  info_height_1_1=name+"身 高"
  info_size_1_0=name+"三围"
  info_constellation_1_0=name+"星座"
  info_constellation_1_1=name+"星 座"
  info_weight_1_0=name+"体重"
  info_weight_1_1=name+"体 重"
  info_bloodtype_1_0=name+"血型"
  info_bloodtype_1_1=name+"血 型"
  info_zodiac_1_0=name+"生肖"
  info_zodiac_1_1=name+"属相"
  info_zodiac_1_2=name+"生 肖"
  info_zodiac_1_3=name+"属"
  info_specialty_1_0=name+"特长"
  info_belief_1_0=name+"宗教信仰"
  info_belief_1_1=name+"信仰"
  info_ancestralhome_1_0=name+"出生地"
  info_ancestralhome_1_1=name+"籍贯"
  info_ancestralhome_1_2=name+"祖籍"
  info_hobby_1_0=name+"爱好"
  info_fansname_1_0=name+"粉丝名"
  info_familymembers_1_0=name+"家庭成员"
  info_familymembers_1_1=name+"配偶"
  info_familymembers_1_2=name+"妻子"
  info_familymembers_1_3=name+"丈夫"
  info_hasmasterpiece_1_0=name+'代表作品'
  info_introduction_1_0=name+"introduction"

  baike_str=judge_baikestr(name)
  if not (baike_str=='null'):
    hash_str=creat_hash(baike_str,name)
    #hasName
    if hash_str.has_key(info_hasname_1_1):
      hash_out["hasName"]=hash_str[info_hasname_1_1]


    elif hash_str.has_key(info_hasname_1_0):
      hash_out["hasName"]=hash_str[info_hasname_1_0]
      
    #hashBirthday
    if hash_str.has_key(info_hasbirthday_1_2):
      hash_out["hasBirthday"]=hash_str[info_hasbirthday_1_2]
    
    elif hash_str.has_key(info_hasbirthday_1_1):
      hash_out["hasBirthday"]=hash_str[info_hasbirthday_1_1]


    elif hash_str.has_key(info_hasbirthday_1_0):
      hash_out["hasBirthday"]=hash_str[info_hasbirthday_1_0]


      

    #hasNickName
    if hash_str.has_key(info_hasnickname_1_1):
      hash_out["hasNickName"]=hash_str[info_hasnickname_1_1]


    elif hash_str.has_key(info_hasnickname_1_0):
      hash_out["hasNickName"]=hash_str[info_hasnickname_1_0]
      

    #creatDate
    if hash_str.has_key(info_creatdate_1_0):
      hash_out["creatDate"]=hash_str[info_creatdate_1_0]


    #hasGender
    if hash_str.has_key(info_hasgender_1_1):
      hash_out["hasGender"]=hash_str[info_hasgender_1_1]


    elif hash_str.has_key(info_hasgender_1_0):
      hash_out["hasGender"]=hash_str[info_hasgender_1_0]

 
    #hasEnglishName
    if hash_str.has_key(info_hasenglishname_1_0):
      hash_out["hasEnglishName"]=hash_str[info_hasenglishname_1_0]


    #belongRegion
    if hash_str.has_key(info_belongregion_1_0):
      hash_out["belongRegion"]=hash_str[info_belongregion_1_0]

    #hasMasterPiece
    if hash_str.has_key(info_hasmasterpiece_1_0):
      hash_out["hasMasterPiece"]=hash_str[info_hasmasterpiece_1_0]
    
    #hasUsedName
    if hash_str.has_key(info_hasusedname_1_1):
      hash_out["hasUsedName"]=hash_str[info_hasusedname_1_1]


    elif hash_str.has_key(info_hasusedname_1_0):
      hash_out["hasUsedName"]=hash_str[info_hasusedname_1_0]


    #hasLanguage
    if hash_str.has_key(info_haslanguage_1_0):
      hash_out["hasLanguage"]=hash_str[info_haslanguage_1_0]


    #hasGenera
    if hash_str.has_key(info_hasgenera_1_0):
      hash_out["hasGenera"]=hash_str[info_hasgenera_1_0]


    #belongCompany
    if hash_str.has_key(info_belongcompany_1_1):
      hash_out["belongCompany"]=hash_str[info_belongcompany_1_1]


    elif hash_str.has_key(info_belongcompany_1_0):
      hash_out["belongCompany"]=hash_str[info_belongcompany_1_0]


    #career
    if hash_str.has_key(info_career_1_0):
      hash_out["career"]=hash_str[info_career_1_0]


    #nation
    if hash_str.has_key(info_nation_1_0):
      hash_out["nation"]=hash_str[info_nation_1_0]


    #school
    if hash_str.has_key(info_school_1_0):
      hash_out["school"]=hash_str[info_school_1_0]


    #achievement
    if hash_str.has_key(info_achievement_1_0):
      hash_out["achievement"]=hash_str[info_achievement_1_0]


    #height
    if hash_str.has_key(info_height_1_1):
      hash_out["height"]=hash_str[info_height_1_1]


    elif hash_str.has_key(info_height_1_0):
      hash_out["height"]=hash_str[info_height_1_0]


    #constellation
    if hash_str.has_key(info_constellation_1_1):
      hash_out["constellation"]=hash_str[info_constellation_1_1]


    elif hash_str.has_key(info_constellation_1_0):
      hash_out["constellation"]=hash_str[info_constellation_1_0]

 
    #weight
    if hash_str.has_key(info_weight_1_1):
      hash_out["weight"]=hash_str[info_weight_1_1]


    elif hash_str.has_key(info_weight_1_0):
      hash_out["weight"]=hash_str[info_weight_1_0]


    #bloodType
    if hash_str.has_key(info_bloodtype_1_1):
      hash_out["bloodType"]=hash_str[info_bloodtype_1_1]


    elif hash_str.has_key(info_bloodtype_1_0):
      hash_out["bloodType"]=hash_str[info_bloodtype_1_0]


    #zodiac
    if hash_str.has_key(info_zodiac_1_3):
      hash_out["zodiac"]=hash_str[info_zodiac_1_3]


    elif hash_str.has_key(info_zodiac_1_2):
      hash_out["zodiac"]=hash_str[info_zodiac_1_2]

        
    elif hash_str.has_key(info_zodiac_1_1):
      hash_out["zodiac"]=hash_str[info_zodiac_1_1]


    elif hash_str.has_key(info_zodiac_1_0):
      hash_out["zodiac"]=hash_str[info_zodiac_1_0]


    #specialty
    if hash_str.has_key(info_specialty_1_0):
      hash_out["specialty"]=hash_str[info_specialty_1_0]


    #belief
    if hash_str.has_key(info_belief_1_1):
      hash_out["belief"]=hash_str[info_belief_1_1]


    elif hash_str.has_key(info_belief_1_0):
      hash_out["belief"]=hash_str[info_belief_1_0]

 
    #ancestralHome
    if hash_str.has_key(info_ancestralhome_1_2):
      hash_out["ancestralHome"]=hash_str[info_ancestralhome_1_2]


    elif hash_str.has_key(info_ancestralhome_1_1):
      hash_out["ancestralHome"]=hash_str[info_ancestralhome_1_1]


    elif hash_str.has_key(info_ancestralhome_1_0):
      hash_out["ancestralHome"]=hash_str[info_ancestralhome_1_0]

          
    #hobby
    if hash_str.has_key(info_hobby_1_0):
      hash_out["hobby"]=hash_str[info_hobby_1_0]


    #fansname
    if hash_str.has_key(info_fansname_1_0):
      hash_out["fansname"]=hash_str[info_fansname_1_0]


    #size
    if hash_str.has_key(info_size_1_0):
      hash_out["size"]=hash_str[info_size_1_0]


    #location
    if hash_str.has_key(info_location_1_0):
      hash_out["location"]=hash_str[info_location_1_0]

    
    #familyMembers
    if hash_str.has_key(info_familymembers_1_3):
      hash_out["familyMembers"]=hash_str[info_familymembers_1_3]

    
    elif hash_str.has_key(info_familymembers_1_2):
      hash_out["familyMembers"]=hash_str[info_familymembers_1_2]

       
    elif hash_str.has_key(info_familymembers_1_1):
      hash_out["familyMembers"]=hash_str[info_familymembers_1_1]


    elif hash_str.has_key(info_familymembers_1_0):
      hash_out["familyMembers"]=hash_str[info_familymembers_1_0]

    

    #introduction
    if hash_str.has_key(info_introduction_1_0):
      hash_out["introduction"]=hash_str[info_introduction_1_0]



  return  hash_out



def main_process(namelistfile,baikedata,filename):
  loop1=0
  loop2=0
  baike_data=baikedata
  global hash_baike

  hash_baike={}
  outmat=[]
  for each_baike in baike_data:
    if re.search('\|##',each_baike):
      baike_mat=re.compile('\|##').split(each_baike)
      hash_baike[baike_mat[0]]=baike_mat[1]

  singername=open(namelistfile,'r')
  outfile=open(filename,'w')
  for eachname in singername:
    eachname=eachname.strip('\n')
    hash_final=addinfo(eachname)
    str1=eachname.strip(' | ')
    for k,v in hash_final.items():
      loop2+=1
      str1+="|"+k+"##"+v
    if re.search('##',str1):
      loop1+=1
      outmat.append(str1)
      outfile.write(str1+'\n')
  singername.close()
  outfile.close()
  total=loop1*27
  percent=float(loop2)/float(total)
  percent=format(percent, '.2%')
  print "%d items from %d person were added to database,the filling rate is %s"%(loop2,loop1,percent)
  return outmat

