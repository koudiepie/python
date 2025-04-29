import socket
import time

host = '172.16.81.137'
port = 5555
address = (host, port)

socket01 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket01.bind(address)

socket01.settimeout(30.0)

print('UDP Socket 啟動')

print('開始寫入影片檔案 "test.mp4"')
mp4File = open('test.mp4', 'wb')

try:
    while True:
        try:
            mp4Data, client_address = socket01.recvfrom(1024)

            if not mp4Data:
                 print("收到空的資料包，可能為結束訊號或錯誤。")
                 break

            mp4File.write(mp4Data)

        except socket.timeout:
            print("Socket 超時：在指定時間內沒有收到資料。")
            break

except Exception as e:
    print(f"發生錯誤: {e}")

finally:
    mp4File.close()
    print('影片已儲存')

    socket01.close()
    print('伺服器關閉')
