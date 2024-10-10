import requests #Libreria para hacer peticiones a una URL
from PIL import Image, ImageTk #Libreria para trabajar con imagenes
from io import BytesIO #Libreria para trabajar con imagenes usando la data obtenida
import tkinter as tk #Libreria para trabajar con la interfaz grafica
from tkinter import Toplevel #Libreria para trabajar con ventanas emergentes, las coloca en el nivel superior

# Función para obtener una imagen desde una URL
def get_image(url): 
    response = requests.get(url)
    if response.status_code == 200: #Si hay respuesta regresa la imagen, sino no regresa nada
        img= Image.open(BytesIO(response.content))
        return img
    else:
        return None

# Función para abrir una ventana con la imagen de un pintor
def abrir_ventana(nombre_pintor, img_url):
    nueva_ventana = Toplevel(root)
    nueva_ventana.title(nombre_pintor)

    # Etiqueta con el nombre del pintor y la imagen
    label = tk.Label(nueva_ventana, text=f"Pintra del pintor {nombre_pintor}", font=("Arial", 20))
    label.pack(padx=20, pady=20)

    img_get = get_image(img_url)
    img=img_get.resize((400,600))#ajuste de las dimensiones de la imagen 
    img_tk = ImageTk.PhotoImage(img) #Se configura la label para llevar la imagen
    label.config(image=img_tk)
    label.image_= img_tk

    boton_cerrar = tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
    boton_cerrar.pack(pady=10)

    # Configurar el tamaño y la posición de la ventana para que se encueentr en la esquin inferior derecha
    #nueva_ventana.geometry("ancho x alto". format (ancho de la pantalla - ancho de la ventana, alto de la pantalla - alto de la ventana))
    nueva_ventana.geometry("500x700+{}+{}".format(root.winfo_screenwidth() - nueva_ventana.winfo_reqwidth(), root.winfo_screenheight() - nueva_ventana.winfo_reqheight()))

# Función para confirmar la salida de la aplicación
def confirmar_salida():
    ventana_salida = Toplevel(root)
    ventana_salida.title("Desea salir?")
    label=tk.Label(ventana_salida, text=f"¿Estás seguro que deseas salir?", font=("Arial", 20))
    label.pack(pady=10)

    boton_volver = tk.Button(ventana_salida, text="Cancela", command=ventana_salida.destroy) #destroy de la veentana, entonce regresa al root
    boton_volver.pack(pady=10)
    boton_cerrar = tk.Button(ventana_salida, text="Cerrar", command=root.destroy) #destroy de la raiz, entonces se cierra la aplicacion
    boton_cerrar.pack(pady=10)

# Ventana principal
root = tk.Tk()
root.title("7SA_Equipo#2_Gambas_Manzanilla_Pérez_Pérez")
#centrar la ventana en la pantalla
#root.geometry("ancho x alto". format ((ancho de la pantalla - ancho de la ventana) // 2, (alto de la pantalla - alto de la ventana) // 2))
root.geometry("700x500+{}+{}".format((root.winfo_screenwidth() - 700) // 2, (root.winfo_screenheight() - 500) // 2))
root.config(bg="lightgreen")

# Botones
btn1 = tk.Button(root, text="Abrir Ventana 1", command=lambda: abrir_ventana("Sidney Nolan","https://uploads3.wikiart.org/images/sidney-nolan/armoured-helmet-1956.jpg"))
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Abrir Ventana 2", command=lambda: abrir_ventana("Tom Roberts","https://uploads6.wikiart.org/images/tom-roberts/lady-with-a-parasol-1893.jpg!HD.jpg"))
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Abrir Ventana 3", command=lambda: abrir_ventana("Albert Namatjira","https://amuraworld.com/images/articles/141-australia/102-albert-namatjira/103-namatjira1.jpg"))
btn3.pack(pady=10)

btn_exit = tk.Button(root, text="Salir", command=lambda: confirmar_salida())
btn_exit.pack(pady=10)

root.mainloop()

