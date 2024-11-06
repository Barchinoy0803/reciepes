from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from dataBase import Database

class DeleteReciepeWindow(QWidget):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.db = Database()

        self.setStyleSheet("font-size:20px; font-weight:500")

        self.verticalEditLayout = QVBoxLayout()

        self.addLabel = QLabel("Delete Reciepe")
        self.addLabel.setStyleSheet("margin-left:35px")

        self.reciepeNameEdit = QLineEdit()
        self.reciepeNameEdit.setPlaceholderText("Reciepe name:")
    

        self.deleteButton = QPushButton("Delete") 
        self.deleteButton.clicked.connect(self.delete) 
        
        self.verticalEditLayout.addWidget(self.addLabel)
        self.verticalEditLayout.addWidget(self.reciepeNameEdit)
        self.verticalEditLayout.addWidget(self.deleteButton)

        self.setLayout(self.verticalEditLayout)

    def delete(self):
        self.db.deleteReciepe(self.reciepeNameEdit.text())
        self.msg = QMessageBox()
        self.msg.setText("Successfully deleted!")
        self.msg.exec_()
        self.finished.emit()
        self.close()