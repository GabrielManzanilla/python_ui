import requests
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk
from tkinter import Toplevel, messagebox

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


# Función para cerrar una ventana
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
                root.protocol("WM_DELETE_WINDOW", root.destroy)
            else:
                btn_exit.config(state="disabled", text="Salir")
                root.protocol("WM_DELETE_WINDOW", on_closing)


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


# Función para insertar un botón en la ventana principal
def insert_button(type_button, value, nombre_pintor, img_url):
            if type_button == "button":
                return tk.Button(root, text=nombre_pintor, command=lambda: abrir_ventana(nombre_pintor, img_url), bg="white", fg="black", font=("Arial", 12, "bold"))
            elif type_button == "check":
                check_var = option_vars[value - 1]  # Usar la variable correspondiente
                return tk.Checkbutton(root, text=nombre_pintor, variable=check_var, command=lambda: abrir_ventana(nombre_pintor, img_url), bg="white", fg="black", font=("Arial", 12, "bold"))
            elif type_button == "radio":
                return tk.Radiobutton(root, text=nombre_pintor, variable=selected_option, value=value, command=lambda: abrir_ventana(nombre_pintor, img_url), bg="white", fg="black", font=("Arial", 12, "bold"))



# Ventana principal
root = tk.Tk()
root.title("7SA_Equipo#2_Gamboa_Manzanilla_Pérez_Pérez")
# root.maxsize(700, 500)
# root.minsize(700, 500)
root.resizable(width=False, height=False)
root.geometry("700x500+{}+{}".format(
    (root.winfo_screenwidth() - 700) // 2, (root.winfo_screenheight() - 500) // 2))
root.config(bg="lightgreen")
def on_closing():
    # Muestra un mensaje cuando intentan cerrar la ventana
    messagebox.showinfo("Información", "El botón de cerrar está deshabilitado.")

root.protocol("WM_DELETE_WINDOW", on_closing)



# The code snippet you provided is setting the `mode` variable to `"check"`, which indicates the mode
# of the buttons to be created.
mode = "button" #modo de los botones
if mode == "check":
    option_vars = [tk.IntVar() for _ in range(3)]  
elif mode == "radio":
    selected_option = tk.IntVar()



# The commented code block you provided is a loop that iterates over a list of painters' names
# ("Sidney Nolan", "Tom Roberts", "Albert Namatjira") using the `enumerate` function with a starting
# index of 1.
for i, pintor in enumerate(["Sidney Nolan", "Tom Roberts", "Albert Namatjira"], start=1):
    img_url = [
        "https://uploads3.wikiart.org/images/sidney-nolan/armoured-helmet-1956.jpg",
        "https://uploads6.wikiart.org/images/tom-roberts/lady-with-a-parasol-1893.jpg!HD.jpg",
        "https://amuraworld.com/images/articles/141-australia/102-albert-namatjira/103-namatjira1.jpg"
    ][i - 1]  # URL de la imagen correspondiente

    btn = insert_button(mode, i, pintor, img_url)
    if btn is not None:  # Asegurarse de que el botón no sea None
        #btn.pack(pady=10)  # Empaquetar el botón
        btn.place(x=100 + 200 * (i - 1), y=120)  # Posicionar el botón
    else:
        print(f"Error: No se pudo crear el botón para {pintor}")



# # Botón de salida, inicialmente deshabilitado
btn_exit = tk.Button(root, text="Salir", command=confirmar_salida, state="disabled", bg="white", fg="black", font=("Arial", 12, "bold"))
btn_exit.pack(pady=10)
#btn_exit.place(x=300, y=120)

root.mainloop()
