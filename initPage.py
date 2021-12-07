import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore

from inputPage import Buddies

from PyQt5.QtWidgets import QLabel

# Filename: dialog.py

"""Dialog-Style application."""


class InitPage(QWidget):
        login_s = QtCore.pyqtSignal()

        def __init__(self, parent=None):
            super().__init__(parent)
            self.setMinimumSize(400, 200)

            l = QVBoxLayout()
            self.setLayout(l)
            self.usernameInput = QLineEdit()
            self.passwordInput = QLineEdit()
            self.clientIDInput = QLineEdit()
            self.clientSecretInput = QLineEdit()
            self.passwordInput.setEchoMode(QLineEdit.Password)
            usernameInputBuddy = Buddies(QLabel('Username: '), self.usernameInput)
            passwordInputBuddy = Buddies(QLabel('Password: '), self.passwordInput)
            clientIDInputBuddy = Buddies(QLabel('Client ID: ') , self.clientIDInput)
            clientSecretInputBuddy = Buddies(QLabel('Client Secret: '), self.clientSecretInput)
            l.addWidget(Buddies(usernameInputBuddy, passwordInputBuddy))
            l.addWidget(Buddies(clientIDInputBuddy, clientSecretInputBuddy))
            self.login = QPushButton('Login')
            l.addWidget(self.login)
            self.login.clicked.connect(self.login_clicked)
            self.data = []


        @QtCore.pyqtSlot()
        def login_clicked(self): 
            # Collect relevant data and place it in the class for the controller
            # to use 
            self.data = [self.usernameInput.text, self.passwordInput.text, 
            self.clientIDInput.text, self.clientSecretInput.text]
            self.login_s.emit() 


