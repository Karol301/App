from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton, QMessageBox, QScrollArea
from PySide6.QtGui import QFont

import csv, re, os

class Zamiana(QWidget):
    def __init__(self):
        super().__init__()

        self.font = QFont()
        self.font.setPointSize(9)
        self.font.setBold(True)

        tfont = QFont()
        tfont.setPointSize(11)
        tfont.setBold(True)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_content)
        self.scroll_area.setWidget(scroll_content)

        self.main_layout = QVBoxLayout()
        self.vlayout = QVBoxLayout()

        text = QLabel("Lista Pracowników przed zmianą:")
        text.setFont(tfont)
        text.setStyleSheet("color: white")
        self.scroll_layout.addWidget(text)

        with open("pracownicy1.csv", "r") as file1:
            list = []
            reader = csv.DictReader(file1)
            for i in reader:
                list.append({"imie": i['imie'], "nazwisko": i['nazwisko'], "id": i['idp'], "pensja": i['pensja']})
            
            for x in list:
                imie = QLabel(f"Imie: {x['imie']}")
                imie.setFont(self.font)
                imie.setStyleSheet("color: white")

                nazwisko = QLabel(f"Naziwsko: {x['nazwisko']}")
                nazwisko.setFont(self.font)
                nazwisko.setStyleSheet("color: white")

                id1 = QLabel(f"Id: {x['id']}")
                id1.setFont(self.font)
                id1.setStyleSheet("color: white")

                pensja = QLabel(f"Pensja: {x['pensja']}")
                pensja.setFont(self.font)
                pensja.setStyleSheet("color: white")

                p = QLabel("")
            
                self.vlayout.addWidget(imie)
                self.vlayout.addWidget(nazwisko)
                self.vlayout.addWidget(id1)
                self.vlayout.addWidget(pensja)
                self.vlayout.addWidget(p)
        
        t1 = QLabel("Id pracownika którego dane chcesz zmienić [3 cyfrowe]")
        t1.setFont(self.font)
        t1.setStyleSheet("color: white")
        self.id2 = QLineEdit()
        self.id2.setStyleSheet("background-color: #1B2F38; color: white")

        hlayout = QHBoxLayout()
        hlayout.addWidget(t1)
        hlayout.addWidget(self.id2)

        self.scroll_layout.addLayout(self.vlayout)
        self.scroll_layout.addLayout(hlayout)

        i = QLabel("Nowe imie")
        i.setFont(self.font)
        i.setStyleSheet("color: white")
        self.imie2 = QLineEdit()
        self.imie2.setStyleSheet("background-color: #1B2F38; color: white")
        n = QLabel("Nowe nazwisko")
        n.setFont(self.font)
        n.setStyleSheet("color: white")
        self.nazwisko2 = QLineEdit()
        self.nazwisko2.setStyleSheet("background-color: #1B2F38; color: white")
        p = QLabel("Nowa pensja [Minimum 4 cyfrowa]")
        p.setFont(self.font)
        p.setStyleSheet("color: white")
        self.pensja2 = QLineEdit()
        self.pensja2.setStyleSheet("background-color: #1B2F38; color: white")

        h1l = QHBoxLayout()
        h1l.addWidget(i)
        h1l.addWidget(self.imie2)

        h2l = QHBoxLayout()
        h2l.addWidget(n)
        h2l.addWidget(self.nazwisko2)

        h3l = QHBoxLayout()
        h3l.addWidget(p)
        h3l.addWidget(self.pensja2)

        self.scroll_layout.addLayout(h1l)
        self.scroll_layout.addLayout(h2l)
        self.scroll_layout.addLayout(h3l)

        self.button1 = QPushButton("Zamień")
        self.button1.setFont(self.font)
        self.button1.setStyleSheet("background-color: #1B2F38; color: white")
        self.button1.setFixedSize(80,50)
        self.button1.clicked.connect(self.zamiana)

        self.button1.enterEvent = self.enter1
        self.button1.leaveEvent = self.leave1

        self.button2 = QPushButton("Wyjście")
        self.button2.setFont(self.font)
        self.button2.setStyleSheet("background-color: #1B2F38; color: white")
        self.button2.setFixedSize(80,50)
        self.button2.clicked.connect(self.wyjście)

        self.button2.enterEvent = self.enter2
        self.button2.leaveEvent = self.leave2

        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(self.button1)
        hlayout2.addWidget(self.button2)

        self.scroll_layout.addLayout(hlayout2)
        self.main_layout.addWidget(self.scroll_area)

        self.setLayout(self.main_layout)
    
    def enter1(self, event):
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)

        self.button1.setFont(font)
    
    def leave1(self, event):
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)

        self.button1.setFont(font)
    
    def enter2(self, event):
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)

        self.button2.setFont(font)
    
    def leave2(self, event):
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)

        self.button2.setFont(font)

    def zamiana(self):
        pattern1 = r"^[0-9]{3}$"
        warunek1 = re.search(pattern1, self.id2.text())

        pattern2 = r"^[a-zA-ZĄąŻżŹźÓóŁłŃń]+$"
        warunek2 = re.search(pattern2, self.imie2.text())

        pattern3 = r"^[a-zA-ZĄąŻżŹźÓóŁłŃń]+$"
        warunek3 = re.search(pattern3, self.nazwisko2.text())

        pattern4 = r"^[0-9]+$"
        warunek4 = re.search(pattern4, self.pensja2.text())

        if not warunek1:
            error1 = QMessageBox()
            error1.setWindowTitle("Błędne wprowadzenie danych")
            error1.setText("Najprawdopodobniej podane przez ciebie Id nie zawiera 3 cyfrowej liczby") 
            error1.setIcon(QMessageBox.Critical)
            error1.setStyleSheet("background-color: #2E3F46; color: white;")
            button = error1.addButton(QMessageBox.Ok)
            button.setStyleSheet("background-color: #1B2F38")
            error1.exec()

        elif not warunek2:
            error2 = QMessageBox()
            error2.setWindowTitle("Błędne wprowadzenie danych")
            error2.setText("Najprawdopodobniej wprowadzone przez ciebie imię nie zawiera liter") 
            error2.setIcon(QMessageBox.Critical)
            error2.setStyleSheet("background-color: #2E3F46; color: white;")
            button = error2.addButton(QMessageBox.Ok)
            button.setStyleSheet("background-color: #1B2F38")
            error2.exec()

        elif not warunek3:
            error3 = QMessageBox()
            error3.setWindowTitle("Błędne wprowadzenie danych")
            error3.setText("Najprawdopodobniej wprowadzone przez ciebie nazwisko nie zawiera liter") 
            error3.setIcon(QMessageBox.Critical)
            error3.setStyleSheet("background-color: #2E3F46; color: white;")
            button = error3.addButton(QMessageBox.Ok)
            button.setStyleSheet("background-color: #1B2F38")
            error3.exec()  
        
        elif not warunek4:
            error4 = QMessageBox()
            error4.setWindowTitle("Błędne wprowadzenie danych")
            error4.setText("Najprawdopodobniej wprowadzona przez ciebie pensja nie zawiera cyfer") 
            error4.setIcon(QMessageBox.Critical)
            error4.setStyleSheet("background-color: #2E3F46; color: white;")
            button = error4.addButton(QMessageBox.Ok)
            button.setStyleSheet("background-color: #1B2F38")
            error4.exec()

        elif len(self.pensja2.text()) < 4:
            error5 = QMessageBox()
            error5.setWindowTitle("Błędne wprowadzenie danych")
            error5.setText("Najprawdopodobniej wprowadzona przez ciebie pensja nie jesy minimum 4 cyfrowa") 
            error5.setIcon(QMessageBox.Critical)
            error5.setStyleSheet("background-color: #2E3F46; color: white;")
            button = error5.addButton(QMessageBox.Ok)
            button.setStyleSheet("background-color: #1B2F38")
            error5.exec() 

        else:
            with open("pracownicy1.csv", "r") as file2:
                list = []
                reader = csv.DictReader(file2)
                for i in reader:
                    if i['idp'] == self.id2.text():
                        i['nazwisko'] = self.nazwisko2.text()
                        i['imie'] = self.imie2.text()
                        i['pensja'] = self.pensja2.text()
                    list.append(i) 
                
            with open("pracownicy2.csv", "w") as file3:
                writer = csv.DictWriter(file3, fieldnames=["imie", "nazwisko", "idp", "pensja"])
                if file3.tell() == 0:    
                    writer.writeheader()
                writer.writerows(list)
            
            os.rename("pracownicy1.csv", "stary_plik.csv")
            os.rename("pracownicy2.csv", "pracownicy1.csv")

            os.remove("stary_plik.csv")

            t = QLabel("Nowa lista pracowników:")
            t.setFont(self.font)
            t.setStyleSheet("color: white")
            self.scroll_layout.addWidget(t)

            with open("pracownicy1.csv", "r") as file:
                list = []
                reader = csv.DictReader(file)
                for i in reader:
                    list.append({"imie": i['imie'], "nazwisko": i['nazwisko'], "id": i['idp'], "pensja": i['pensja']})
            
            for x in list:
                imie = QLabel(f"Imie: {x['imie']}")
                imie.setFont(self.font)
                imie.setStyleSheet("color: white")

                nazwisko = QLabel(f"Naziwsko: {x['nazwisko']}")
                nazwisko.setFont(self.font)
                nazwisko.setStyleSheet("color: white")

                id1 = QLabel(f"Id: {x['id']}")
                id1.setFont(self.font)
                id1.setStyleSheet("color: white")

                pensja = QLabel(f"Pensja: {x['pensja']}")
                pensja.setFont(self.font)
                pensja.setStyleSheet("color: white")
                p = QLabel("")
            
                self.scroll_layout.addWidget(imie)
                self.scroll_layout.addWidget(nazwisko)
                self.scroll_layout.addWidget(id1)
                self.scroll_layout.addWidget(pensja)
                self.scroll_layout.addWidget(p)
            
            t1 = QLabel("Id pracownika którego dane chcesz zmienić [3 cyfrowe]")
            t1.setFont(self.font)
            t1.setStyleSheet("color: white")
            self.id2 = QLineEdit()
            self.id2.setStyleSheet("background-color: #1B2F38; color: white")

            hlayout = QHBoxLayout()
            hlayout.addWidget(t1)
            hlayout.addWidget(self.id2)

            self.scroll_layout.addLayout(self.vlayout)
            self.scroll_layout.addLayout(hlayout)

            i = QLabel("Nowe imie")
            i.setFont(self.font)
            i.setStyleSheet("color: white")
            self.imie2 = QLineEdit()
            self.imie2.setStyleSheet("background-color: #1B2F38; color: white")
            n = QLabel("Nowe nazwisko")
            n.setFont(self.font)
            n.setStyleSheet("color: white")
            self.nazwisko2 = QLineEdit()
            self.nazwisko2.setStyleSheet("background-color: #1B2F38; color: white")
            p = QLabel("Nowa pensja [Minimum 4 cyfrowa]")
            p.setFont(self.font)
            p.setStyleSheet("color: white")
            self.pensja2 = QLineEdit()
            self.pensja2.setStyleSheet("background-color: #1B2F38; color: white")

            h1l = QHBoxLayout()
            h1l.addWidget(i)
            h1l.addWidget(self.imie2)

            h2l = QHBoxLayout()
            h2l.addWidget(n)
            h2l.addWidget(self.nazwisko2)

            h3l = QHBoxLayout()
            h3l.addWidget(p)
            h3l.addWidget(self.pensja2)

            self.scroll_layout.addLayout(h1l)
            self.scroll_layout.addLayout(h2l)
            self.scroll_layout.addLayout(h3l)

            self.button1 = QPushButton("Zamień")
            self.button1.setFont(self.font)
            self.button1.setStyleSheet("background-color: #1B2F38; color: white")
            self.button1.setFixedSize(80,50)
            self.button1.clicked.connect(self.zamiana)

            self.button1.enterEvent = self.enter1
            self.button1.leaveEvent = self.leave1

            self.button2 = QPushButton("Wyjście")
            self.button2.setFont(self.font)
            self.button2.setStyleSheet("background-color: #1B2F38; color: white")
            self.button2.setFixedSize(80,50)
            self.button2.clicked.connect(self.wyjście)

            self.button2.enterEvent = self.enter2
            self.button2.leaveEvent = self.leave2

            hlayout2 = QHBoxLayout()
            hlayout2.addWidget(self.button1)
            hlayout2.addWidget(self.button2)

            self.scroll_layout.addLayout(hlayout2)
            self.main_layout.addWidget(self.scroll_area)

            self.setLayout(self.main_layout)       

    def wyjście(self):
        self.close()

