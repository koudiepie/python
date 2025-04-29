import socket
import cv2
import numpy as np
import os

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5555
IMAGE_TO_SEND = 'solo.png'

def main():
    if not os.path.exists(IMAGE_TO_SEND):
        print(f"錯誤: 找不到影像檔案 '{IMAGE_TO_SEND}'。請檢查路徑。")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"嘗試連線到伺服器 {SERVER_HOST}:{SERVER_PORT}")

    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("連線成功！")

        image = cv2.imread(IMAGE_TO_SEND)

        if image is None:
            print(f"錯誤: 無法讀取影像檔案 '{IMAGE_TO_SEND}'。請確認檔案是有效的影像檔。")
            client_socket.close()
            return

        print("影像讀取成功。")

        _, encoded_image = cv2.imencode('.jpg', image)

        image_data = encoded_image.tobytes()

        image_size = len(image_data)
        print(f"準備傳送影像，大小為 {image_size} 位元組。")

        client_socket.send(image_size.to_bytes(8, byteorder='big'))
        print("已傳送影像大小。")

        client_socket.sendall(image_data)
        print("已傳送影像資料。")

        print("等待接收處理後的影像大小...")

        data = client_socket.recv(8)
        if not data:
            print("錯誤: 伺服器在傳送處理後的影像大小前斷開連線。")
            client_socket.close()
            return

        processed_image_size = int.from_bytes(data, byteorder='big')
        print(f"準備接收處理後的影像，大小為 {processed_image_size} 位元組。")

        processed_image_data = b''
        buffer_size = 4096
        while len(processed_image_data) < processed_image_size:
            bytes_to_receive = min(buffer_size, processed_image_size - len(processed_image_data))
            packet = client_socket.recv(bytes_to_receive)
            if not packet:
                print("錯誤: 在接收處理後的影像資料時伺服器斷開連線。")
                break
            processed_image_data += packet


        if len(processed_image_data) == processed_image_size:
            print("處理後的影像資料接收完成。")

            nparr = np.frombuffer(processed_image_data, np.uint8)
            processed_image = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED) # 或使用 cv2.IMREAD_COLOR

            if processed_image is None:
                print("錯誤: 無法解碼接收到的處理後影像。")
            else:
                print("處理後的影像解碼成功。")
                output_filename = 'received_processed_' + os.path.basename(IMAGE_TO_SEND)
                cv2.imwrite(output_filename, processed_image)
                print(f"處理後的影像已儲存為 '{output_filename}'。")

        else:
             print("警告: 未接收到完整的處理後影像資料。")


    except ConnectionRefusedError:
        print(f"連線被拒絕。請確認伺服器程式在 {SERVER_HOST}:{SERVER_PORT} 執行中。")
    except Exception as e:
        print(f"發生錯誤: {e}")
    finally:
        print("關閉連線。")
        client_socket.close()

if __name__ == "__main__":
    if not os.path.exists(IMAGE_TO_SEND):
        print(f"正在創建測試影像檔案 '{IMAGE_TO_SEND}'...")
        test_img = np.zeros((100, 100, 3), dtype=np.uint8)
        test_img[:, :, 0] = 255
        test_img[25:75, 25:75, 1] = 255
        test_img[50:100, 50:100, 2] = 255
        cv2.imwrite(IMAGE_TO_SEND, test_img)
        print(f"測試影像 '{IMAGE_TO_SEND}' 已創建。")
        print("請重新執行程式以使用此影像。")
    else:
        main()