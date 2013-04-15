#Client for the Python music transfer project
#Corresponds to one individual musician

#Imports

#PY-OPUS
#For encoding

#GStreaner (or equivalent)
#For sending the transmission to the other musician

#Something for accepting the raw input

#End imports

#Program body

#Initialization of program parameters

#Make connection to raw input channel
#if not found, fatal error

#Receive IP address for the server
#Server controls time clock
#Handshake with the server

#Receive IP address for the other musician client
#Only one for the current implementation
#Handshake with the client

#Begin program itself
#Open connection between client and server
#Open connection between client and other client

#Initialize statistical information tracking
#Determine average round trip latency incurred
#Determine overall latency of signal to endpoint on average
#Determine others

#When the "begin" button is pressed, commence the track recording
#Consult the central server as the timeclock authority
#Record the audio locally for eventual recombination

#Until the maximum track length is reached or the track is ended, keep rapidly sending packets

#At the same time, rapidly receive the audio from the other host

#End the audio stream

#Receive the complete track of the other recording as a file via TCP connection
#The TCP connection is to provide checksum