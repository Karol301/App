from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QScrollArea
from PySide6.QtGui import QFont

import csv

class Wypisanie(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()

        font = QFont()
        font.setPointSize(9)
        font.setBold(True)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_content)
        scroll_area.setWidget(scroll_content)

        text = QLabel("Lista pracowników:")
        
        text.setStyleSheet("color: white")
        tfont = QFont()
        tfont.setPointSize(11)
        tfont.setBold(True)
        text.setFont(tfont)

        self.scroll_layout.addWidget(text)

        with open ("pracownicy1.csv", "r") as file:
            list = []
            reader = csv.DictReader(file) 

            for i in reader:
                list.append({"imie": i["imie"], "nazwisko": i["nazwisko"], "id": i["idp"], "pensja": i["pensja"]})

            for x in list:
                imie1 = QLabel(f"Imie: {x['imie']}")
                imie1.setFont(font)
                imie1.setStyleSheet("color: white")

                nazwisko1 = QLabel(f"Nazwisko: {x['nazwisko']}")
                nazwisko1.setFont(font)
                nazwisko1.setStyleSheet("color: white")

                id1 = QLabel(f"Id: {x['id']}")
                id1.setFont(font)
                id1.setStyleSheet("color: white")
                
                pensja1 = QLabel(f"Pensja: {x['pensja']}")
                pensja1.setFont(font)
                pensja1.setStyleSheet("color: white")
                p = QLabel("")

                self.scroll_layout.addWidget(imie1)
                self.scroll_layout.addWidget(nazwisko1)
                self.scroll_layout.addWidget(id1)
                self.scroll_layout.addWidget(pensja1)
                self.scroll_layout.addWidget(p)
        
        self.button = QPushButton("Wyjście")
        self.button.setFont(font)
        self.button.setFixedSize(85, 40)
        self.button.setStyleSheet("background-color: #1B2F38; color: white")
        self.button.clicked.connect(self.wyjście)

        self.button.enterEvent = self.enter
        self.button.leaveEvent = self.leave

        self.scroll_layout.addWidget(self.button)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

    def enter(self, event):
        font=QFont()
        font.setPointSize(11)
        font.setBold(True)
            
        self.button.setFont(font)  

    def leave(self, event):          
        font=QFont()
        font.setPointSize(9)
        font.setBold(True)

        self.button.setFont(font) 

    def wyjście(self):
        self.close()