import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout



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


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        table = QtWidgets.QTableView()
        m = QHBoxLayout()
        self.setLayout(m)
        data = [
          ['DogsSuck'],
          ['RandomCat'],
          ['jimbob420'],
        ]

        model = TableModel(data)
        table.setModel(model)

        left = QWidget()
        main = QWidget()
        mainLayout = QHBoxLayout()
        main.setLayout(mainLayout)

        leftLayout = QVBoxLayout()
        left.setLayout(leftLayout)
        leftLayout.addWidget(QLabel('nkjn'))
        leftLayout.addWidget(table)
    
        right = QWidget()
        
        rightPanel = QHBoxLayout()
        right.setLayout(rightPanel)
        tableTR = QtWidgets.QTableView()
        
        TRdata = [
          ['DogsSuck'],
          ['RandomCat'],
          ['jimbob420'],
        ]
    

        rightModel = TableModel(TRdata)
        tableTR.setModel(rightModel)
        TRwidget = QWidget()
        TRlay = QVBoxLayout()
        TRlay.addWidget(QLabel('Top Users: '))
        TRlay.addWidget(tableTR)
        rightPanel.addWidget(TRwidget)
        
        
        mainLayout.addWidget(left)
        mainLayout.addWidget(right)
        m.addWidget(main)
        #self.setCentralWidget(main)


app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()