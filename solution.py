# import socket module
from socket import *
import sys  # In order to terminate the program


def webServer(port=13331):
    # Prepare a server socket
    # Fill in start

    serverSocket = socket(AF_INET, SOCK_STREAM)
    port = 13331
    serverSocket.bind(('127.0.0.1', port))
    serverSocket.listen(5)

    # Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        # Fill in start       #Fill in end
        try:
            message = connectionSocket.recv(5000).decode()  # Fill in start    #Fill in end
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.readlines()
            # Fill in start     #Fill in end
            # Send one HTTP header line into socket
            connectionSocket.sendall('HTTP/1.1 200 OK'.encode())
            #print(outputdata)
            # Fill in start
            # Fill in end
            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            # Send response message for file not found (404)
            # Fill in start
            # Fill in end
            error = 'HTTP/1.1 404 Not Found'
            connectionSocket.sendall(error.encode())
            #print(error)
            # Close client socket
            # Fill in start
            # Fill in end
            connectionSocket.close()

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
