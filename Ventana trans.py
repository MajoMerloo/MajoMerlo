import tkinter as tk
import customtkinter

root = tk.Tk()
root.title("Ventana Transparente")

# Configura la transparencia de la ventana (0 = completamente transparente, 1 = completamente opaca)
root.attributes("-alpha", 0.3)  # Cambia este valor según lo transparente que desees que sea la ventana

frame = customtkinter.CTkFrame(root)
frame.pack(fill=tk.BOTH, expand=True)

label = customtkinter.CTkLabel(frame, text="Esta es una ventana transparente")
label.pack(pady=20)

button = customtkinter.CTkButton(frame, text="Cerrar", command=root.quit)
button.pack()

root.mainloop()