import socket

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost',12345))

file=open('akinci.png','rb')
imagge_date=file.read(2048)
 
while imagge_date:
   client.send(imagge_date)
   imagge_date=file.read(2048)

file.close()
client.close()
