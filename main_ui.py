import sys 
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, 
    QTextEdit, QPushButton, QTableWidget, QTableWidgetItem, QLabel
)

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

        pintor1 =  QPushButton("Pintor 1", self)
        pintor2 =  QPushButton("Pintor 2", self)
        pintor3 =  QPushButton("Pintor 3", self)

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
