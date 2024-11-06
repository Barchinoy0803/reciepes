from PyQt5.QtWidgets import *
from dataBase import Database
from PyQt5.QtCore import *

class EditReciepeWindow(QWidget):
    finished = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.db = Database()

        self.setStyleSheet("font-size:20px; font-weight:500")

        self.verticalEditLayout = QVBoxLayout()

        self.addLabel = QLabel("Edit Reciepe")
        self.addLabel.setStyleSheet("margin-left:40px")

        self.enterEdit = QLineEdit()
        self.enterEdit.setPlaceholderText("Enter the reciepe name: ")
        self.reciepeNameEdit = QLineEdit()
        self.reciepeNameEdit.setPlaceholderText("Reciepe name:")
        self.reciepeIngredientsEdit = QLineEdit()
        self.reciepeIngredientsEdit.setPlaceholderText("Ingredients of reciepe: ")
        self.preparingReciepeEdit = QLineEdit()
        self.preparingReciepeEdit.setPlaceholderText("Preparing of reciepe: ")

        self.submitButton = QPushButton("Submit") 
        self.submitButton.clicked.connect(self.submit) 
        self.startEditButton = QPushButton("Start Edit")
        self.startEditButton.clicked.connect(self.startEdit)
        
        self.verticalEditLayout.addWidget(self.enterEdit)
        self.verticalEditLayout.addWidget(self.startEditButton)
        self.verticalEditLayout.addWidget(self.addLabel)
        self.verticalEditLayout.addWidget(self.reciepeNameEdit)
        self.verticalEditLayout.addWidget(self.reciepeIngredientsEdit)
        self.verticalEditLayout.addWidget(self.preparingReciepeEdit)
        self.verticalEditLayout.addWidget(self.submitButton)

        self.setLayout(self.verticalEditLayout)

    def startEdit(self):
        self.data = self.db.getReciepeByName(self.enterEdit.text())
        self.reciepeNameEdit.setText(self.data[1])
        self.reciepeIngredientsEdit.setText(self.data[2])
        self.preparingReciepeEdit.setText(self.data[3])


    def submit(self):
        oldName = self.enterEdit.text()
        newData = {
            'name': self.reciepeNameEdit.text(),
            'ingredients': self.reciepeIngredientsEdit.text(),
            'prepare': self.preparingReciepeEdit.text()
        }
        self.db.updateReciepe(oldName, newData)
        msg = QMessageBox()
        msg.setText("Successfully🥳🥳🥳")
        msg.exec_()
        self.finished.emit()
        self.close()