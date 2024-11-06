from PyQt5.QtWidgets import *
from dataBase import Database


class SearchByIngredientsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.db = Database()

        self.setStyleSheet("font-size:20px; font-weight:500")

        self.searchVerticalLayout = QVBoxLayout()

        self.searchLabel = QLabel("Searching by Ingredients")
        self.searchLabel.setStyleSheet("margin: 15px")

        self.searchEdit = QLineEdit()
        self.searchEdit.setPlaceholderText("Searching by ingredients: ")

        self.searchList = QListWidget() 
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.searchByIngredients)

        self.searchVerticalLayout.addWidget(self.searchLabel)
        self.searchVerticalLayout.addWidget(self.searchEdit)
        self.searchVerticalLayout.addWidget(self.searchList)
        self.searchVerticalLayout.addWidget(self.searchButton)
        self.setLayout(self.searchVerticalLayout)

    def searchByIngredients(self):
        self.data = self.db.searchByIngredients(self.searchEdit.text()) 
        self.searchList.clear()
        for i in self.data:
            self.searchList.addItem(f'''
                            {i[0]}.Name: {i[1]}
                            Ingredients: {i[2]}
                            Instructions: {i[3]}''')
            print(" ")