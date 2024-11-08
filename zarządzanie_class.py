from PySide6.QtWidgets import QApplication, QVBoxLayout, QMessageBox, QWidget, QToolButton, QHBoxLayout, QLabel, QGridLayout, QToolBar, QMainWindow
from PySide6.QtGui import QIcon, QFont, QAction, Qt, QColor


from dodawanie import Dodawanie
from wypisanie import Wypisanie
from usuwanie import Usuwanie
from zamiana import Zamiana

class Menu(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        
        self.setStyleSheet("background-color: #2E3F46")
        self.setWindowTitle("Zarządzanie Pracownikami")
        self.setFixedSize(800,500)
        
        #toolbar
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)  

        toolbar = QToolBar("My Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(Qt.LeftToolBarArea, toolbar)

        toolbar.setStyleSheet("background-color: #1B2F38; color: white;")
        toolbar.setFixedSize(150,700)
        
        spacer = QWidget()
        spacer.setFixedSize(100, 20)
        toolbar.addWidget(spacer)

        info = QAction(QIcon("info.png"), "Informacje o Aplikacji", self)
        info.setToolTip("Informacje o Aplikacji")
        toolbar.addAction(info)
        info.triggered.connect(self.o_aplikacji)

        spacer = QWidget()
        spacer.setFixedSize(100, 20)
        toolbar.addWidget(spacer)

        action1 = QAction("Dodaj Pracownika",self)
        action1.setFont(font)
        action1.triggered.connect(self.dodaj)

        self.button1 = QToolButton()
        self.button1.setDefaultAction(action1)
        self.button1.setFixedSize(140, 50)
        self.button1.setStyleSheet("border: 2px solid #2E3F46; background-color: #2E3F46; margin-left: 5px;")

        self.button1.enterEvent = self.wejście1
        self.button1.leaveEvent = self.wyjście1

        toolbar.addWidget(self.button1)

        spacer = QWidget()
        spacer.setFixedSize(130, 40)
        toolbar.addWidget(spacer)

        action2 = QAction("Usuń Pracownika",self)
        action2.setFont(font)
        action2.triggered.connect(self.usuń)

        self.button2 = QToolButton()
        self.button2.setDefaultAction(action2)
        self.button2.setFixedSize(140, 50)
        self.button2.setStyleSheet("border: 2px solid #2E3F46; background-color: #2E3F46; margin-left: 5px;")

        self.button2.enterEvent = self.wejście2
        self.button2.leaveEvent = self.wyjście2

        toolbar.addWidget(self.button2)

        spacer = QWidget()
        spacer.setFixedSize(100, 40)
        toolbar.addWidget(spacer)

        action3 = QAction("Zmień Dane",self)
        action3.setFont(font)
        action3.triggered.connect(self.zmień_dane)

        self.button3 = QToolButton()
        self. button3.setDefaultAction(action3)
        self.button3.setFixedSize(140, 50)
        self.button3.setStyleSheet("border: 2px solid #2E3F46; background-color: #2E3F46; margin-left: 5px;")

        self.button3.enterEvent = self.wejście3
        self.button3.leaveEvent = self.wyjście3

        toolbar.addWidget(self.button3)

        spacer = QWidget()
        spacer.setFixedSize(100, 40)
        toolbar.addWidget(spacer)

        action4 = QAction("Wypisz Pracowników",self)
        action4.setFont(font)
        action4.triggered.connect(self.wypisz)
        
        self.button4 = QToolButton()
        self.button4.setDefaultAction(action4)
        self.button4.setFixedSize(140, 50)
        self.button4.setStyleSheet("border: 2px solid #2E3F46; background-color: #2E3F46; margin-left: 5px;")

        self.button4.enterEvent = self.wejście4
        self.button4.leaveEvent = self.wyjście4

        toolbar.addWidget(self.button4)

        spacer = QWidget()
        spacer.setFixedSize(100, 20)
        toolbar.addWidget(spacer)

        exit = QAction(QIcon("exit.png"), "Wyjście", self)
        exit.setToolTip("Wyjście z Aplikacji")
        toolbar.addAction(exit)
        exit.triggered.connect(self.exit)


    def o_aplikacji(self):
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Informacje o Aplikacji")
        message.setText("Program służy do zarządzania listą pracowników. Możesz wybrać różne działania na liście pracowników: dodanie pracownika,  usunięcie, wypisanie listy obecnych pracowników czy zmiana ich danych.")
        message.setIcon(QMessageBox.Information)
        message.setStyleSheet("background-color: #2E3F46; color: white;")
        button = message.addButton(QMessageBox.Ok)
        button.setStyleSheet("background-color: #1B2F38")
        message.exec()
  
        
    def exit(self):
        QApplication.quit()
    
    def wejście1(self, event):
        font = QFont()
        font.setPointSize(10)
        font.setBold(True) 
        self.button1.setFont(font)
    
    def wyjście1(self, event):
        font = QFont()
        font.setPointSize(9)
        font.setBold(True) 
        self.button1.setFont(font)
    
    def wejście2(self, event):
        font = QFont()
        font.setPointSize(10)
        font.setBold(True) 
        self.button2.setFont(font)
    
    def wyjście2(self, event):
        font = QFont()
        font.setPointSize(9)
        font.setBold(True) 
        self.button2.setFont(font)

    def wejście3(self, event):
        font = QFont()
        font.setPointSize(10)
        font.setBold(True) 
        self.button3.setFont(font)
    
    def wyjście3(self, event):
        font = QFont()
        font.setPointSize(9)
        font.setBold(True) 
        self.button3.setFont(font)
    
    def wejście4(self, event):
        font = QFont()
        font.setPointSize(10)
        font.setBold(True) 
        self.button4.setFont(font)
    
    def wyjście4(self, event):
        font = QFont()
        font.setPointSize(9)
        font.setBold(True) 
        self.button4.setFont(font)

    def dodaj(self): 
        self.dodawanie = Dodawanie()
        self.dodawanie.show()
        self.setCentralWidget(self.dodawanie)

    def usuń(self):
        self.usuwanie = Usuwanie()
        self.usuwanie.show()
        self.setCentralWidget(self.usuwanie)

    def zmień_dane(self):
        self.zamiana = Zamiana()
        self.zamiana.show()
        self.setCentralWidget(self.zamiana)

    def wypisz(self):
        self.wypisanie = Wypisanie()
        self.wypisanie.show()
        self.setCentralWidget(self.wypisanie)
        
