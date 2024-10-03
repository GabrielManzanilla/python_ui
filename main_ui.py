import sys 
import requests
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, 
    QTextEdit, QPushButton, QTableWidget, QTableWidgetItem, QLabel
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# Clase principal de la ventana
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Título y tamaño de la ventana
        self.setWindowTitle("Pintores de Australia")
        self.resize(700, 400)
        self.initUI()  # Llamada al método que inicializa la interfaz de usuario

        ### Sección encargada de alinear la ventana en la esquina inferior derecha de la pantalla

        # Obtener el tamaño de la pantalla disponible
        screen_geometry = QApplication.desktop().availableGeometry()
        screen_width = screen_geometry.width()   # Ancho de la pantalla
        screen_height = screen_geometry.height() # Altura de la pantalla

        # Obtener el tamaño actual de la ventana
        window_width = self.frameGeometry().width()   # Ancho de la ventana
        window_height = self.frameGeometry().height() # Altura de la ventana

        # Calcular la posición para colocar la ventana en la esquina inferior derecha
        pos_x = screen_width - window_width  # Coordenada X para mover la ventana
        pos_y = screen_height - window_height # Coordenada Y para mover la ventana

        # Mover la ventana a la esquina inferior derecha de la pantalla
        self.move(pos_x, pos_y)

    # Método para inicializar la interfaz de usuario (UI)
    def initUI(self):
        # Crear el widget central de la ventana
        central_widget = QWidget()
        self.setCentralWidget(central_widget)  # Establecer el widget central
        #self.setStyleSheet("background-color: lightgray;")  # Cambia "lightgray" por el color que desees

        # ------------- Primer pintor: Sidney Nolan ----------------
        pintor1 = QWidget()  # Crear un widget contenedor para el pintor 1
        pintor1_layout = QVBoxLayout()  # Diseño vertical para organizar los elementos
        pintor1_nombre = QLabel("Sidney Nolan")  # Etiqueta con el nombre del pintor
        pintor1_nombre.setAlignment(Qt.AlignCenter)  # Centrar el texto
        pintor1_img = QLabel()  # Etiqueta para mostrar la imagen
        pintor1_img.resize(200, 250)  # Tamaño de la imagen
        pintor1_img.setFixedSize(200, 250)  # Fijar el tamaño de la imagen
        # Código comentado para cargar una imagen desde una URL
        # image_url = "https://www.artst.org/wp-content/uploads/2022/04/Sidney-Nolan-768x530.jpg"
        # img_data = requests.get(image_url).content
        # pixmap = QPixmap()
        # pixmap.loadFromData(img_data)
        # pintor1_img.setPixmap(pixmap)
        # pintor1_img.setScaledContents(True)
        pintor1_button = QPushButton("Ver pinturas")  # Botón para "Ver pinturas"
        # Añadir el nombre, la imagen y el botón al diseño
        pintor1_layout.addWidget(pintor1_nombre)
        pintor1_layout.addWidget(pintor1_img)
        pintor1_layout.addWidget(pintor1_button)
        pintor1.setLayout(pintor1_layout)  # Establecer el diseño al widget pintor1
        
        # ------------- Segundo pintor: Tom Roberts (nombre repetido por error) ---------------
        pintor2 = QWidget()  # Crear el widget para el segundo pintor
        pintor2_layout = QVBoxLayout()  # Diseño vertical
        pintor2_nombre = QLabel("Sidney Nolan")  # Nombre del pintor (error en el código original)
        pintor2_nombre.setAlignment(Qt.AlignCenter)  # Centrar el texto
        pintor1_nombre.setStyleSheet("color: white; background-color: darkblue;")

        pintor2_img = QLabel()  # Etiqueta para la imagen
        pintor2_img.resize(200, 250)  # Tamaño de la imagen
        pintor2_img.setFixedSize(200, 250)  # Fijar tamaño
        # Código comentado para cargar una imagen desde una URL
        # image_url = "https://www.artst.org/wp-content/uploads/2022/04/Tom-Roberts.jpg"
        # img_data = requests.get(image_url).content
        # pixmap = QPixmap()
        # pixmap.loadFromData(img_data)
        # pintor2_img.setPixmap(pixmap)
        # pintor2_img.setScaledContents(True)
        pintor2_button = QPushButton("Ver pinturas")  # Botón para "Ver pinturas"
        # Añadir el nombre, la imagen y el botón al diseño
        pintor2_layout.addWidget(pintor2_nombre)
        pintor2_layout.addWidget(pintor2_img)
        pintor2_layout.addWidget(pintor2_button)
        pintor2.setLayout(pintor2_layout)  # Establecer el diseño al widget pintor2

        # ------------- Tercer pintor: Albert Namatjira ----------------
        pintor3 = QWidget()  # Crear el widget para el tercer pintor
        pintor3_layout = QVBoxLayout()  # Diseño vertical
        pintor3_nombre = QLabel("Albert Namatjira")  # Nombre del pintor
        pintor3_nombre.setAlignment(Qt.AlignCenter)  # Centrar el texto
        pintor3_img = QLabel()  # Etiqueta para la imagen
        pintor3_img.resize(200, 250)  # Tamaño de la imagen
        pintor3_img.setFixedSize(200, 250)  # Fijar tamaño
        # Código comentado para cargar una imagen desde una URL
        # image_url = "https://www.artst.org/wp-content/uploads/2022/04/Tom-Roberts.jpg"
        # img_data = requests.get(image_url).content
        # pixmap = QPixmap()
        # pixmap.loadFromData(img_data)
        # pintor3_img.setPixmap(pixmap)
        # pintor3_img.setScaledContents(True)
        pintor3_button = QPushButton("Ver pinturas")  # Botón para "Ver pinturas"
        # Añadir el nombre, la imagen y el botón al diseño
        pintor3_layout.addWidget(pintor3_nombre)
        pintor3_layout.addWidget(pintor3_img)
        pintor3_layout.addWidget(pintor3_button)
        pintor3.setLayout(pintor3_layout)  # Establecer el diseño al widget pintor3

        # ------------- Diseño Horizontal para organizar los tres pintores ------------
        hbox = QHBoxLayout()  # Crear un diseño horizontal
        hbox.addWidget(pintor1)  # Añadir el primer pintor
        hbox.addWidget(pintor2)  # Añadir el segundo pintor
        hbox.addWidget(pintor3)  # Añadir el tercer pintor

        # Asignar el diseño horizontal al widget central
        central_widget.setLayout(hbox)

# Función principal para iniciar la aplicación
def main():
    app = QApplication(sys.argv)  # Crear una aplicación
    main = MainWindow()  # Crear una instancia de la ventana principal
    main.show()  # Mostrar la ventana
    sys.exit(app.exec_())  # Ejecutar el bucle de eventos de la aplicación

# Punto de entrada del programa
if __name__ == '__main__':
    main()
