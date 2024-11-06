from PyQt5.QtWidgets import *
from dataBase import Database
from PyQt5.QtCore import *

class AddReciepeWindow(QWidget):
    finished = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.db = Database()

        self.setStyleSheet("font-size:20px; font-weight:500")

        self.verticalEditLayout = QVBoxLayout()

        self.addLabel = QLabel("Add Reciepe")
        self.addLabel.setStyleSheet("margin-left:40px")

        self.reciepeNameEdit = QLineEdit()
        self.reciepeNameEdit.setPlaceholderText("Reciepe name:")
        self.reciepeIngredientsEdit = QLineEdit()
        self.reciepeIngredientsEdit.setPlaceholderText("Ingredients of reciepe: ")
        self.preparingReciepeEdit = QLineEdit()
        self.preparingReciepeEdit.setPlaceholderText("Preparing of reciepe: ")

        self.submitButton = QPushButton("Submit")  
        self.submitButton.clicked.connect(self.submit)
        
        self.verticalEditLayout.addWidget(self.addLabel)
        self.verticalEditLayout.addWidget(self.reciepeNameEdit)
        self.verticalEditLayout.addWidget(self.reciepeIngredientsEdit)
        self.verticalEditLayout.addWidget(self.preparingReciepeEdit)
        self.verticalEditLayout.addWidget(self.submitButton)

        self.setLayout(self.verticalEditLayout)

    def submit(self):
        if self.reciepeNameEdit.text() and self.reciepeIngredientsEdit.text() and self.preparingReciepeEdit.text():
            self.message = self.db.addReciepe(self.reciepeNameEdit.text(), self.reciepeIngredientsEdit.text(), self.preparingReciepeEdit.text())
            self.msg = QMessageBox()
            self.msg.setText(f'{self.message}')
            self.msg.exec_()
            self.reciepeNameEdit.clear()
            self.reciepeIngredientsEdit.clear()
            self.preparingReciepeEdit.clear()
            self.finished.emit()
            self.close()
