import requests  # Importa la biblioteca para realizar solicitudes HTTP
from PIL import Image, ImageTk  # Importa para manejar imágenes
from io import BytesIO  # Importa para manejar flujos de bytes
import tkinter as tk  # Importa la biblioteca Tkinter para crear la interfaz gráfica
from tkinter import Toplevel, messagebox  # Importa clases para ventanas adicionales y cuadros de mensaje

# Función para obtener una imagen desde una URL
# Realiza una solicitud HTTP para descargar la imagen, la convierte en un objeto de imagen y la retorna.
def get_image(url):
    response = requests.get(url)  # Realiza una solicitud GET a la URL
    if response.status_code == 200:  # Si la respuesta es exitosa (código 200)
        img = Image.open(BytesIO(response.content))  # Abre la imagen desde el contenido de bytes
        return img  # Devuelve la imagen
    else:
        return None  # Devuelve None si la solicitud falló

# Variables globales para controlar el estado de la aplicación
pintores_vistos = set()  # Conjunto para registrar pintores vistos
ventana_abierta = None  # Variable para rastrear si hay una ventana abierta

# Función para abrir una ventana con la imagen de un pintor
# Esta función crea una nueva ventana con una imagen del pintor y la posiciona.
def abrir_ventana(nombre_pintor, img_url):
    global ventana_abierta, pintores_vistos

    # Incrementa el conjunto si se abre una ventana de un pintor nuevo
    if nombre_pintor not in pintores_vistos:
        pintores_vistos.add(nombre_pintor)

    # Cierra la ventana anterior si ya hay una abierta
    if ventana_abierta:  
        ventana_abierta.destroy()

    ventana_abierta = Toplevel(root)  # Crea una nueva ventana
    ventana_abierta.title(nombre_pintor)  # Establece el título de la ventana

    # Etiqueta con el nombre del pintor
    label = tk.Label(ventana_abierta, text=f"Pintura del pintor {nombre_pintor}", font=("Arial", 20))
    label.pack(padx=20, pady=20)  # Agrega la etiqueta a la ventana

    img_get = get_image(img_url)  # Obtiene la imagen desde la URL
    img = img_get.resize((400, 600))  # Redimensiona la imagen
    img_tk = ImageTk.PhotoImage(img)  # Convierte la imagen a un formato que Tkinter puede usar
    label.config(image=img_tk)  # Configura la etiqueta para mostrar la imagen
    label.image_ = img_tk  # Previene la recolección de basura de la imagen

    # Botón para cerrar la ventana
    boton_cerrar = tk.Button(ventana_abierta, text="Cerrar", command=lambda: cerrar_ventana(ventana_abierta))
    boton_cerrar.pack(pady=10)

    # Posicionar la ventana en la esquina inferior derecha de la pantalla
    ventana_abierta.geometry("500x700+{}+{}".format(
        root.winfo_screenwidth() - 520, root.winfo_screenheight() - 720))

    # Verificar si se han visto todos los pintores
    verificar_pintores_vistos()

# Función para cerrar la ventana
# Destruye la ventana secundaria y actualiza el estado del programa.
def cerrar_ventana(ventana):
    ventana.destroy()  # Cierra la ventana
    global ventana_abierta
    ventana_abierta = None  # Reinicia la variable de la ventana abierta
    verificar_pintores_vistos()  # Actualiza el estado del botón "Salir"

# Función para verificar si se han visto todos los pintores
# Habilita el botón "Salir" si se han visto los 3 pintores.
def verificar_pintores_vistos():
    if len(pintores_vistos) == 3:  # Si se han visto tres pintores
        btn_exit.config(state="normal")  # Habilita el botón de salida
        root.protocol("WM_DELETE_WINDOW", root.destroy)  # Permite cerrar la ventana
    else:
        btn_exit.config(state="disabled", text="Salir")  # Deshabilita el botón
        root.protocol("WM_DELETE_WINDOW", on_closing)  # Muestra un mensaje al intentar cerrar

# Función para confirmar la salida de la aplicación
# Crea una ventana secundaria que pregunta si se desea cerrar la aplicación.
def confirmar_salida():
    ventana_salida = Toplevel(root)  # Crea una ventana para la confirmación
    ventana_salida.title("¿Desea salir?")  # Establece el título de la ventana
    label = tk.Label(ventana_salida, text="¿Estás seguro que deseas salir?", font=("Arial", 20))
    label.pack(pady=10)  # Agrega la etiqueta a la ventana

    boton_volver = tk.Button(ventana_salida, text="Cancelar", command=ventana_salida.destroy)
    boton_volver.pack(pady=10)  # Botón para cancelar
    boton_cerrar = tk.Button(ventana_salida, text="Cerrar", command=root.destroy)
    boton_cerrar.pack(pady=10)  # Botón para cerrar la aplicación

# Función para insertar botones, checkboxes o radiobuttons
# Crea un botón, checkbox o radiobutton según el tipo especificado.
def insert_button(type_button, value, nombre_pintor, img_url):
    if type_button == "button":  # Si el tipo es botón
        return tk.Button(root, text=nombre_pintor, command=lambda: abrir_ventana(nombre_pintor, img_url), bg="white", fg="black", font=("Arial", 12, "bold"))
    elif type_button == "check":  # Si el tipo es checkbox
        check_var = option_vars[value - 1]  # Usa la variable correspondiente
        return tk.Checkbutton(root, text=nombre_pintor, variable=check_var, command=lambda: abrir_ventana(nombre_pintor, img_url), bg="white", fg="black", font=("Arial", 12, "bold"))
    elif type_button == "radio":  # Si el tipo es radiobutton
        return tk.Radiobutton(root, text=nombre_pintor, variable=selected_option, value=value, command=lambda: abrir_ventana(nombre_pintor, img_url), bg="white", fg="black", font=("Arial", 12, "bold"))

# Ventana principal
# Configura la ventana principal, centra la ventana y deshabilita su redimensionamiento.
root = tk.Tk()  # Crea la ventana principal
root.title("7SA_Equipo#2_Gamboa_Manzanilla_Pérez_Pérez")  # Establece el título
root.resizable(width=False, height=False)  # Deshabilita el redimensionamiento
root.geometry("700x500+{}+{}".format(
    (root.winfo_screenwidth() - 700) // 2,  # Calcula la posición X para centrar la ventana
    (root.winfo_screenheight() - 500) // 2))  # Calcula la posición Y para centrar la ventana
root.config(bg="lightgreen")  # Establece el color de fondo

# Función para manejar el cierre de la ventana principal
# Muestra un mensaje de advertencia si se intenta cerrar la aplicación antes de tiempo.
def on_closing():
    messagebox.showinfo("Información", "El botón de cerrar está deshabilitado.")  # Mensaje informativo

root.protocol("WM_DELETE_WINDOW", on_closing)  # Configura la acción al intentar cerrar

# Configuración del modo de botones (botones normales, checkboxes o radiobuttons)
mode = "radio"  # Modo de los botones
if mode == "check":  # Si el modo es checkbox
    option_vars = [tk.IntVar() for _ in range(3)]  
elif mode == "radio":  # Si el modo es radiobutton
    selected_option = tk.IntVar()

# Lista de pintores y sus URLs de imagen
# Crea botones para cada pintor con su respectiva imagen.
for i, pintor in enumerate(["Sidney Nolan", "Tom Roberts", "Albert Namatjira"], start=1):
    img_url = [
        "https://uploads3.wikiart.org/images/sidney-nolan/armoured-helmet-1956.jpg",
        "https://uploads6.wikiart.org/images/tom-roberts/lady-with-a-parasol-1893.jpg!HD.jpg",
        "https://amuraworld.com/images/articles/141-australia/102-albert-namatjira/103-namatjira1.jpg"
    ][i - 1]  # URL de la imagen correspondiente

    btn = insert_button(mode, i, pintor, img_url)  # Crea el botón
    if btn is not None:  # Asegura que el botón se haya creado
        btn.pack(pady=10)  # Empaqueta el botón en la ventana
    else:
        print(f"Error: No se pudo crear el botón para {pintor}")  # Mensaje de error

# Botón de salida, inicialmente deshabilitado
btn_exit = tk.Button(root, text="Salir", command=confirmar_salida, state="disabled", bg="white", fg="black", font=("Arial", 12, "bold"))
btn_exit.pack(pady=10)  # Agrega el botón de salida

root.mainloop()  # Inicia el bucle principal de la interfaz gráfica
