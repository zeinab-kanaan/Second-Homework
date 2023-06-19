import socket,threading

quiz_questions = {
    "x+y=? :a.9 or b.10": "a",
    "x-y=? :a.1 or b.-1": "b",
    "x+z=? :a.9 or b.10": "b",
    "x+y+z=? :a.14 or b.10": "a",
    "z+y-x=? :a.9 or b.7": "b",
    "x*y=? :a.9 or b.20": "b",
    "y//x=? :a.1 or b.10": "a",
    "x*x*y? :a.80 or b.10": "a",
    "y*y*x? :a.1 or b.100": "b",
    "z*z*x? :a.144 or b.10": "a",
    "z-y-x? :a.-3 or b.10": "a",
    "z-x? :a.2 or b.10": "a",
    "z*y/x ? :a.7.5 or b.10": "a",
    "x*z/y? :a.1 or b.3.34": "b",
    "y*y-x*x? :a.9 or b.10": "a",
    "x*x+z*y ? :a.46 or b.10": "a",
    "y*z-2x? :a.22 or b.10": "a",
    "2x+2z-y? :a.1 or b.10": "b",
    "3x-z*y? :a.30 or b.10": "a",
    "z-4y+6x? :a.1 or b.10": "b"
}

client_scores = {}

def handle_new_client(client_socket, client_address):
    try:
        client_socket.send(str(len(quiz_questions)).encode())

        for question in quiz_questions:
            client_socket.send(question.encode())

            client_answer = client_socket.recv(1024).decode().strip()

            if client_answer.lower() == quiz_questions[question].lower():
                client_scores[client_address] = client_scores.get(client_address, 0) + 1

        score = client_scores.get(client_address, 0)
        client_socket.send(f"Your Score: {score}/{len(quiz_questions)}\n".encode())

    except ConnectionAbortedError:
        print(f"Connection aborted by the client: {client_address}")

    client_socket.close()
    print(f"Disconnected client: {client_address}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 2525)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print("Quiz Server started. Waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")

        client_thread = threading.Thread(target=handle_new_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    start_server()

