import sys
import socket
import logging

def sendData():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.basicConfig(format='%(message)s', level=logging.WARNING)
    server_address = ('0.0.0.0', 45000)
    logging.warning(f"[OPEN SOCKET]\t {server_address}")
    sock.connect(server_address)

    try:
        # Send Data
        message = 'TIME' + chr(13) + chr(10)
        logging.warning(f"[MENGIRIM]\t {message}")
        sock.sendall(message.encode())
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            logging.warning(f"[MENERIMA]\t {data}")
    finally:
        logging.warning("[CLOSE SOCKET]")
        logging.warning("================================================")
        sock.close()
    return

if __name__=='__main__':
    for i in range(1,10):
        senData()
