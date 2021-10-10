#!/usr/bin/env python3

import socket
import time
import datetime
import random
import sys

HOST = '127.0.0.1'  
PORT = 65436        

def craftMessage():
    ct = datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    tare = round(random.uniform(1.0,5.0),2)
    net = round(random.uniform(500.0,505.0),2)
    gross = round((net + tare),2)

    string = f"Date Time:             {ct}\n"
    string += f"Gross:           {gross} kg\n"
    string += f"Net:      {net} kg\n"
    string += f"Tare:         {tare} kg\n"
    string += f"*************************\n"
    
    return string



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Waiting for Connections on port {PORT}')
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            count = craftMessage()            
            randomInt = random.randint(1,8)
            conn.sendall(count.encode())
            print("Sleeping for " + str(randomInt) + " seconds")
            time.sleep(randomInt)
