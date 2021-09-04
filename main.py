from medaldata import *

def gen_newid():
    roomid = []
    datatxt = open("vtbs.txt","r",encoding="utf8")
    for line in datatxt:
        datalist = line.split()
        if datalist[-1] != "无":
            roomid += [int(datalist[-1])]
            
    ridset = set(roomid)
    for item in vtblist:
        ridset.discard(item)
        
    print(ridset)
    datatxt.close()
    return list(ridset)

def dict_update(olddict:dict,newdict:dict):
    old_item_list = list(olddict.items())
    for item in old_item_list:
        rid,oldmedal = item
        newmedal = newdict.get(rid,None)
        if "-" in str(rid):
            print(',"'+str(rid)+'":"'+str(oldmedal)+'"')
        if (oldmedal != newmedal) and (newmedal != None) and (oldmedal != "暂无粉丝勋章"):
            for n in range(1,10):
                if olddict.get(str(str(rid)+"-"+str(n)),None) == None:
                    break
            print(',"'+str(rid)+'-'+str(n)+'":"'+str(oldmedal)+'"')

def gen_uid_list():
    uid_list = []
    datatxt = open("vtbs.txt","r",encoding="utf8")
    for line in datatxt:
        datalist = line.split()    
        if datalist[-2] != "无":
            uid_list += [int(datalist[-2])]
    uid_list.sort()
    return uid_list

def gen_rid_to_uid_dict():
    i=0
    rid_to_uid_dict = dict()
    datatxt = open("vtbs.txt","r",encoding="utf8")
    for line in datatxt:
        datalist = line.split()    
        if datalist[-1] != "无":
            rid_to_uid_dict.update({int(datalist[-1]):int(datalist[-2])})
        else:
            i+=1
    return rid_to_uid_dict

def gen_uid_to_rid_dict():
    i=0
    uid_to_rid_dict = dict()
    datatxt = open("vtbs.txt","r",encoding="utf8")
    for line in datatxt:
        datalist = line.split()    
        if datalist[-1] != "无":
            uid_to_rid_dict.update({int(datalist[-2]):int(datalist[-1])})
        else:
            i+=1
    return uid_to_rid_dict

def gen_rid_to_name_dict():
    rid_to_name_dict = dict()
    datatxt = open("vtbs.txt","r",encoding="utf8")
    for line in datatxt:
        datalist = line.split()    
        if datalist[-1] != "无":
            rid_to_name_dict.update({int(datalist[-1]):str(datalist[0])})
    return rid_to_name_dict

def gen_name_to_rid_dict():
    name_to_rid_dict = dict()
    datatxt = open("vtbs.txt","r",encoding="utf8")
    for line in datatxt:
        datalist = line.split()    
        if datalist[-1] != "无":
            name_to_rid_dict.update({str(datalist[0]):int(datalist[-1])})
    return name_to_rid_dict

def gen_rid_to_fans_dict():
    rid_to_fans_dict = dict()
    datatxt = open("vtbs.txt","r",encoding="utf8")
    for line in datatxt:
        datalist = line.split() 
        if datalist[-1] != "无":
            rid_to_fans_dict.update({int(datalist[-1]):int(datalist[1])})
    return rid_to_fans_dict

def gen_uid_to_name_dict():
    uid_to_name_dict = dict()
    datatxt = open("vtbs.txt","r",encoding="utf8")
    for line in datatxt:
        datalist = line.split()    
        if datalist[-2] != "无":
            uid_to_name_dict.update({int(datalist[-2]):str(datalist[0])})
    return uid_to_name_dict
    
def find_not_logged_in_vtbs():
    namedict = gen_rid_to_name_dict()
    not_logged_list = []
    for item in vtblist:
        feedback = namedict.get(item) 
        if feedback == None:    
            not_logged_list += [item]
    return not_logged_list

def find_rid_by_medal(mname:str):
    rid = []
    for key,value in vtb_fan_medal_dict.items():
        if value == mname:
            rid += [key]
    if rid == []:
        return ["Does Not Exist"]
    else:
        return rid

def old_medal_rid(oldrid:str):
    new = ""
    for char in oldrid:
        if char != "-":
            new += char
        else:
            break
    return int(new)

def get_info_by_medal(mname:str,namedict,uiddict,showfans=False):
    try:
        name = []
        uid = []
        roomid = find_rid_by_medal(mname)
        isold = False
        if "-" in str(roomid[0]) and len(roomid) == 1:
            isold = True
            roomid[0] = old_medal_rid(roomid[0])
            
        for item in roomid:
            nametemp = namedict.get(item,"Name Not Found")
            name += [nametemp]
        for item in roomid:
            uidtemp = uiddict.get(item,"Does Not Exist")
            uid += [uidtemp]
            
        if isold == True:
            print("此勋章已经不再被使用")
        print("勋章名: "+str(mname)+"\n用户名: "+str(name)+
              "\n  UID: "+str(uid)+"\n房间号: "+str(roomid))
        if showfans == True:
            fansdict = gen_rid_to_fans_dict()
            fans = fansdict.get(roomid,"Does Not Exist")
            print("粉丝数："+str(fans))
        return [name,uid,roomid]
    
    except Exception as error:
        print(error)
        print("An ERROR Occurred")
        return None

def get_info_by_rid(roomid:int,namedict,uiddict,showfans=False):
    name = namedict.get(roomid,"Name Not Found")
    uid = uiddict.get(roomid,"Does Not Exist")
    medal = vtb_fan_medal_dict.get(roomid,"Does Not Exist")
    
    old_medals = []
    for i in range(1,11):
        temp = vtb_fan_medal_dict.get(str(roomid)+"-"+str(i),"Does Not Exist") 
        if temp != "Does Not Exist" :
            old_medals += [str(temp)]
            
    print("用户名: "+str(name)+"\n  UID: "+str(uid)+
          "\n房间号: "+str(roomid)+"\n勋章名: "+str(medal))
    if showfans == True:
        fansdict = gen_rid_to_fans_dict()
        fans = fansdict.get(roomid,"Does Not Exist")
        print("粉丝数："+str(fans)+" ("+data_version+")")
    if old_medals != []:
        print("曾用勋章："+str(old_medals))
        
    return [name,uid,roomid,medal,old_medals]

def gen_fst_list():
    medallist = list(vtb_fan_medal_dict.items())
    fstlist = []
    for obj in medallist:
        rid, name = obj
        if name == "粉丝团":
            fstlist += [rid]
    return fstlist

def gen_none_list():
    medallist = list(vtb_fan_medal_dict.items())
    nonelist = []
    for obj in medallist:
        rid, name = obj
        if name == "暂无粉丝勋章":
            nonelist += [rid]
    return nonelist

def gen_update_list(fanlimit=900):
    nonelist = gen_none_list()
    fansdict = gen_rid_to_fans_dict()
    update_list = []
    for item in nonelist:
        current_fans = fansdict.get(int(item),0)
        if current_fans >= fanlimit:
            update_list += [item]
    return update_list


def search_by_str(stri,name_to_riddict=None):
    if name_to_riddict == None:
        name_to_riddict = gen_name_to_rid_dict()
    keylist = list(name_to_riddict.keys())
    result_name = []
    for item in keylist:
        temp = item.upper()
        if stri.upper() in temp:
            result_name += [item]
    result_rid = []
    for name in result_name:
        rid = name_to_riddict.get(name)
        result_rid += [rid]
    if result_rid != []:
        batch(result_rid,showfans=False)
        length = str(len(result_rid))
        if length != "1":
            print(length+" Results")
        else:
            print(length+" Result")
    else:
        print("No Result")
    return result_rid
    
def batch(datalist:list,showfans=True):
    print("-------------------")
    namedict = gen_rid_to_name_dict()
    uiddict = gen_rid_to_uid_dict()
    for item in datalist:
        try: 
            inputdata = int(item)
            livedata = get_info_by_rid(item,namedict,uiddict,showfans)
        except:
            medaldata = get_info_by_medal(item,namedict,uiddict,showfans)
        print("-------------------")        

def main():
    exit = False
    print("当前数据库版本："+data_version)
    namedict = gen_rid_to_name_dict()
    name_to_riddict = gen_name_to_rid_dict()
    uiddict = gen_rid_to_uid_dict()    
    while not exit:
        print("-------------------")
        inputdata = str(input("请输入粉丝勋章名/房间号: "))
        if inputdata.upper() == "E":
            break
        try: 
            inputdata = int(inputdata)
            livedata = get_info_by_rid(inputdata,namedict,uiddict)
        except:
            if (":" in inputdata) or (";" in inputdata)\
            or ("：" in inputdata) or ("；" in inputdata):
                print("搜索模式")
                inputdata = inputdata.replace(":","").replace(";","")\
                                     .replace("：","").replace("；","")
                search_by_str(inputdata,name_to_riddict)
            else:
                medaldata = get_info_by_medal(inputdata,namedict,uiddict)
                print("-------------------")
        if str(input("退出? Y/y: ")).upper() == "Y":
            exit = True

if __name__ == "__main__":
    main()
