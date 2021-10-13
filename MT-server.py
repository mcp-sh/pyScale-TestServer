import socket
import threading
import time
import random
import datetime

# HOST = ''
PORT = int(sys.argv[1])
# PORT = 1034

msg_count = 0

def craftMessage():
    ct = datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    tare = round(random.uniform(1.0, 5.0), 2)
    net = round(random.uniform(500.0, 505.0), 2)
    gross = round((net + tare), 2)

    string = f"Date Time:             {ct}\n"
    string += f"Gross:           {gross} kg\n"
    string += f"Net:      {net} kg\n"
    string += f"Tare:         {tare} kg\n"
    string += f"*************************\n"

    return string

def threaded_client(conn):
    string = craftMessage()
    rt = random.randint(1,5)
    time.sleep(rt)
    print(f'Sending msg number: {msg_count}')
    conn.send(str.encode(string))
    conn.close()

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    ServerSocket.bind(('', PORT))
except socket.error as e:
    print(str(e))

print(f"Waiting for connection on {PORT}")
ServerSocket.listen(5)

while True:
    conn, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    x = threading.Thread(target=threaded_client, args=(conn, ))
    print('Starting Thread')
    active_threads = threading.active_count()
    msg_count += 1
    print(f'Active Threads: {active_threads}, Message Count: {msg_count}')
    x.start()

ServerSocket.close()
