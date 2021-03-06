# TCP Server 
# Intro to networking concepts

"""
TCP (Transmission Control Protocol) - is a standard that defines how to establish and maintain a network conversation through which application programs can exchange data.
TCP works with the Internet Protocol (IP), which defines how computers send packets of data to each other. 
Uses a 3 way hand shake
c > syn
s < syn/ack
c > ack

Server - listens for incomming connections via TCP
Clinet - connects to the server via TCP
Network - A network consists of two or more computers that are linked
IP - the number that represents the machine on the network (IPv4 or IPv6)
Port - A communication end point
Protocol - Defined means of application communications
"""

# Includes
import logging
import socket
logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

# TCP Server
def server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = (ip, port)

    logging.info(f'Build: {ip}:{port}')
    s.bind(address)

    logging.info(f'Listening')
    s.listen(1)

    con, addr = s.accept()
    logging.info(f'Connected: {addr}')

    while True:
        data = con.recv(1024)
        if len(data) == 0:
            logging.info(f'Exiting')
            con.close()
            break
        logging.info(f'Data: {data}')
    
    logging.info('Closing the server')
    s.close()

# Main Function
def main():
    server('localhost', 2607)

if __name__ == '__main__':
    main()