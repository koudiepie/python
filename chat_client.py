import socket
host = "172.16.124.74"
port = 6800
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Client端 : 已經連線")
msg = ''
while msg != "bye":
    mydata = input("輸入傳送內容 : ")
    s.send(mydata.encode())
    if mydata == "bye":
        break
    print("Client端 : waiting ...")
    msg = s.recv(1024).decode()
    print(f"顯示收到內容 : {msg}")                   
s.close()
