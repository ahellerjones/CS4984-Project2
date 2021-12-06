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
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
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
class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        table = QtWidgets.QTableView()
        m = QVBoxLayout()
        self.setLayout(m)
        self.leftTable = [
          ['DogsSuck'],
          ['RandomCat'],
          ['jimbob420'],
        ]
        leftTable = LabelTable(QLabel('Found Users: '), self.leftTable)
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
        m.addWidget(self.searchAgain)


app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()
