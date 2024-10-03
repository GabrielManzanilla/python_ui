import sys 
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, 
    QTextEdit, QPushButton, QTableWidget, QTableWidgetItem, QLabel
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()


app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())

