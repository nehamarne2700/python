import socket

print('Welcome to DNS to IP Address')
URL=input('Enter URL: ')

addr1 = socket.gethostbyname(URL)

print(addr1)
print('WelCome IP address to DNS')
IP=input('Enter IP Address: ')
addr6=socket.gethostbyaddr(IP)
print(addr6)
