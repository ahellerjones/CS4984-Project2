import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout

from PyQt5.QtWidgets import QLabel

# Filename: dialog.py

"""Dialog-Style application."""


class buddies(QWidget):
        def __init__(self,  lab,  ed, parent=None):
            l = QHBoxLayout()
            l.addWidget(lab)
            l.addWidget(ed)
            self.setLayout(l)


class EntryScreen(QWidget):


    """First screen."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setMinimumSize(400, 600)
        l = QVBoxLayout()
        self.topics = QLineEdit()
        '''
        self.srName = QLineEdit(self)

        self.subs = QHBoxLayout(self)
        self.minSub = QLineEdit(self)
        self.maxSub = QLineEdit(self)
        self.actives = QHBoxLayout(self) 


        self.minActiveUsers = QLineEdit(self)
        self.maxActiveUsers = QLineEdit(self)
        self.userName = QLineEdit(self)
        '''
        
        self.setWindowTitle('CS4984 Reddit Investigation Tool')
        topicsLabel = QLabel('Search terms (seperated by space)')
        # topicsLabel.setBuddy(self.topics)
        jim = QWidget()
        buddies = QHBoxLayout()
        jim.setLayout(buddies)
       
        buddies.addWidget(topicsLabel)
        
        
        buddies.addWidget(self.topics)
        
        l.addWidget(jim)
        self.setLayout(l)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = EntryScreen()
    dlg.show()
    sys.exit(app.exec_())
