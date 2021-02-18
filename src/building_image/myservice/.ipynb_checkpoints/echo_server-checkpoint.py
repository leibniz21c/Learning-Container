#
# echo server for container test
#
import socket

with socket.socket() as server_socket:
  server_socket.bind(("0.0.0.0", 50000))
  server_socket.listen()
  print("server is started")
  client_socket, client_addr = server_socket.accept()
    
  with client_socket:
    print("Connected by", client_addr)
    
    while True:
      data = client_socket.recv(1024)
      if not data: break
      print('Message by ', client_addr, ' : ', data)
      client_socket.sendall(data)