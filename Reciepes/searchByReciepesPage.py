from PyQt5.QtWidgets import *
from dataBase import Database
class SearchByReciepesWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.db = Database()

        self.setStyleSheet("font-size:20px; font-weight:500")

        self.searchVerticalLayout = QVBoxLayout()

        self.searchLabel = QLabel("Searching by Reciepes")
        self.searchLabel.setStyleSheet("margin: 15px")

        self.searchEdit = QLineEdit()
        self.searchEdit.setPlaceholderText("Searching by reciepes: ")

        self.searchList = QListWidget() 
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.searchByReciepes)

        self.searchVerticalLayout.addWidget(self.searchLabel)
        self.searchVerticalLayout.addWidget(self.searchEdit)
        self.searchVerticalLayout.addWidget(self.searchList)
        self.searchVerticalLayout.addWidget(self.searchButton)
        self.setLayout(self.searchVerticalLayout)

    def searchByReciepes(self):
        self.data = self.db.searchByReciepes(self.searchEdit.text())
        self.searchList.clear()
        for i in self.data:
            self.searchList.addItem(f'''
                            {i[0]}.Name: {i[1]}
                            Ingredients: {i[2]}
                            Instructions: {i[3]}''')
            print(" ")