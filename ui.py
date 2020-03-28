from PyQt5.QtWidgets import (QApplication,QGridLayout,QWidget,QPushButton,QLabel,QLineEdit,QFrame,QMainWindow,QSplitter,QListWidget,QPlainTextEdit,QDesktopWidget,QFileDialog)
from PyQt5 import QtCore
from PyQt5.QtCore import (Qt,pyqtSignal)
import sys

class Frames(QMainWindow):
	def __init__(self):
		super().__init__()
		self.frameInit()

	def frameInit(self):
		self.grid = QGridLayout()
		self.frame = QFrame()
		self.setCentralWidget(self.frame)
		self.frame.setLayout(self.grid)
		
		self.frame1 = QFrame(self.frame)
		self.frame2 = QFrame(self.frame)
		self.frame3 = QFrame(self.frame)
		self.frame1.setFrameShape(QFrame.StyledPanel)
		self.frame2.setFrameShape(QFrame.StyledPanel)
		self.frame3.setFrameShape(QFrame.StyledPanel)

		self.splitter1=QSplitter(QtCore.Qt.Horizontal)
		self.splitter2=QSplitter(QtCore.Qt.Vertical)

		self.splitter1.addWidget(self.frame1)
		self.splitter1.addWidget(self.frame2)
		self.splitter2.addWidget(self.frame3)
		
		self.splitter2.addWidget(self.splitter1)
		self.grid.addWidget(self.splitter2,0,0)
		
		self.splitter1.setSizes([400,600])
		self.splitter2.setSizes([400,150])

class Widgets(Frames):
	def __init__(self):
		super().__init__()
		self.Frame1()
		self.Frame2()
		self.Frame3()
	def Frame1(self):
		self.grid1 = QGridLayout()
		
		self.start = QPushButton('start')
		self.exit = QPushButton('Exit')

		self.userlabel = QLabel('Username')
		self.userinput = QLineEdit(self.frame1)

		self.passlabel = QLabel('Password')
		self.passinput = QLineEdit(self.frame1)

		self.grid1.addWidget(self.start,0,0,1,2)
		self.grid1.addWidget(self.userlabel,1,0)
		self.grid1.addWidget(self.userinput,1,1)
		self.grid1.addWidget(self.passlabel,2,0)
		self.grid1.addWidget(self.passinput,2,1)
		self.grid1.addWidget(self.exit,3,0,1,2)

		self.frame1.setLayout(self.grid1)
	def Frame2(self):
		self.grid2 = QGridLayout()

		self.jobinput = QLineEdit(self.frame2)
		self.joblabel = QLabel('Job Position')

		self.cityinput = QLineEdit(self.frame2)
		self.citylabel = QLabel('City')

		self.countrylabel=QLabel('Country')
		self.countryinput = QListWidget()

		
		self.exceptionsinput = ClickableLineEdit()
		self.exceptionslabel = QLabel('Exceptions')
		
		self.coverinput = ClickableLineEdit()
		self.coverlabel = QLabel('Cover')
		
		self.cvinput = ClickableLineEdit()
		self.cvlabel = QLabel('CV')

		self.reset = QPushButton('Reset')
		self.check = QPushButton('Check')
		self.addentry = QPushButton('Add')
				
		self.grid2.addWidget(self.countrylabel,1,0,1,1)
		self.grid2.addWidget(self.countryinput,1,1,1,2)
		
		self.grid2.addWidget(self.joblabel,0,0,1,1)
		self.grid2.addWidget(self.jobinput,0,1,1,2)
		
		self.grid2.addWidget(self.citylabel,2,0,1,1)
		self.grid2.addWidget(self.cityinput,2,1,1,2)
		
		self.grid2.addWidget(self.exceptionslabel,3,0,2,1)
		self.grid2.addWidget(self.exceptionsinput,3,1,2,2)
		
		self.grid2.addWidget(self.coverlabel,5,0,2,1)
		self.grid2.addWidget(self.coverinput,5,1,2,2)
		
		self.grid2.addWidget(self.cvlabel,7,0,1,1)
		self.grid2.addWidget(self.cvinput,7,1,1,2)

		self.grid2.addWidget(self.reset,8,2,1,1)
		self.grid2.addWidget(self.check,8,1,1,1)
		self.grid2.addWidget(self.addentry,8,0,1,1)
		
		self.frame2.setLayout(self.grid2)
	def Frame3(self):
		self.grid3 = QGridLayout()

		self.import_=QPushButton('Import')
		self.export=QPushButton('Export')					
		self.save=QPushButton('Save')
		self.clear=QPushButton('Clear')
		self.display = QLabel('')

		self.col1 = QLabel('Index')
		self.col2 = QLabel('Job Title')
		self.col3 = QLabel('Country')
		self.col4 = QLabel('City')
		self.col5 = QLabel('Cover Letter')
		self.col6 = QLabel('CV')
		self.col7 = QLabel('Exceptions')
		self.grid3.addWidget(self.col1,0,0)
		self.grid3.addWidget(self.col2,0,1)
		self.grid3.addWidget(self.col3,0,2)
		self.grid3.addWidget(self.col4,0,3)
		self.grid3.addWidget(self.col5,0,4)
		self.grid3.addWidget(self.col6,0,5)
		self.grid3.addWidget(self.col7,0,6)

		self.grid3.addWidget(self.import_,6,2)
		self.grid3.addWidget(self.export,6,3)
		self.grid3.addWidget(self.save,6,0)
		self.grid3.addWidget(self.clear,6,1)

		self.grid3.addWidget(self.display,1,0,5,9)
		self.frame3.setLayout(self.grid3)

class PopupBox(QWidget):
	def __init__(self,main,var):
		super().__init__()
		self.var = var
		self.main = main
		self.boxgrid = QGridLayout()
		self.setLayout(self.boxgrid)

	def Cover(self):
		label = QLabel('Add a cover letter below or upload a txt file')
		self.field = QPlainTextEdit()
		self.confirmBox = QPushButton('Add cover letter')
		self.cancelBox = QPushButton('Back')
		self.uploadBox = QPushButton('Upload')

		self.boxgrid.addWidget(label,0,0,1,5)
		self.boxgrid.addWidget(self.uploadBox,0,4,1,1)
		self.boxgrid.addWidget(self.field,1,0,5,5)		
		self.boxgrid.addWidget(self.confirmBox,7,0,1,2)
		self.boxgrid.addWidget(self.cancelBox,7,3,1,2)

	def Exceptions(self):
		label = QLabel('Add a list of exceptions, separated by commas')
		self.field = QPlainTextEdit()
		self.confirmBox = QPushButton('Add Exceptions')
		self.cancelBox = QPushButton('Back')
		self.uploadBox = QPushButton('Upload')

		self.boxgrid.addWidget(label,0,0,1,5)
		self.boxgrid.addWidget(self.field,1,0,5,5)		
		self.boxgrid.addWidget(self.confirmBox,7,0,1,2)
		self.boxgrid.addWidget(self.cancelBox,7,3,1,2)

	def Modify(self):
		#self.confirmBox = QPushButton('Add Exceptions')		
		self.jobinput = QLineEdit(self)
		self.joblabel = QLabel('Job Position')

		self.cityinput = QLineEdit(self)
		self.citylabel = QLabel('City')

		self.countrylabel=QLabel('Country')
		self.countryinput = QListWidget()

		
		self.exceptionsinput = QPlainTextEdit()
		self.exceptionslabel = QLabel('Exceptions')
		
		self.coverinput = QPlainTextEdit()
		self.coverlabel = QLabel('Cover')
		
		self.cvinput = ClickableLineEdit()
		self.cvlabel = QLabel('CV')

		self.reset = QPushButton('Reset')
		self.check = QPushButton('Check')
		self.confirmBox = QPushButton('Confirm')
		self.cancelBox = QPushButton('Back')
				
		self.boxgrid.addWidget(self.countrylabel,1,0,1,1)
		self.boxgrid.addWidget(self.countryinput,1,1,1,3)
		
		self.boxgrid.addWidget(self.joblabel,0,0,1,1)
		self.boxgrid.addWidget(self.jobinput,0,1,1,3)
		
		self.boxgrid.addWidget(self.citylabel,2,0,1,1)
		self.boxgrid.addWidget(self.cityinput,2,1,1,3)
		
		self.boxgrid.addWidget(self.exceptionslabel,3,0,2,1)
		self.boxgrid.addWidget(self.exceptionsinput,3,1,10,3)
		
		self.boxgrid.addWidget(self.coverlabel,13,0,10,1)
		self.boxgrid.addWidget(self.coverinput,13,1,10,3)
		
		self.boxgrid.addWidget(self.cvlabel,23,0,1,1)
		self.boxgrid.addWidget(self.cvinput,23,1,1,3)

		self.boxgrid.addWidget(self.reset,24,3,1,1)
		self.boxgrid.addWidget(self.confirmBox,24,0,1,1)
		self.boxgrid.addWidget(self.cancelBox,24,1,1,1)

class Warning(QWidget):
	def __init__(self,text):
		super().__init__()
		grid = QGridLayout()
		label=QLabel(text)
		grid.addWidget(label)
		self.setLayout(grid)

class ClickableLineEdit(QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: self.clicked.emit()
        else: super().mousePressEvent(event)
