from zarządzanie_class import Menu
from PySide6.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

window = Menu()
window.show()

app.exec() 
