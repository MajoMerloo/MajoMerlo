import tkinter as tk
import random
import threading
import serial 
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Entry
from tkinter import StringVar
from tkinter import Spinbox
from tkinter import Button
from tkinter import Label
from tkinter import Scale
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ser = serial.Serial(port='COM6', baudrate=9600, timeout=.1) 

# Función para abrir o cerrar el puerto
def open_close_port():
    if port_button["text"] == "Abrir Puerto":
        # Agregar lógica para abrir el puerto aquí
        port_button["text"] = "Cerrar Puerto"
    else:
        # Agregar lógica para cerrar el puerto aquí
        port_button["text"] = "Abrir Puerto"

# Función para enviar datos
def send_data():
    # Agregar lógica para enviar datos a una PC remota aquí
    pass

# Función para recibir datos
def receive_data():
    # Agregar lógica para recibir datos de una PC remota aquí
    pass

# Función para enviar una secuencia de números
def send_sequence():
    # Agregar lógica para enviar una secuencia de números aquí
    pass

# Función para enviar un archivo TXT
def send_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Agregar lógica para enviar el archivo a una computadora remota aquí
        messagebox.showinfo("Éxito", "Archivo enviado correctamente")

# Simulación de lectura de entradas analógicas
def read_voltage():
    return random.uniform(0, 5)

def read_temperature():
    return random.uniform(20, 30)

# Función para actualizar los gráficos en tiempo real
def update_plots():
    voltage_data.append(read_voltage())
    temperature_data.append(read_temperature())
    voltage_plot.clear()
    temperature_plot.clear()

    voltage_plot.plot(voltage_data)
    temperature_plot.plot(temperature_data)

    voltage_canvas.draw()
    temperature_canvas.draw()

    temperature_bar["value"] = temperature_data[-1]

    app.after(1000, update_plots)

app = tk.Tk()
app.title("Practicas 2 y 3")

# Crear pestañas
notebook = ttk.Notebook(app)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Communication Simple")
notebook.add(tab2, text="Pestaña de Control")
notebook.pack()

# Tab 1 widgets
port_button = tk.Button(tab1, text="Abrir Puerto", bg="medium orchid", command=open_close_port)
port_button.pack()

speed_label = Label(tab1, text="Seleccionar Velocidad:")
speed_label.pack()
speed_combo = ttk.Combobox(tab1, values=["9600", "115200"])
speed_combo.pack()

send_button = tk.Button(tab1, text="Enviar Datos", bg="medium purple", command=send_data)
send_button.pack()

receive_button = tk.Button(tab1, text="Recibir Datos", bg="medium orchid", command=receive_data)
receive_button.pack()

sequence_label = Label(tab1, text="Enviar Secuencia de Números:")
sequence_label.pack()
sequence_spinbox = Spinbox(tab1, from_=1, to=100)
sequence_spinbox.pack()
sequence_button = tk.Button(tab1, text="Enviar Secuencia", bg="medium purple", command=send_sequence)
sequence_button.pack()

delay_label = Label(tab1, text="Seleccionar Retardo:")
delay_label.pack()
delay_scale = Scale(tab1, from_=0, to=10, orient="horizontal")
delay_scale.pack()

file_button = tk.Button(tab1, text="Enviar Archivo", bg="medium orchid", command=send_file)
file_button.pack()

# Tab 2 widgets
voltage_data = []
voltage_fig = Figure(figsize=(5, 3), dpi=100)
voltage_plot = voltage_fig.add_subplot(111)
voltage_canvas = FigureCanvasTkAgg(voltage_fig, master=tab2)
voltage_canvas.get_tk_widget().pack()
temperature_data = []
temperature_fig = Figure(figsize=(5, 3), dpi=100)
temperature_plot = temperature_fig.add_subplot(111)
temperature_canvas = FigureCanvasTkAgg(temperature_fig, master=tab2)
temperature_canvas.get_tk_widget().pack()

temperature_bar_label = Label(tab2, text="Último Valor de Temperatura")
temperature_bar_label.pack()
temperature_bar = Scale(tab2, from_=20, to=30, orient="horizontal")
temperature_bar.set(20)
temperature_bar.pack()

pwm_label = Label(tab2, text="Control PWM")
pwm_label.pack()
pwm_scale = Scale(tab2, from_=0, to=100, orient="horizontal")
pwm_scale.pack()

# Iniciar el hilo para la actualización de los gráficos
update_thread = threading.Thread(target=update_plots)
update_thread.daemon = True
update_thread.start()

#serrial
ser.close
# Main loop
app.mainloop()