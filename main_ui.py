import sys 
import requests
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, 
    QTextEdit, QPushButton, QTableWidget, QTableWidgetItem, QLabel
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pintores de Australia")
        self.resize(700, 400)
        self.initUI()

        ###seccion encargada de obtener alinear la ventana en la esquina inferiror derecha
        #obtener el tamaño de la pantalla
        screen_geometry = QApplication.desktop().availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        #obtener el tamaño de la ventana
        window_width = self.frameGeometry().width()
        window_height = self.frameGeometry().height()
        #calcular la posicion de la esquina superior izquierda para osicionar la ventana en la esquina inferior derecha
        pos_x = screen_width - window_width
        pos_y = screen_height - window_height

        self.move(pos_x, pos_y) #posicionar la ventana en la esquina inferior derecha

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        pintor1= QWidget()
        pintor1_layout = QVBoxLayout()
        pintor1_nombre = QLabel("Sidney Nolan")
        pintor1_nombre.setAlignment(Qt.AlignCenter)
        pintor1_img = QLabel()
        pintor1_img.resize(200,250)
        pintor1_img.setFixedSize(200,250)
        # image_url = "https://www.artst.org/wp-content/uploads/2022/04/Sidney-Nolan-768x530.jpg"
        # img_data = requests.get(image_url).content
        # pixmap = QPixmap()
        # pixmap.loadFromData(img_data)
        # pintor1_img.setPixmap(pixmap)
        # pintor1_img.setScaledContents(True)
        pintor1_button = QPushButton("Ver pinturas")
        pintor1_layout.addWidget(pintor1_nombre)
        pintor1_layout.addWidget(pintor1_img)
        pintor1_layout.addWidget(pintor1_button)
        pintor1.setLayout(pintor1_layout)
        
        pintor2= QWidget()
        pintor2_layout = QVBoxLayout()
        pintor2_nombre = QLabel("Sidney Nolan")
        pintor2_nombre.setAlignment(Qt.AlignCenter)
        pintor2_img = QLabel()
        pintor2_img.resize(200,250)
        pintor2_img.setFixedSize(200,250)
        # image_url = "https://www.artst.org/wp-content/uploads/2022/04/Tom-Roberts.jpg"
        # img_data = requests.get(image_url).content
        # pixmap = QPixmap()
        # pixmap.loadFromData(img_data)
        # pintor2_img.setPixmap(pixmap)
        # pintor2_img.setScaledContents(True)
        pintor2_button = QPushButton("Ver pinturas")
        pintor2_layout.addWidget(pintor2_nombre)
        pintor2_layout.addWidget(pintor2_img)
        pintor2_layout.addWidget(pintor2_button)
        pintor2.setLayout(pintor2_layout)

        pintor3= QWidget()
        pintor3_layout = QVBoxLayout()
        pintor3_nombre = QLabel("Albert Namatjira")
        pintor3_nombre.setAlignment(Qt.AlignCenter)
        pintor3_img = QLabel()
        pintor3_img.resize(200,250)
        pintor3_img.setFixedSize(200,250)
        # image_url = "https://www.artst.org/wp-content/uploads/2022/04/Tom-Roberts.jpg"
        # img_data = requests.get(image_url).content
        # pixmap = QPixmap()
        # pixmap.loadFromData(img_data)
        # pintor3_img.setPixmap(pixmap)
        # pintor3_img.setScaledContents(True)
        pintor3_button = QPushButton("Ver pinturas")
        pintor3_layout.addWidget(pintor3_nombre)
        pintor3_layout.addWidget(pintor3_img)
        pintor3_layout.addWidget(pintor3_button)
        pintor3.setLayout(pintor3_layout)
  

        hbox = QHBoxLayout()
        hbox.addWidget(pintor1)
        hbox.addWidget(pintor2)
        hbox.addWidget(pintor3)

        central_widget.setLayout(hbox)
def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
