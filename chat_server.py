import socket
host = socket.gethostname()
port = 2255
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
print("Server端 : waiting ...")
conn, addr = s.accept()
print("Server端:已經連線")
msg = conn.recv(1024).decode()
while msg != "bye":
    if msg:
        print(f"顯示收到內容 : {msg}")
    mydata = input("輸入傳送內容 : ")
    conn.send(mydata.encode())
    if mydata == "bye":
        break
    print("Server端 : waiting ...")
    msg = conn.recv(1024).decode()
conn.close()
s.close()
