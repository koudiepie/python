import socket
import cv2
import numpy as np

def process_image(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def main():
    host = '127.0.0.1'
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")

        data = conn.recv(8)
        if not data:
            break
        image_size = int.from_bytes(data, byteorder='big')
        print(f"Receiving image of size {image_size} bytes")

        image_data = b''
        while len(image_data) < image_size:
            packet = conn.recv(4096)
            if not packet:
                break
            image_data += packet

        nparr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if image is None:
            print("Failed to decode image")
            conn.close()
            continue

        print("Image received and decoded")

        processed_image = process_image(image)

        _, encoded_image = cv2.imencode('.jpg', processed_image)
        encoded_image_data = encoded_image.tobytes()

        conn.send(len(encoded_image_data).to_bytes(8, byteorder='big'))

        conn.sendall(encoded_image_data)
        print("Processed image sent back to client")

        conn.close()

if __name__ == "__main__":
    main()
