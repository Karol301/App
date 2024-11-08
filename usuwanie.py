from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QScrollArea, QMainWindow
from PySide6.QtGui import QFont, Qt
import os, re, csv

class Usuwanie(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(650,500)

        self.main_layout = QVBoxLayout()

        #dodanie suwaka do przewijania
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(scroll_content)
        self.scroll_area.setWidget(scroll_content)
        
        #dodanie czcionki
        self.font = QFont()
        self.font.setPointSize(9)
        self.font.setBold(True)

        t1 = QLabel("Lista pracowników przed usunięciem:")
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        t1.setFont(font1)
        t1.setFixedHeight(30)
        t1.setStyleSheet("color: white")
        self.scroll_layout.addWidget(t1)

        #wypisanie początkowej listy pracowników
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

        t2 = QLabel("Id pracownika którego chcesz usunąć [3 cyfrowe]")
        t2.setFont(self.font)
        t2.setStyleSheet("color: white")
        self.d2 = QLineEdit()
        self.d2.setFont(self.font)
        self.d2.setStyleSheet("background-color: #1B2F38; color: white")

        hlayout = QHBoxLayout()
        hlayout.addWidget(t2)
        hlayout.addWidget(self.d2)
        
        self.scroll_layout.addLayout(hlayout)

        self.button1 = QPushButton("Usuń")

        self.button1.enterEvent = self.enter1
        self.button1.leaveEvent = self.leave1

        self.button1.setFont(self.font)
        self.button1.setFixedSize(110,40)
        self.button1.setStyleSheet("background-color: #1B2F38; color: white")
        self.button1.clicked.connect(self.usuwanie)
        
        self.button2 = QPushButton("Wyjście")

        self.button2.enterEvent = self.enter2
        self.button2.leaveEvent = self.leave2

        self.button2.setFont(self.font)
        self.button2.setFixedSize(110,40)
        self.button2.setStyleSheet("background-color: #1B2F38; color: white")
        self.button2.clicked.connect(self.zamykanie)

        hlayout = QHBoxLayout()
        hlayout.addWidget(self.button1)
        hlayout.addWidget(self.button2)
        self.scroll_layout.addLayout(hlayout)

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

    def usuwanie(self):
        s_id = self.d2.text()
        pattern = r"^[0-9]{3}$"
        warunek = re.search(pattern, s_id)

        #przypisanie początkowej wartości jako False (nie mamy id) 
        szukanie_id = False

        #sprawdzenie czy id spełnia warunek
        if not warunek:
            error1 = QMessageBox()
            error1.setWindowTitle("Błędne wprowadzenie danych!")
            error1.setText("Źle wprowadziłeś id pracownika, najprawdopodobniej nie podałeś 3 cyfrowej liczby")
            error1.setIcon(QMessageBox.Critical)
            error1.setStyleSheet("background-color: #2E3F46; color: white;")
            button = error1.addButton(QMessageBox.Ok)
            button.setStyleSheet("background-color: #1B2F38")
            error1.exec()

            self.d2.clear()

        else:    
            #przepisanie do pliku wszyskich dzanych oprócz wiersza z podanym id
            with open("pracownicy1.csv", "r") as file1, open("pracownicy2.csv", "w") as file2:
                reader = csv.DictReader(file1)
                for i in reader:
                    if i['idp'] != self.d2.text():
                        dodawanie = csv.DictWriter(file2, fieldnames=["imie","nazwisko","idp","pensja"])
                        if file2.tell() == 0:
                            dodawanie.writeheader()
                        dodawanie.writerow(i)
                    else:
                        #zmiana wartości jeżeli podane id znajduje się w pliku to przyjmuje wartość True
                        szukanie_id = True
            
            self.d2.clear()
        
            os.rename("pracownicy1.csv", "plik_roboczy.csv")   
            os.rename("pracownicy2.csv", "pracownicy1.csv")
            
            os.remove("plik_roboczy.csv")   

            #jeżeli po przeszukaniu pliku nie wartość się nie zmieniła i jest False wyskakuje informacja
            if not szukanie_id:
                error2 = QMessageBox()
                error2.setWindowTitle("Błędne wprowadzenie danych!")
                error2.setText("Najprawdopodobniej nie istnieje pracownik z takim numerem id")
                error2.setIcon(QMessageBox.Critical)
                error2.setStyleSheet("background-color: #2E3F46; color: white;")
                button = error2.addButton(QMessageBox.Ok)
                button.setStyleSheet("background-color: #1B2F38")
                error2.exec()

                #jeżeli wyskoczy ten "error" to wraca do początku funkcji
                return
                       
            p2 = QLabel("")
            t2 = QLabel("Lista pracowników po usunięciu:")
            t2.setStyleSheet("color: white")
            
            font = QFont()
            font.setPointSize(11)
            font.setBold(True)
            t2.setFont(font)

            self.scroll_layout.addWidget(p2)
            self.scroll_layout.addWidget(t2)

            #dodanie nowej listy pracowników po usunięciu
            with open("pracownicy1.csv", "r") as file:
                list = []
                writer = csv.DictReader(file)
                for i in writer:
                    list.append({"imie": i['imie'], "nazwisko": i['nazwisko'], "id": i['idp'], "pensja": i['pensja']})

                if not list:
                    text = QLabel("Lista pracowników jest pusta!")
                    font = QFont()
                    font.setBold(True)
                    font.setPointSize(10)
                    text.setFont(font)
                    text.setStyleSheet("color: white")
                    
                    self.scroll_layout.addWidget(text)
                else:
                    for x in list:
                        p2 = QLabel("")
                        imie2 = QLabel(f"Imie: {x['imie']}")
                        imie2.setFont(self.font)
                        imie2.setStyleSheet("color: white")
                        nazwisko2 = QLabel(f"Naziwsko: {x['nazwisko']}")
                        nazwisko2.setFont(self.font)
                        nazwisko2.setStyleSheet("color: white")
                        id2 = QLabel(f"Id: {x['id']}")
                        id2.setFont(self.font)
                        id2.setStyleSheet("color: white")
                        pensja2 = QLabel(f"Pensja: {x['pensja']}")
                        pensja2.setFont(self.font)
                        pensja2.setStyleSheet("color: white")
                    
                        self.scroll_layout.addWidget(imie2)
                        self.scroll_layout.addWidget(nazwisko2)
                        self.scroll_layout.addWidget(id2)
                        self.scroll_layout.addWidget(pensja2)
                        self.scroll_layout.addWidget(p2)
                    
                    t2 = QLabel("Id pracownika którego chcesz usunąć [3 cyfrowe]")
                    t2.setFont(self.font)
                    t2.setStyleSheet("color: white")
                    self.d2 = QLineEdit()
                    self.d2.setFont(self.font)
                    self.d2.setStyleSheet("background-color: #1B2F38; color: white")

                    hlayout = QHBoxLayout()
                    hlayout.addWidget(t2)
                    hlayout.addWidget(self.d2)
                            
                    self.scroll_layout.addLayout(hlayout)

                    self.button1 = QPushButton("Usuń")

                    self.button1.enterEvent = self.enter1
                    self.button1.leaveEvent = self.leave1

                    self.button1.setFont(self.font)
                    self.button1.setFixedSize(110,40)
                    self.button1.setStyleSheet("background-color: #1B2F38; color: white")
                    self.button1.clicked.connect(self.usuwanie)
                            
                    self.button2 = QPushButton("Wyjście")

                    self.button2.enterEvent = self.enter2
                    self.button2.leaveEvent = self.leave2

                    self.button2.setFont(self.font)
                    self.button2.setFixedSize(110,40)
                    self.button2.setStyleSheet("background-color: #1B2F38; color: white")
                    self.button2.clicked.connect(self.zamykanie)

                    hlayout = QHBoxLayout()
                    hlayout.addWidget(self.button1)
                    hlayout.addWidget(self.button2)
                    self.scroll_layout.addLayout(hlayout)

                    self.main_layout.addWidget(self.scroll_area)
                    self.setLayout(self.main_layout)     

    #dodaje funkję zamknięcia okna 
    def zamykanie(self):
        self.close()
        