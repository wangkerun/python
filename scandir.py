import requests
# 提取域名并且去重复
class mydir():
    def __init__(self):
        self.dirset=set()
        self.dirlist=[]
        f=open("URL.txt",'r',encoding="unicode_escape")
        for i in f:
            num=i.find("/",7)
            url=i[0:num:1]
            self.dirset.add(url)
        f.close()
        dirfile=open("DIR.txt","r",encoding="unicode_escape")
        for dirf in dirfile:
            self.dirlist.append(dirf.replace("\n",""))
        dirfile.close()



    def dir_scan(self):

        for url in self.dirset:
            for data in  self.dirlist:
                try:
                    r = requests.get(url + data)
                    if r.status_code != 404:
                        code = url + data + "存在"
                        f = open("mulu.txt", "a", encoding="utf-8")
                        f.write(url + data + "\n")
                        f.close()
                        print(code)
                    else:
                        print(url + data + "不存在")
                except requests.exceptions.ConnectionError:
                    break


if __name__ == '__main__':
    mydir=mydir()
    mydir.dir_scan()