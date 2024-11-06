from PyQt5.QtWidgets import * 
from mainWindow import MainWindow


app = QApplication([])
win = MainWindow()
win.show() 
app.exec_()