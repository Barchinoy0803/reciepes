from PyQt5.QtWidgets import *
from addReciepePage import AddReciepeWindow
from editReciepePage import EditReciepeWindow
from deleteReciepePage import DeleteReciepeWindow
from searchByIngredientsPage import SearchByIngredientsWindow
from searchByReciepesPage import SearchByReciepesWindow
from dataBase import Database

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.db = Database()

        self.setStyleSheet("font-size:25px; font-weight:600")
        

        self.verticalLayout = QVBoxLayout()
        self.horizontalLayout1 = QHBoxLayout()
        self.horizontalLayout2 = QHBoxLayout()

        self.reciepsList = QListWidget()
        self.addReciepeButton = QPushButton("Add Reciepe")
        self.addReciepeButton.setFixedSize(430,80)
        self.addReciepeButton.clicked.connect(self.clickAddReciepe)
        self.editReciepeButton = QPushButton("Edit Reciepe")
        self.editReciepeButton.setFixedSize(430,80)  
        self.editReciepeButton.clicked.connect(self.editReciepe)
        self.deleteReciepeButton = QPushButton("Delete Reciepe")
        self.deleteReciepeButton.setFixedSize(430,80)
        self.deleteReciepeButton.clicked.connect(self.deleteReciepe)
        self.searchByIngredientsButton = QPushButton("Search by Ingredients")
        self.searchByIngredientsButton.setFixedSize(430,80)  
        self.searchByIngredientsButton.clicked.connect(self.searchByIngredients) 
        self.searchByReciepesButton = QPushButton("Search by Reciepes")
        self.searchByReciepesButton.setFixedSize(430,80)
        self.searchByReciepesButton.clicked.connect(self.searchByReciepes)

        self.verticalLayout.addWidget(self.reciepsList)
        self.horizontalLayout1.addWidget(self.addReciepeButton)
        self.horizontalLayout1.addWidget(self.editReciepeButton)
        self.horizontalLayout1.addWidget(self.deleteReciepeButton)
        self.horizontalLayout2.addWidget(self.searchByIngredientsButton)
        self.horizontalLayout2.addWidget(self.searchByReciepesButton)
        self.verticalLayout.addLayout(self.horizontalLayout1)
        self.verticalLayout.addLayout(self.horizontalLayout2)

        
        self.reciepes = self.db.getAllReciepes()
        self.renderReciepes()
        self.setLayout(self.verticalLayout)

    def renderReciepes(self):
        for i in self.reciepes:
            self.reciepsList.addItem(f'''
                            {i[0]}.Name: {i[1]}
                            Ingredients: {i[2]}
                            Instructions: {i[3]}''')
            print(" ")


    def clickAddReciepe(self):
        self.addreciepe = AddReciepeWindow()
        self.addreciepe.show()
        self.addreciepe.finished.connect(self.updateData)

    def updateData(self):
        self.reciepes = self.db.getAllReciepes()
        self.reciepsList.clear()
        self.renderReciepes()
        print(self.reciepes)

    def editReciepe(self):
        self.editReciepes = EditReciepeWindow()
        self.editReciepes.show()
        self.editReciepes.finished.connect(self.updateData)

    def deleteReciepe(self):
        self.deleted = DeleteReciepeWindow()
        self.deleted.show()
        self.deleted.finished.connect(self.updateData)

    def searchByIngredients(self):
        self.search = SearchByIngredientsWindow()
        self.search.show()
        

    def searchByReciepes(self):
        self.search = SearchByReciepesWindow()
        self.search.show()