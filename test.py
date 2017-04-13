import sys
import os
import socket

def refBanner(ip, port): #根据端口号和IP，连接接收banner信息
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner, filename): #检测文件中的每一条信息是否在banner中
    f = open(filename, "r")
    for line in f.readlines():
        if line.strip('\n') in banner:
            print '[+] server is vulnerable:' + banner.strip('\n')

def main():
if len(sys.argv) == 2: #判断参数传入的文件存在且可执行
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print("[-]" + filename + "does not exist")
        exit(0)
    if not os.access(filename, os.R_OK):
        print("[-]" + filename + "access denied")
        exit(0)
    else:
        print "[-] Usage:" + str(sys.argv[0]) +" vuln filename"
        exit(0)

portlist = [21, 22, 25, 80, 110, 443] #遍历端口和ip，获取远程banner，判断banner是否vulnerable
for x in range(100, 110):
    ip = "192.168.1." + str(x)
    for port in portlist:
        banner = refBanner(ip,port)
        if banner:
            print "[+]" + ip + ":" + banner
            checkVulns(banner, filename)


if __name__ == '_main_':
    main()