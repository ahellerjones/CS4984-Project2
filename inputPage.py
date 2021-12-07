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
from PyQt5.QtWidgets import QCheckBox
from PyQt5 import QtCore


from PyQt5.QtWidgets import QLabel


"""Dialog-Style application."""


class Buddies(QWidget):
        def __init__(self,  lab,  ed, parent=None):
            super().__init__(parent)

            l = QHBoxLayout()
            l.addWidget(lab)
            l.addWidget(ed)
            self.setLayout(l)


class InputPage(QWidget):
    search_s = QtCore.pyqtSignal()

    @QtCore.pyqtSlot()
    def search_clicked(self): 
        # Collect relevant data and place it in the class for the controller
        # to use 
        self.topicsString = self.topics.text()
        self.search_s.emit() 

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setMinimumSize(400, 600)
        l = QVBoxLayout()
        self.mode1check = QCheckBox("Search for sub reddits")
        self.mode2check = QCheckBox("Get info on a user")
        self.mode3check = QCheckBox("Search subreddits for overlapping users")
        checks = QWidget()
        vert = QVBoxLayout()
        checks.setLayout(vert)
        vert.addWidget(self.mode1check)
        vert.addWidget(self.mode2check)
        vert.addWidget(self.mode3check)
        l.addWidget(checks)

        self.topics = QLineEdit()

        self.srName = QLineEdit()  
        self.userName = QLineEdit()   

        self.reddits = QLineEdit()
        self.numberOfDays = QLineEdit()   

        self.minSub = QLineEdit()
        self.maxSub = QLineEdit()

        self.minActiveUsers = QLineEdit()
        self.maxActiveUsers = QLineEdit()


        topicsBuds = Buddies( QLabel('Search terms (seperated by comma)'), self.topics)
        srNameBuds = Buddies( QLabel('Specific username query'), self.userName)
        redditsBuds= Buddies( QLabel('Find overlapping users among these reddits'), self.reddits)
        numDaysBuds = Buddies( QLabel('Number of days back to search: '), self.numberOfDays)


        minSubBuds = Buddies(QLabel('Min Sub count: '), self.minSub)
        maxSubBuds = Buddies(QLabel('Max Sub count '), self.maxSub)


        subsWidg = Buddies(minSubBuds, maxSubBuds)

        minActiveBuds = Buddies(QLabel('Min active users: '), self.minActiveUsers)
        maxActiveBuds = Buddies(QLabel('Max active users: '), self.maxActiveUsers)

        activeBuds = Buddies(minActiveBuds, maxActiveBuds)
   
        l.addWidget(topicsBuds)
        l.addWidget(srNameBuds)
        l.addWidget(redditsBuds)
        l.addWidget(numDaysBuds)
        l.addWidget(subsWidg)
        l.addWidget(activeBuds)
        self.setLayout(l)
        self.search = QPushButton('Search')
        self.cancel = QPushButton('Cancel')
        l.addWidget(Buddies(self.search, self.cancel))

        self.search.clicked.connect(self.search_clicked)
        self.setWindowTitle('CS4984 Reddit Investigation Tool')
        
       
