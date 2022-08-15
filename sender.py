from email import message
import socket
import os
from turtle import delay
import time
os.system('cls')

while True: # Loop forever
    udp_ip = "172.16.0.52" # IP address of the receiver
    udp_ipp = "172.16.0.64"  # IP address of the second receiver
    udp_port = 8889 # port to send on
    message = input("Enter your message: ") # message to send
    messagesec = input("Enter your second message: ") # second message to send

    print("Sending IP: " + udp_ip) # print the first IP address
    print("Sending IP: " + udp_ipp) # print the second IP address
    print("Sending Port: " + str(udp_port)) # port to send on
    print("Sending message: " + message + "\n\n") # message to send
    print("Sending message: " + messagesec + "\n\n") # second message to send


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP socket for sending data to the receiver
    sock.sendto(message.encode(), (udp_ip, udp_port)) # send the message to the second receiver
    sock.sendto(message.encode(), (udp_ipp, udp_port)) 
    time.sleep(5) # delay for 5 seconds
    sock.sendto(messagesec.encode(), (udp_ip, udp_port)) # send second the message to the receiver
    sock.sendto(messagesec.encode(), (udp_ipp, udp_port))    # send second the message to the second receiver