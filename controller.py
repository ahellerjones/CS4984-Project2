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
from inputPage import InputPage
from initPage import InitPage
from resultsPage import ResultsPage
from PyQt5 import QtCore
import praw 
from psaw import PushshiftAPI
from reddit import mode1, mode2, mode3
from prawcore.exceptions import ResponseException


class Controller(QWidget):
    reddit = None
    api = None


    '''/split

        Connected to the init pages login signal
    '''
    @QtCore.pyqtSlot()
    def login_clicked(self):
        data = self.initPage.data
        if (self.initPage.usernameInput.text() == ""):
            username="Bright_Row4632"
            password="Alpha257!"
            clientID="rA5jrwcLTVhro2QxnggdFQ"
            clientSecret="4OYyJQOSPcVcnrKlZqbER-jwQ1CsoQ"
            self.reddit = praw.Reddit(client_id=clientID, client_secret=clientSecret, 
            user_agent="Test script by u/Bright_Row4632",
            username=username, password=password
            )
            print('bnjhbjhbjhb')
            try:
                print("Authenticated as {}".format(self.reddit.user.me()))
            except ResponseException:
                print("Something went wrong during authentication")
        else:
            self.reddit = praw.Reddit(
            client_id=data[2],
            client_secret=data[3],
            user_agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
            username=data[0],
            password=data[1]
            )

        api = PushshiftAPI(self.reddit) # use this to interface 
        # Start an instance of reddit thing from thgisc login
        #self.initPage.deleteLater()

        self.initPage.setHidden(True)
        self.resultsPage.setHidden(True)
        self.l.addWidget(self.resultsPage)
        self.l.addWidget(self.inputPage)

    '''
        Perform the search
    '''
    @QtCore.pyqtSlot()
    def search_clicked(self):
        search_fields = self.inputPage.topicsString

        # ==== Mode 1 ====
        if (self.inputPage.mode1check.isChecked()):
            print(search_fields)
            urls, subscribers = mode1(search_fields, self.reddit)

            #for url, sub in urls, subscribers: 
                    # TODO subscriber filtering 
            #self.resulbtsPage.leftTable = [urls]
            newTable = []
            for u in urls: 
                newTable.append([u])
            i = 0
            for u in newTable: 
                self.resultsPage.leftTable.model.insertRows(i, 1, u)
                #self.resultsPage.leftTable.model.addColumn([['Jim']])
                i += 1

            print(urls)
        # ==== Mode 2 ====
        if(self.inputPage.mode2check.isChecked()): 
            user = self.inputPage.userName.text()
            print(user)
            userInfo = mode2(user, self.reddit)
            print(userInfo)
            newTable = []
            for u in userInfo: 
                newTable.append([u])
            print(newTable)
            i = 0
            for u in newTable: 
                self.resultsPage.TRwidget.model.insertRows(i, 1, u)
                #self.resultsPage.leftTable.model.addColumn([['Jim']])
                i += 1

        # ==== Mode 3 ====
        if (self.inputPage.mode3check.isChecked()):
            reddits = self.inputPage.reddits.text()
            print(reddits)
            mode3(reddits, int(self.inputPage.numberOfDays.text()))



        # Start an instance of reddit thing from thgisc login
        self.inputPage.setHidden(True)
        self.resultsPage.setHidden(False)

    '''
        Return to input
    '''
    @QtCore.pyqtSlot()
    def return_clicked(self):
        self.resultsPage.setHidden(True)
        self.inputPage.setHidden(False)

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.l = QVBoxLayout()
        self.setLayout(self.l)
        self.setMinimumSize(400, 600)
        self.initPage = InitPage()
        self.inputPage = InputPage()
        self.resultsPage = ResultsPage()
        
        self.l.addWidget(self.initPage)
        self.initPage.login_s.connect(self.login_clicked)
        self.inputPage.search_s.connect(self.search_clicked)
        self.resultsPage.return_s.connect(self.return_clicked)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Controller()
    dlg.show()
    sys.exit(app.exec_())