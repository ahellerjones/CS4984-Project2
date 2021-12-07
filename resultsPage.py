import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QModelIndex
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
    
    def setNewData(self, data):
      i = 0 
      for d in data:
        self._data[i] = data[i]
        i += 1
    
class ABCTableModel(QtCore.QAbstractTableModel):
    def __init__(self,data,parent=None):
        QtCore.QAbstractTableModel.__init__(self,parent)
        self.__data=data     # Initial Data

    def rowCount( self, parent ):
        return len(self.__data)

    def columnCount( self , parent ):
        return len(self.__data[0])

    def data ( self , index , role ):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.__data[row][column]
            return (str(value))

    def setData(self, index, value):
        self.__data[index.row()][index.column()] = value
        return True

    def set(self, row, value):
        self.__data[row][0] = value
        return True

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable      

    def insertRows(self , position , rows , item , parent=QtCore.QModelIndex()):
        # beginInsertRows (self, QModelIndex parent, int first, int last)
        self.beginInsertRows(QtCore.QModelIndex(),len(self.__data),len(self.__data)+1)
        self.__data.append(item) # Item must be an array
        print(item)
        self.endInsertRows()
        return True
    def addColumn(self, name):
        newColumn = self.columnCount(self.parent)
        #self.beginInsertColumns(QModelIndex(), newColumn, newColumn + 1)
        self.beginInsertColumns(QtCore.QModelIndex(),len(self.__data[0]),len(self.__data[0])+1)

        self.__data.append(name)
        for row in self.__data:
            row.append('')
        self.endInsertColumns()
  

'''
Makes Label and table pairs
'''
class LabelTable(QWidget): 
    def __init__(self, label, tableData, parent=None):
        super().__init__(parent)
        self.lay = QVBoxLayout()
        self.setLayout(self.lay)
        self.lay.addWidget(label)
        self.table = QtWidgets.QTableView()
        self.model = ABCTableModel(tableData)
        self.table.setModel(self.model)
        self.lay.addWidget(self.table)

    def addTable(self, data):
        model = TableModel(data)       
        table = QtWidgets.QTableView()
        table.setModel(model)
        self.lay.removeWidget(self.table)
        self.table.deleteLater()
        
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
        self.leftTableData = [
          [''],
        ]
        self.leftTable = LabelTable(QLabel('Relevant subreddits: '), self.leftTableData)



        left = self.leftTable
        main = QWidget()
        mainLayout = QHBoxLayout()
        main.setLayout(mainLayout)

    
        right = QWidget()
        
        rightPanel = QVBoxLayout()
        right.setLayout(rightPanel)



        
        self.TRdata = [
          [''],
        ]
    
        self.BRdata = [
          ['DogsSuck'],
          ['RandomCat'],
          ['jimbob420'],
        ]

        self.TRwidget = LabelTable(QLabel('Top Users: '), self.TRdata)
        BRwidget = LabelTable(QLabel('Top Posts: '), self.BRdata)
        rightPanel.addWidget(self.TRwidget)
        #rightPanel.addWidget(BRwidget)

        
        mainLayout.addWidget(left)
        mainLayout.addWidget(right)
        m.addWidget(main)
        self.searchAgain = QPushButton('Search Again')
        self.searchAgain.clicked.connect(self.return_clicked)
        m.addWidget(self.searchAgain)


