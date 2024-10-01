# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()   #Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode() #Fill in start -a client is sending you a message   #Fill in end 
      filename = message.split()[1]
      
      #print(message.split())
    
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "rt")
      #fill in end
      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
      #['GET', '/helloworld.html', 'HTTP/1.1', 'Host:', '127.0.0.1:13331', 'Connection:', 'keep-alive', 'Cache-Control:', 'max-age=0', 'sec-ch-ua:',
      # '"Chromium";v="128",', '"Not;A=Brand";v="24",', '"Microsoft', 'Edge";v="128"', 'sec-ch-ua-mobile:', '?0', 'sec-ch-ua-platform:', '"Windows"', 
      #'Upgrade-Insecure-Requests:', '1', 'User-Agent:', 'Mozilla/5.0', '(Windows', 'NT', '10.0;', 'Win64;', 'x64)', 'AppleWebKit/537.36', '(KHTML,', 
      #'like', 'Gecko)', 'Chrome/128.0.0.0', 'Safari/537.36', 'Edg/128.0.0.0', 'Accept:', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif
      #,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Sec-Fetch-Site:', 'none', 'Sec-Fetch-Mode:', 'navigate', 'Sec-Fetch-User:',
      # '?1', 'Sec-Fetch-Dest:', 'document', 'Accept-Encoding:', 'gzip,', 'deflate,', 'br,', 'zstd', 'Accept-Language:', 'en-US,en;q=0.9,en-CA;q=0.8']
      respProtocol = "HTTP/1.1"
      respStatus = "200"
      respStatusText = "OK"
      #respBody = "<html lang=\"en\"><head><meta charset=\"UTF-8\"><title>HelloWorld</title></head><body><p>Hello World!</p></body></html>"
      #Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = "Content-Type: text/html; charset=UTF-8\r\n"
      fileContents = ""
      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
      #Fill in end
      for i in f: #for line in file
        fileContents = fileContents + i
      
      capSentence = respProtocol+" "+ respStatus+" "+respStatusText+" "+outputdata+"\r\n\r\n"+fileContents
      connectionSocket.send(capSentence.encode())
      f.close()
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      raise RuntimeError('error') from error
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Close client socket
      #Fill in start
    connectionSocket.close()
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

#if __name__ == "__main__":
#  webServer(13331)
