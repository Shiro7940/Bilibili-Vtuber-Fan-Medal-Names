from medaldata import vtblist, vtb_fan_medal_dict

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
    return ridset
    
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
    #print(i)
    #print(rid_to_uid_dict)
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
    #print(i)
    #print(uid_to_rid_dict)
    return uid_to_rid_dict

def gen_rid_to_name_dict():
    rid_to_name_dict = dict()
    datatxt = open("vtbs.txt","r",encoding="utf8")
    for line in datatxt:
        datalist = line.split()    
        if datalist[-1] != "无":
            rid_to_name_dict.update({int(datalist[-1]):str(datalist[0])})
    #print(rid_to_name_dict)
    return rid_to_name_dict
    
def gen_uid_to_name_dict():
    uid_to_name_dict = dict()
    datatxt = open("vtbs.txt","r",encoding="utf8")
    for line in datatxt:
        datalist = line.split()    
        if datalist[-2] != "无":
            uid_to_name_dict.update({int(datalist[-2]):str(datalist[0])})
    #print(uid_to_name_dict)
    return uid_to_name_dict
    
def find_not_logged_in_vtbs():
    namedict = gen_rid_to_name_dict()
    lst = []
    for item in vtblist:
        feedback = namedict.get(item) 
        if feedback == None:
            #print(item)    
            lst += [item]
    return lst

def find_rid_by_medal(mname:str):
    rid = []
    for key,value in vtb_fan_medal_dict.items():
        if value == mname:
            rid += [key]
    if rid == []:
        return ["Does Not Exist"]
    else:
        return rid

def get_info_by_medal(mname:str):
    try:
        name = []
        uid = []
        roomid = find_rid_by_medal(mname)
        namedict = gen_rid_to_name_dict()
        for item in roomid:
            nametemp = namedict.get(item,"Name Not Found")
            name += [nametemp]
        uiddict = gen_rid_to_uid_dict()
        for item in roomid:
            uidtemp = uiddict.get(item,"Does Not Exist")
            uid += [uidtemp]
        print("勋章名: "+str(mname)+"\n用户名: "+str(name)+
              "\n  UID: "+str(uid)+"\n房间号: "+str(roomid))
        return [name,uid,roomid]
    except Exception as error:
        print(error)
        print("An ERROR Occurred")
        return None

def gen_fst_list():
    medallist = list(vtb_fan_medal_dict.items())
    fstlist = []
    for obj in medallist:
        rid, name = obj
        if name == "粉丝团":
            fstlist += [rid]
    return fstlist

def main():
    exit = False
    while not exit:
        medalname = str(input("请输入粉丝勋章名: "))
        medaldata = get_info_by_medal(medalname)
        if str(input("退出? Y/y: ")).upper() == "Y":
            exit = True
            
if __name__ == "__main__":
    main()
