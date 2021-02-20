from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start

    clientSocket = socket(AF_INET, SOCK_STREAM)
    #mailserver = '127.0.0.1'
    #port = 1025
    clientSocket.connect(('127.0.0.1', 1025))
    # clientSocket.bind((mailserver, port))
    # clientSocket.listen(1)
    # clientSocket, addr = clientSocket.accept()

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    mailCommand = 'MAIL FROM:<jah8859@nyu.edu>\r\n'
    clientSocket.send(mailCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    #if recv2[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in start
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptCommand = '<RCPT TO:jah8859.nyu.edu>\r\n'
    clientSocket.send(rcptCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    #if recv3[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    #if recv4[:3] != '354':
        #print('354 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    #clientSocket.send(msg.encode())
    #print(recv5)
    #if recv5[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv6)
    #if recv6[:3] != '250':
        #print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv7 = clientSocket.recv(1024).decode()
    #print(recv7)
    #if recv7[:3] != '221':
        #print('221 reply not received from server.')
    # Fill in end

    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
