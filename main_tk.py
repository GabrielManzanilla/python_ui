import requests
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk
from tkinter import Toplevel

# Función para obtener una imagen desde una URL
def get_image(url): 
    response = requests.get(url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        return img
    else:
        return None

# Variables globales para controlar el estado
pintores_vistos = set()  # Conjunto para registrar pintores vistos
ventana_abierta = None

# Función para abrir una ventana con la imagen de un pintor
def abrir_ventana(nombre_pintor, img_url):
    global ventana_abierta, pintores_vistos

    # Incrementa al abrir una ventana de un pintor nuevo
    if nombre_pintor not in pintores_vistos:
        pintores_vistos.add(nombre_pintor)

    if ventana_abierta:
        ventana_abierta.destroy()
        
    ventana_abierta = Toplevel(root)
    ventana_abierta.title(nombre_pintor)

    # Etiqueta con el nombre del pintor y la imagen
    label = tk.Label(ventana_abierta, text=f"Pintura del pintor {nombre_pintor}", font=("Arial", 20))
    label.pack(padx=20, pady=20)

    img_get = get_image(img_url)
    img = img_get.resize((400, 600))
    img_tk = ImageTk.PhotoImage(img)
    label.config(image=img_tk)
    label.image_ = img_tk

    boton_cerrar = tk.Button(ventana_abierta, text="Cerrar", command=lambda: cerrar_ventana(ventana_abierta))
    boton_cerrar.pack(pady=10)

    # Posicionar la ventana en la esquina inferior derecha
    ventana_abierta.geometry("500x700+{}+{}".format(
        root.winfo_screenwidth() - 520, root.winfo_screenheight() - 720))
    
    # Verificar si ya se han visto todos los pintores
    verificar_pintores_vistos()

def cerrar_ventana(ventana):
    ventana.destroy()
    global ventana_abierta
    ventana_abierta = None
    # Actualizar el estado del botón "Salir" en cada cierre
    verificar_pintores_vistos()

# Función para verificar el conteo de pintores vistos
def verificar_pintores_vistos():
    if len(pintores_vistos) == 3:
        btn_exit.config(state="normal")  # Habilitar botón de salida
    else:
        btn_exit.config(state="disabled", text="Salir")

# Función para confirmar la salida de la aplicación
def confirmar_salida():
    ventana_salida = Toplevel(root)
    ventana_salida.title("¿Desea salir?")
    label = tk.Label(ventana_salida, text="¿Estás seguro que deseas salir?", font=("Arial", 20))
    label.pack(pady=10)

    boton_volver = tk.Button(ventana_salida, text="Cancelar", command=ventana_salida.destroy)
    boton_volver.pack(pady=10)
    boton_cerrar = tk.Button(ventana_salida, text="Cerrar", command=root.destroy)
    boton_cerrar.pack(pady=10)

# Ventana principal
root = tk.Tk()
root.title("7SA_Equipo#2_Gamboa_Manzanilla_Pérez_Pérez")
root.geometry("700x500+{}+{}".format(
    (root.winfo_screenwidth() - 700) // 2, (root.winfo_screenheight() - 500) // 2))
root.config(bg="lightgreen")

# Botones para los pintores
btn1 = tk.Button(root, text="Sidney Nolan", command=lambda: abrir_ventana("Sidney Nolan", "https://uploads3.wikiart.org/images/sidney-nolan/armoured-helmet-1956.jpg"), bg="white", fg="black", font=("Arial", 12, "bold")) 
btn1.pack(pady=10) 
#btn1.place(x=100, y=50) 
btn2 = tk.Button(root, text="Tom Roberts", command=lambda: abrir_ventana("Tom Roberts", "https://uploads6.wikiart.org/images/tom-roberts/lady-with-a-parasol-1893.jpg!HD.jpg"), bg="white", fg="black", font=("Arial", 12, "bold")) 
btn2.pack(pady=10) 
#btn2.place(x=300, y=50)
btn3 = tk.Button(root, text="Albert Namatjira", command=lambda: abrir_ventana("Albert Namatjira", "https://amuraworld.com/images/articles/141-australia/102-albert-namatjira/103-namatjira1.jpg"), bg="white", fg="black", font=("Arial", 12, "bold")) 
btn3.pack(pady=10) 
#btn3.place(x=500, y=50)

# Botón de salida, inicialmente deshabilitado
btn_exit = tk.Button(root, text="Salir", command=confirmar_salida, state="disabled", bg="white", fg="black", font=("Arial", 12, "bold")) 
btn_exit.pack(pady=10)
#btn_exit.place(x=300, y=120)

root.mainloop()
