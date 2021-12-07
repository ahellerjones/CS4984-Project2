import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton



'''
Wrapper for table data 
'''
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

'''
Makes Label and table pairs
'''
class LabelTable(QWidget): 
    def __init__(self, label, tableData, parent=None):
        super().__init__(parent)
        self.lay = QVBoxLayout()
        self.setLayout(self.lay)
        self.lay.addWidget(label)
        table = QtWidgets.QTableView()
        model = TableModel(tableData)
        table.setModel(model)
        self.lay.addWidget(table)

''' 
holds the main window
'''
class ResultsPage(QWidget):
    return_s = QtCore.pyqtSignal()

    @QtCore.pyqtSlot()
    def return_clicked(self): 
        # Collect relevant data and place it in the class for the controller
        # to use 
        self.return_s.emit() 

      
    def __init__(self, parent=None):
        super().__init__(parent)

        m = QVBoxLayout()
        self.setLayout(m)
        self.leftTable = [
          ['DogsSuck'],
          ['RandomCat'],
          ['jimbob420'],
        ]
        leftTable = LabelTable(QLabel('Relevant subreddits: '), self.leftTable)
        left = leftTable
        main = QWidget()
        mainLayout = QHBoxLayout()
        main.setLayout(mainLayout)

    
        right = QWidget()
        
        rightPanel = QVBoxLayout()
        right.setLayout(rightPanel)



        
        self.TRdata = [
          ['DogsSuck'],
          ['RandomCat'],
          ['jimbob420'],
        ]
    
        self.BRdata = [
          ['DogsSuck'],
          ['RandomCat'],
          ['jimbob420'],
        ]

        TRwidget = LabelTable(QLabel('Top Users: '), self.TRdata)
        BRwidget = LabelTable(QLabel('Top Posts: '), self.BRdata)
        rightPanel.addWidget(TRwidget)
        rightPanel.addWidget(BRwidget)

        
        mainLayout.addWidget(left)
        mainLayout.addWidget(right)
        m.addWidget(main)
        self.searchAgain = QPushButton('Search Again')
        self.searchAgain.clicked.connect(self.return_clicked)
        m.addWidget(self.searchAgain)


