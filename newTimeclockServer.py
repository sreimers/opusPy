import time
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
  #Initialize time clock
  currentTime = time.clock()
  print currentTime
  counter = 0

  #Time clock
  while counter < 100:
      time.sleep(.01)
      currentTime = time.clock()
      print currentTime
      counter = counter+1
 

