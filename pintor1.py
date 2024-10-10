import sys 
import requests
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, 
    QTextEdit, QPushButton, QTableWidget, QTableWidgetItem, QLabel
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# Clase principal de la ventana
class Pintor1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sidney Nolan")
        self.setGeometry(100, 100, 800, 600)
        self.initPintor1_UI()

    def initPintor1_UI(self):

        format =QWidget()
        self.setCentralWidget(format)

        pintura1_layout = QHBoxLayout()
        pintura1_img=QLabel("")
        image_url = "https://www.artst.org/wp-content/uploads/2022/04/Sidney-Nolan-768x530.jpg"
        img_data = requests.get(image_url).content
        pixmap = QPixmap()
        pixmap.loadFromData(img_data)
        pintura1_img.setPixmap(pixmap).setScaledContents(True)

        pintura1_Description= QLabel("Descripcion de la pintura")
        pintura1_Description.setAlignment(Qt.AlignTop)
        pintura1_layout.addWidget(pintura1_img)
        pintura1_layout.addWidget(pintura1_Description)
        format.setLayout(pintura1_layout)
        

def main():
    app = QApplication(sys.argv)  # Crear una aplicación
    pintor1 = Pintor1()  # Crear una instancia de la ventana principal
    pintor1.show()  # Mostrar la ventana
    sys.exit(app.exec_())  # Ejecutar el bucle de eventos de la aplicación

# Punto de entrada del programa
if __name__ == '__main__':
    main()