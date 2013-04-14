#import socket module

import socket
import os.path

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Prepare a server socket

serverPort = 50001
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
  #Establish connection
  print 'Ready to serve...'
  connectionSocket, addr = serverSocket.accept()

  #Get Request
  message = connectionSocket.recv(1024)
  capitalizedWords = message.upper()
  filename = message.split()[1][1:]
  print filename

  #Read File
  if os.path.exists(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()

    outputdata = []
    outputdata.append("HTTP/1.0 200 OK\r\n")
  else:
    message = []
    message.append("HTTP Error 404: File Not Found<br>")
    message.append("Error: can\'t find the file or ")
    message.append("read data from it")
    data = ''.join(message)
    outputdata = []
    outputdata.append("HTTP/1.0 404 NOT FOUND\r\n")

  outputdata.append("Connection: close\r\n")
  #outputdata.append("Content-Type: text/plain\r\n")
  outputdata.append("Content-Length: ")
  outputdata.append(str(len(data)))
  outputdata.append("\r\n\r\n")
  outputdata.append(data)

  #Send the content of the requested file to the client
  for i in range(0, len(outputdata)):
    connectionSocket.send(outputdata[i])
  connectionSocket.close()
serverSocket.close()

