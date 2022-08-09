from email import message
import socket
import os
os.system('cls')

while True:
    udp_ip = "172.16.0.255"
    udp_ipp = "172.16.0.249"   
    udp_port = 8889 # port to send on
    message = input("Enter your message: ")

    print("Sending IP: " + udp_ip)
    print("Sending Port: " + str(udp_port))
    print("Sending message: " + message + "\n\n")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket for sending data to the receiver
    sock.sendto(message.encode(), (udp_ip, udp_port)) # send the message to the receiver
    sock.sendto(message.encode(), (udp_ipp, udp_port))   