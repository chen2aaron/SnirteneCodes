#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import sys

# 创建sockt
# 地址簇 : AF_INET (IPv4)
# 类型: SOCK_STREAM (使用 TCP 传输控制协议)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print "Failed to creat socket. Error code:" + str(msg[0]) + " , Error message: " + msg[1]
    sys.exit()
print "Socket Created"

host = "www.v2ex.com"
port = 80

# 获取远程ip地址
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print "Hostname could not be resolved. Exiting"
    sys.exit()
print "IP Address of " + host + " is " + remote_ip


# 连接远程服务器 如果不用80端口，会显示socket.error: [Errno 60] Operation timed out
# 这个逻辑相当于构建了一个端口扫描器
s.connect((remote_ip, port))
print "Socket connect to " + host + " on ip " + remote_ip

# 发送数据
message = "GET / HTTP/1.1\r\n\r\n"
try:
    s.sendall(message)
except socket.error:
    print "Send failed."
    sys.exit()
print "Message send successfully!"


# 接受数据
reply = s.recv(4096)
print reply
s.close()
