# Server program for broadcast

import socket
import datetime

# Set the socket parameters
addr = ('<broadcast>', 33333)  # host, port

# Create socket and bind to address
UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPSock.bind(('',33333))
UDPSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
print("----------------------------------\n동신과고 야자이동 시스템 서버 v.1.0\n----------------------------------\n서버 준비됨.")

# Receive messages
while True:
    data, addr = UDPSock.recvfrom(1024)
    if data.decode() == 'stop':
        print('Client wants me to stop.')
        sudoconfirm=input("Press y then enter to close server.")
        if sudoconfirm=='y':
            break
        else:
            continue
    else:
        now = datetime.datetime.now()
        print("----------------------------------\n야자 이동 정보 수신.\nTime stamp:",now,"\n신청 IP: '%s', 신청 정보: '%s'" % (addr[0], data.decode()),"\n----------------------------------")
        #UDPSock.sendto(data, addr)

# Close socket
UDPSock.close()
print('서버 종료됨.')
