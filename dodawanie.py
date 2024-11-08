from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QApplication, QMessageBox
from PySide6.QtGui import QFont

import csv
import re

class Dodawanie(QWidget):
    def __init__(self):
        super().__init__()

        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
       
        #możliwość wpisania danych
        t1 = QLabel("Imie")
        t1.setFont(font)
        t1.setStyleSheet("color: white")
        self.d1 = QLineEdit()
        self.d1.setStyleSheet("background-color: #1B2F38; color: white;")
        t2 = QLabel("Nazwisko")
        t2.setFont(font)
        t2.setStyleSheet("color: white")
        self.d2 = QLineEdit()
        self.d2.setStyleSheet("background-color: #1B2F38; color: white;")
        t3 = QLabel("Id [3 cyfrowe]")
        t3.setStyleSheet("color: white")
        t3.setFont(font)
        self.d3 = QLineEdit()
        self.d3.setStyleSheet("background-color: #1B2F38; color: white;")
        t4 = QLabel("Pensja [4 cyfrowa]")
        t4.setStyleSheet("color: white")
        t4.setFont(font)
        self.d4 = QLineEdit() 
        self.d4.setStyleSheet("background-color: #1B2F38; color: white;")    

        #pozycjonowanie tekstu 
        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(t1)
        hlayout1.addWidget(self.d1)

        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(t2)
        hlayout2.addWidget(self.d2)

        hlayout3 = QHBoxLayout()
        hlayout3.addWidget(t3)
        hlayout3.addWidget(self.d3)

        hlayout4 = QHBoxLayout()
        hlayout4.addWidget(t4)
        hlayout4.addWidget(self.d4)

        layout = QVBoxLayout()
        layout.addLayout(hlayout1)
        layout.addLayout(hlayout2)
        layout.addLayout(hlayout3)
        layout.addLayout(hlayout4)

        #dodanie przycisków
        self.button1 = QPushButton("Dodaj")
        self.button1.setFont(font)
        self.button1.setStyleSheet("background-color: #1B2F38; color: white;")
        self.button1.setFixedSize(110,40)

        #dodanie działania najechania na przycisk
        self.button1.enterEvent = self.enter1
        self.button1.leaveEvent = self.leave1

        self.button1.clicked.connect(self.dodanie)

        self.button2 = QPushButton("Wyjście")
        self.button2.setFont(font)
        self.button2.setStyleSheet("background-color: #1B2F38; color: white;")
        self.button2.setFixedSize(110,40)

        self.button2.enterEvent = self.enter2
        self.button2.leaveEvent = self.leave2

        self.button2.clicked.connect(self.wyjście)
        
        blayout = QHBoxLayout()
        blayout.addWidget(self.button1)
        blayout.addWidget(self.button2)

        layout.addLayout(blayout)

        self.setLayout(layout)
    
    #dodanie działania jeśli się najedzie się na przycisk i na odwrót
    def enter1(self, event):
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)

        self.button1.setFont(font)
    
    def leave1(self, event):
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)

        self.button1.setFont(font)
    
    def enter2(self, event):
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)

        self.button2.setFont(font)
    
    def leave2(self, event):
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)

        self.button2.setFont(font)

    #dodanie po kliknięciu w przycisk
    def dodanie(self):
        #sprawdzenie czy dane są dobrze wprowadzone
        imie = self.d1.text()
        nazwisko = self.d2.text()
        id = self.d3.text()
        pensja = self.d4.text()
        
        pattern_d1 = r"^[a-zA-ZÓóĘęŃńŻżŹźĄą]+$"
        warunek1 = re.search(pattern_d1, imie)

        pattern_d2 = r"^[a-zA-ZÓóĘęŃńŻżŹźąĄ]+$"
        warunek2 = re.search(pattern_d2, nazwisko)

        pattern_d3 = r"^[0-9]{3}$"
        warunek3 = re.search(pattern_d3, id)

        pattern_d4 = r"^[0-9]+$"
        warunek4 = re.search(pattern_d4, pensja)

        if not warunek1:
             error1 = QMessageBox()
             error1.setMaximumSize(700,200)
             error1.setWindowTitle("Błędne wprowadzenie danych!")
             error1.setText("Źle wprowadziłeś imie pracownika, najprawdopodobniej nie podałeś liter")
             error1.setIcon(QMessageBox.Critical)
             error1.setStyleSheet("background-color: #2E3F46; color: white;")
             button = error1.addButton(QMessageBox.Ok)
             button.setStyleSheet("background-color: #1B2F38")
             error1.exec()
             
             
        elif not warunek2:
            error2 = QMessageBox()
            error2.setWindowTitle("Błędne wprowadzenie danych!")
            error2.setText("Źle wprowadziłeś nazwisko pracownika, najprawdopodobniej nie podałeś liter")
            error2.setIcon(QMessageBox.Critical)
            error2.setStyleSheet("background-color: #2E3F46; color: white;")
            button = error2.addButton(QMessageBox.Ok)
            button.setStyleSheet("background-color: #1B2F38")
            error2.exec()
        
        elif not warunek3:
            error3 = QMessageBox()
            error3.setWindowTitle("Błędne wprowadzenie danych!")
            error3.setText("Źle wprowadziłeś id pracownika, najprawdopodobniej nie podałeś 3 cyfrowej liczby")
            error3.setIcon(QMessageBox.Critical)
            error3.setStyleSheet("background-color: #2E3F46; color: white;")
            button = error3.addButton(QMessageBox.Ok)
            button.setStyleSheet("background-color: #1B2F38")
            error3.exec()

        elif not warunek4:
            error4 = QMessageBox()
            error4.setWindowTitle("Błędne wprowadzenie danych!")
            error4.setText("Źle wprowadziłeś pensję pracownika, najprawdopodobniej nie wprowadziłeś liczby")
            error4.setIcon(QMessageBox.Critical)
            error4.setStyleSheet("background-color: #2E3F46; color: white;")
            button = error4.addButton(QMessageBox.Ok)
            button.setStyleSheet("background-color: #1B2F38")
            error4.exec()
        
        elif len(pensja) < 4:
            error5 = QMessageBox()
            error5.setWindowTitle("Błędne wprowadzenie danych!")
            error5.setText("Źle wprowadziłeś pensję pracownika, najprawdopodobniej jest ona zbyt mała")
            error5.setIcon(QMessageBox.Critical)
            error5.setStyleSheet("background-color: #2E3F46; color: white;")
            button = error5.addButton(QMessageBox.Ok)
            button.setStyleSheet("background-color: #1B2F38")
            error5.exec()

        else:    
            #dodanie danych do pliku
            with open ("pracownicy1.csv", "a") as file:
                dodawanie = csv.DictWriter(file, fieldnames=["imie","nazwisko","idp","pensja"])
                if file.tell() == 0:
                    dodawanie.writeheader()
                dodawanie.writerow({"imie": imie, "nazwisko": nazwisko, "idp": id, "pensja": pensja})
            
        self.d1.clear()
        self.d2.clear()
        self.d3.clear()
        self.d4.clear()

    #zamknięcie po kliknięciu w przycisk
    def wyjście(self):
        self.close()

      