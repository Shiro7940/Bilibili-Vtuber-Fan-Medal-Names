from main import *
import random

all_medal = set(vtb_fan_medal_dict.values())
all_medal.remove("粉丝团")
all_medal.remove("暂无粉丝勋章")
all_medal_lst = list(all_medal)

def get_name_by_medal(mname:str,namedict):
    try:
        name = []
        roomid = find_rid_by_medal(mname)
        for item in roomid:
            nametemp = namedict.get(item,"Name Not Found")
            name += [nametemp]
        return name[0]
    except Exception as error:
        print(error)
        print("An ERROR Occurred")
        return None

def gen_question_set(mname:str,namedict):
    names = []
    medals = []
    output = set()
    i = 0
    while i in range(0,3):
        temp = all_medal_lst[random.randint(0,len(all_medal_lst)-1)]
        if temp != mname:
            temp_name = get_name_by_medal(temp,namedict)
            if temp_name != 'Name Not Found':
                medals += [temp]
                names += [temp_name]
                i += 1
    names += [get_name_by_medal(mname,namedict)]
    medals += [mname]
    for n in range(0,len(names)):
        output.add((names[n],medals[n]))
    name1 = 1
    return output
    
def gen_question(qset:set,ans_name:str,ans_medal:str,mode:int,answer=None) -> bool:
    try:
        if mode == 0:
            print('下列哪个虚拟UP主的勋章是 "'+ans_medal+'":')
        elif mode == 1:
            print('虚拟UP主 "'+ans_name+'" 的勋章是: ')
        else:
            print("模式选择无效")
            return False
        qlist = list(qset)
        a = qlist[0][mode]
        b = qlist[1][mode]
        c = qlist[2][mode]
        d = qlist[3][mode]
        templist = [a,b,c,d]
        ans_dict = {"A":0,"B":1,"C":2,"D":3,
                    "1":0,"2":1,"3":2,"4":3}
        print("A: "+str(a)+
              "\nB: "+str(b)+
              "\nC: "+str(c)+
              "\nD: "+str(d))
        
        if answer == None:
            answer = str(input("答案: ")).upper()
        else:
            print("答案: "+str(answer))
        if answer == "E":
            print("退出游戏")
            return "Exit"
        
        c = ans_dict.get(answer)
        if mode == 1 and templist[c] == ans_medal:
            print("回答正确")
            return True
        elif mode == 0 and templist[c] == ans_name:
            print("回答正确")
            return True
        else:
            if mode == 1:
                print('回答错误，答案是 "'+ans_medal+'"')
            if mode == 0:
                print('回答错误，答案是 "'+ans_name+'"')
            return False
        
    except:
        print("答案无效")
        return False

def game():
    exit = False
    correct = 0
    false = 0
    total = 0 
    print("大小写均可，回答E可退出")
    namedict = gen_rid_to_name_dict()
    uiddict = gen_rid_to_uid_dict()        
    try:
        limit = int(input("请输入题目量: "))
    except:
        limit = 2000
    try:
        while (not exit) and (len(all_medal) >= 4) and total<limit: 
            ans_medal = all_medal.pop()
            ans_name = get_name_by_medal(ans_medal,namedict)
            if ans_name != 'Name Not Found':
                total+=1
                print("第 "+str(total)+"/"+str(limit)+" 题")
                qset = gen_question_set(ans_medal,namedict)
                mode = round(random.random())
                status = gen_question(qset,ans_name,ans_medal,mode)
                if status == True:
                    correct += 1
                elif status == False:
                    false += 1
                elif status == "Exit":
                    exit = True
                    total-=1
                print("-------------------")
            else:
                pass
            
    finally:
        score_percent = "NaN"
        if total != 0 :
            score_percent = str(round((correct/total)*100,2))
        print("你的分数是: "+score_percent+"分")
        print("正确: "+str(correct)+"题, 错误: "+str(false)+"题, 总计: "+str(total)+"题")
        
def test():
    all_medal = set(vtb_fan_medal_dict.values())
    all_medal.remove("粉丝团")
    all_medal.remove("暂无粉丝勋章")
    all_medal_lst = list(all_medal)    
    exit = False
    correct = 0
    false = 0
    total = 0 
    ans_list = ["A","B","C","D","1","2","3","4"]
    namedict = gen_rid_to_name_dict()
    uiddict = gen_rid_to_uid_dict()        
    limit = 6000
    try:
        while (not exit) and (len(all_medal) >= 4) and total<limit: 
            ans_medal = all_medal.pop()
            ans_name = get_name_by_medal(ans_medal,namedict)
            if ans_name != 'Name Not Found':
                total+=1
                print("第 "+str(total)+"/"+str(limit)+" 题")
                qset = gen_question_set(ans_medal,namedict)
                mode = round(random.random())
                answer = ans_list[random.randint(0,7)]
                status = gen_question(qset,ans_name,ans_medal,mode,answer)
                if status == True:
                    correct += 1
                elif status == False:
                    false += 1
                elif status == "Exit":
                    exit = True
                    total-=1
                print("-------------------")
            else:
                pass  
            
    finally:
        score_percent = "NaN"
        if total != 0 :
            score_percent = str(round((correct/total)*100,2))
        print("你的分数是: "+score_percent+"分")
        print("正确: "+str(correct)+"题, 错误: "+str(false)+"题, 总计: "+str(total)+"题")
   
        
        
if __name__ == "__main__":
    game()
