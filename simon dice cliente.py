import socket
import serial  # Módulo para la comunicación con Arduino
import tkinter as tk

class SimonDiceServer:
    def _init_(self, host, port):
        self.host = host
        self.port = port
       
    arduino = serial.Serial('COM8', 9600)  
    HOST = '192.168.68.92'
    PORT = 65432
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    
    def setup_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server listening on {self.host}:{self.port}")
        conn, addr = self.server_socket.accept()
        print(f"Connected by {addr}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                # Procesa los comandos recibidos del cliente
                if data == b"RED":
                    # Lógica para el botón Rojo
                    self.arduino.write(b"R")
                elif data == b"GREEN":
                    # Lógica para el botón Verde
                    self.arduino.write(b"G")
                elif data == b"BLUE":
                    # Lógica para el botón Azul
                    self.arduino.write(b"B")
                elif data == b"YELLOW":
                    # Lógica para el botón Amarillo
                    self.arduino.write(b"Y")
                elif data == b"OFF":4|14
                    # Lógica para apagar el juego
        self.arduino.write(b"O")
        
        self.server_socket.close()

if __name__== "_main_":
    server_host = '192.168.68.92'  # Puedes cambiar la dirección IP si es necesario
    server_port = 65432  # Cambia el puerto si es necesario

    server = SimonDiceServer(server_host,server_port)