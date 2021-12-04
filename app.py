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


from PyQt5.QtWidgets import QLabel

# Filename: dialog.py

"""Dialog-Style application."""


class Buddies(QWidget):
        def __init__(self,  lab,  ed, parent=None):
            super().__init__(parent)

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

        self.srName = QLineEdit()  
        self.userName = QLineEdit()   

        self.minSub = QLineEdit()
        self.maxSub = QLineEdit()

        self.minActiveUsers = QLineEdit()
        self.maxActiveUsers = QLineEdit()


        topicsBuds = Buddies( QLabel('Search terms (seperated by comma)'), self.topics)
        srNameBuds = Buddies( QLabel('Specific username query'), self.srName)


        minSubBuds = Buddies(QLabel('Min Sub count: '), self.minSub)
        maxSubBuds = Buddies(QLabel('Max Sub count '), self.maxSub)


        subsWidg = Buddies(minSubBuds, maxSubBuds)

        minActiveBuds = Buddies(QLabel('Min active users: '), self.minActiveUsers)
        maxActiveBuds = Buddies(QLabel('Max active users: '), self.maxActiveUsers)

        activeBuds = Buddies(minActiveBuds, maxActiveBuds)
   
        l.addWidget(topicsBuds)
        l.addWidget(srNameBuds)
        l.addWidget(subsWidg)
        l.addWidget(activeBuds)
        self.setLayout(l)
        self.search = QPushButton('Search')
        self.cancel = QPushButton('Cancel')
        l.addWidget(Buddies(self.search, self.cancel))

        self.setWindowTitle('CS4984 Reddit Investigation Tool')
        
       
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = EntryScreen()
    dlg.show()
    sys.exit(app.exec_())
