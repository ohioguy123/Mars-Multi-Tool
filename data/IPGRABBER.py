import requests
import json
import socket
import time

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def send_message(webhook, message):
    data = {
        'content': message
    }
    response = requests.post(webhook, json=data)
    if response.status_code != 204:
        print('Message sending failed.')

def get_link():
    return 'https://trollface.dk'

def main():
    webhook = input('Enter your Discord webhook: ')
    if not webhook:
        return
    link = get_link()
    send_message(webhook, f'Your fake website is not ready and this code will finish later it lazy to finish it: {link}')
    time.sleep(1)
    send_message(webhook, 'Waiting for victim...')
    while True:
        ip = get_ip()
        if ip != '127.0.0.1':
            send_message(webhook, f'Gotcha! Victim IP: {ip}')
            break
        time.sleep(1)

if __name__ == '__main__':
    main()