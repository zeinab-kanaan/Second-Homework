import socket
print ("x=4","y=5","z=6")
client = input('Enter Name :')
def start_client():
    server_host = 'localhost'
    server_port = 2525
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_host, server_port))
        print(f"Connected to server {server_host}:{server_port}")

        num_questions = int(client_socket.recv(1024).decode())

        for i in range(num_questions):
            question = client_socket.recv(1024).decode()

            answer = input(f"{question}: ")

            client_socket.sendall(answer.encode())

        final_score = client_socket.recv(1024).decode()
        print("Dear ",client ,",Your score is :",final_score)

    except ConnectionRefusedError:
        print("Failed to connect to the server.")
    finally:
        client_socket.close()

if __name__ == '__main__':
    start_client()
