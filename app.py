import inspect
from PyQt5.QtWidgets import (QApplication,QPushButton,QLabel,QDesktopWidget,QFileDialog)
from PyQt5 import QtCore
from PyQt5.QtGui import (QFont)
import sys
import scripts
import theme
import ui
import os

class Frame1init(ui.Widgets):
	def __init__(self):
		super().__init__()
		self.frame1Config()
	def frame1Config(self):
		self.exit.clicked.connect(QApplication.instance().quit)
class Frame2init(Frame1init):
	def __init__(self):
		super().__init__()
		self.default()
		self.file = 'entries.csv'
		self.displaycount=1
		self.displaydict = {}
		self.entry= scripts.Entry(self.file)		
		self.frame2Config()
		self.show()
	def frame2Config(self):
		country_data=scripts.Load_Data().Load_Countries()
		count = 0
		for i in country_data.Country:
			self.countryinput.insertItem(count,i)
			count +=1
		self.countryinput.clicked.connect(lambda:self.__configureInput__('countryinput'))
		self.jobinput.textChanged.connect(lambda:self.__configureInput__('jobinput'))
		self.cityinput.textChanged.connect(lambda:self.__configureInput__('cityinput'))
		self.cvinput.clicked.connect(self.upload)
		self.exceptionsinput.clicked.connect(lambda: self.ExceptionsPopup('exceptionsinput'))
		self.coverinput.clicked.connect(lambda: self.CoverPopup('coverinput'))
		self.reset.clicked.connect(self.resetData)
		
		self.exceptionsinput.setReadOnly(1)
		self.cvinput.setReadOnly(1)
		self.coverinput.setReadOnly(1)
	def default(self):
		self.jobdata = ''
		self.countrydata = ''
		self.citydata = ''
		self.coverdata = ''
		self.cvdata = ''
		self.exceptionsdata = ''

	def __configureInput__(self,prop):
		if prop == 'countryinput':
			self.countrydata=self.countryinput.currentItem().text()
		elif prop == 'jobinput':
			self.jobdata=self.jobinput.text()
		elif prop == 'cityinput':
			self.citydata=self.cityinput.text()

	def upload(self):
		options = QFileDialog.Options()| QFileDialog.DontUseNativeDialog
		file, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","(*)", options=options)
		if file:
			self.cvdata = file
			self.cvinput.setText(self.cvdata)
	def resetData(self):
		self.default()
		self.jobinput.setText('')
		self.cityinput.setText('')
		self.exceptionsinput.setText('')
		self.coverinput.setText('')
		self.cvinput.setText('')

	def ExceptionsPopup(self,var):
		self.exceptionsbox = popupInterface(self,var)
		text=self.exceptionsbox.Exceptions(self.exceptionsdata)
		
		self.exceptionsbox.show()
		self.exceptionsbox.__adjust__(200,400)

	def CoverPopup(self,var):
		self.coverbox = popupInterface(self,var)
		text=self.coverbox.Cover(self.coverdata)
		self.close()
		self.coverbox.show()
		self.coverbox.__adjust__()
	def ReturnPopup(self,var,text):
		if var == 'exceptionsinput':
			self.exceptionsdata=text.toPlainText().replace('\n','')
			self.exceptionsinput.setText(self.exceptionsdata)
		elif var == 'coverinput':
			self.coverdata=text.toPlainText()
			self.coverinput.setText(self.coverdata)
					
class Frame3init(Frame2init):
	def __init__(self):
		super().__init__()
		self.frame3Config()                                           
	def frame3Config(self,refresh=False):
		self.clear.clicked.connect(self.clearEntries)
		self.save.clicked.connect(self.Save)
		self.export.clicked.connect(self.Export)
		self.import_.clicked.connect(self.Import_)
		
	def Save(self):
		self.entry.__setattr__('self.file',self.file,False)
		self.entry.__write__()
	def Export(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","(*.csv)", options=options)
		if fileName:
			if not fileName.endswith('csv'):
				fileName = f'{fileName}.csv'
			self.entry.__setattr__('self.file',fileName,False)
			self.entry.__write__()
			self.file = fileName
	def Import_(self,file=None):
		
		if file == False:
			options = QFileDialog.Options()| QFileDialog.DontUseNativeDialog
			file, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","(*.csv)", options=options)
		if file:
			if file.endswith('csv'):
				self.entry.__setattr__('self.file',file)
				self.file = file
				self.clearEntries(True)
		
	def clearEntries(self,importbool=False):
		for count,widgets in self.displaydict.items():
			for widget in widgets:
				widget.deleteLater()
		self.displaydict = {}
		self.displaycount = 1
		if self.file == 'entries.csv':
			self.entry.__delete__()
		elif self.file != 'entries.csv' and importbool == False:
			self.file = 'entries.csv'
		else:
			pass
		self.entry= scripts.Entry(self.file)
		self.grid3.addWidget(self.import_,6,2)
		self.grid3.addWidget(self.export,6,3)
		self.grid3.addWidget(self.save,6,0)
		self.grid3.addWidget(self.clear,6,1)
		self.splitter1.setSizes([400,600])
		self.splitter2.setSizes([400,150])
		self.__adjust__()
		self.__adjust__()
		self.displayConfig()

	def __adjust__(self):
		self.resize(1000,550)
		window=QDesktopWidget().availableGeometry()
		window=window.center()
		frame = self.frameGeometry()
		frame = frame.center()
		pos = window - frame
		self.move(pos)
		
	def displayConfig(self):
		pass

class Displayinit(Frame3init):
	def __init__(self):
		super().__init__()
		self.displayConfig()
		self.addentry.clicked.connect(self.addEntry)
	def displayConfig(self):
		
		if len(self.entry.__read__()) != 0:
			
			for entry in self.entry.__read__().iterrows():
				entry = entry[1]
				self.jobdata = str(entry[0])
				self.countrydata = str(entry[1])
				self.citydata = str(entry[2])
				self.coverdata =str(entry[3])
				self.exceptionsdata = str(entry[4])
				self.cvdata = str(entry[5])
				self.addEntry(True)
		self.entry.__read__()

	def addEntry(self,imported=False):
		x={'job':self.jobdata,
		'country':self.countrydata,
		'city':self.citydata,
		'cover':self.coverdata,
		'exceptions':self.exceptionsdata,
		'cv':self.cvdata}
		if imported == False:			
			self.entry.__append__(x)
		self.displaydict[self.displaycount]=[
			QLabel(str(self.displaycount)),
			QLabel(self.jobdata),
			QLabel(self.countrydata),
			QLabel(self.citydata),
			QPushButton('View Cover'),
			QLabel(self.cvdata),
			QPushButton('View Exceptions'),
			QPushButton('Modify'),
			QPushButton('Check'),
			QPushButton('Delete')
			]
		rowcount=0
		index=self.displaydict[self.displaycount][0].text()
		for widget in self.displaydict[self.displaycount]:
			if self.displaydict[self.displaycount].index(widget) == 4:
				pass
				#widget.clicked.connect(self.ExceptionsPopup)
			elif self.displaydict[self.displaycount].index(widget) == 6:
				pass				
				#widget.clicked.connect(self.OpenPopup)
			elif self.displaydict[self.displaycount].index(widget) == 7:			
				widget.clicked.connect(lambda: self.ModifyPopup('Modify',index))
			elif self.displaydict[self.displaycount].index(widget) == 9:
				pass				
				widget.clicked.connect(lambda:self.deleteItem(index))
			widget.setFont(QFont('Ubuntu',10))	
			self.grid3.addWidget(widget,self.displaycount,rowcount)
			rowcount+=1

		if self.displaycount >= 6:
			index=self.displaycount+1
			self.grid3.addWidget(self.import_,index,2)
			self.grid3.addWidget(self.export,index,3)
			self.grid3.addWidget(self.save,index,0)
			self.grid3.addWidget(self.clear,index,1)
		self.displaycount+=1
		self.resetData()
		self.__adjust__()
		self.__adjust__()
	def ModifyPopup(self,var,index):
		tbindex= int(index)-1
		data=self.entry.__getline__(tbindex)
		self.Modifybox = popupInterface(self,var)
		text=self.Modifybox.Modify(data)
		
		self.Modifybox.show()
		self.Modifybox.__adjust__(600,600)
		
	def deleteItem(self,index):
		tbindex = int(index)-1
		x=self.entry.__drop__(tbindex)
		if x is not None:
			self.warning=ui.Warning(x)
			self.warning.show()
			self.warning.setGeometry(0,0,100,100)
		else:
			
			purge = [[widget.deleteLater() for widget in widgets]
				for widgets in [self.displaydict[n]
					 for n in range(1,self.displaycount)]]
			oldself = self.file
			self.entry.__setattr__('self.file','temp.csv',False)
			self.entry.__write__()
			self.Import_('temp.csv')
			self.file = oldself
			self.entry.__setattr__('self.file',self.file,False)
			if os.path.exists('temp.csv'):
				os.remove('temp.csv')
class popupInterface(ui.PopupBox):
	def __init__(self,main,var):
		super().__init__(main,var)
		style = 'factory'
		if style == 'factory':
			self.factoryStyle()
	def Cover(self,cover):
		super().Cover()
		self.cancelBox.clicked.connect(self.back)
		self.confirmBox.clicked.connect(self.back)
		self.uploadBox.clicked.connect(self.upload)
		if cover != '':
			self.field.setPlainText(cover)
	def Exceptions(self,exceptions):
		super().Exceptions()
		self.cancelBox.clicked.connect(self.back)
		self.confirmBox.clicked.connect(self.back)
		if exceptions != '':
			self.field.setPlainText(exceptions)
	def Modify(self,data):
		super().Modify()
		self.field = data
		self.cancelBox.clicked.connect(self.back)
		for i,x in enumerate(self.field):
			if isinstance(x,float):
				self.field[i] = 'Void'
				
		country_data=scripts.Load_Data().Load_Countries()
		count = 0

		for i in country_data.Country:
			self.countryinput.insertItem(count,i)
			count +=1

		self.Modifydefault(self.field)
		self.reset.clicked.connect(self.Modifydefault)
	def Modifydefault(self,vals):

		self.jobdata,self.countrydata,self.citydata,self.coverdata,self.exceptionsdata,self.cvdata=vals
		self.countryinput.setCurrentItem(self.countrydata)
		self.jobinput.setText(self.jobdata)
		self.cityinput.setText(self.citydata)
		self.cvinput.setText(self.cvdata)
		self.exceptionsinput.setPlainText(self.exceptionsdata)
		self.coverinput.setPlainText(self.coverdata)
		
	def __adjust__(self,h=1000,w=550):
		self.resize(h,w)
		window=QDesktopWidget().availableGeometry()
		window=window.center()
		frame = self.frameGeometry()
		frame = frame.center()
		pos = window - frame
		self.move(pos)
	def upload(self):
		options = QFileDialog.Options()| QFileDialog.DontUseNativeDialog
		
		file, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","(*.txt)", options=options)
		if file:
			if file.endswith('txt'):
				text=''
				for i in open(file):
					text = '\n'.join([text,i])
				self.field.insertPlainText(text)
	def back(self):
		self.close()
		self.main.show()
		self.main.ReturnPopup(self.var,self.field)

	def factoryStyle(self):
		self.setStyleSheet(open('mainStyle1.css').read())
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		

class interface(Displayinit):
	def __init__(self):
		super().__init__()
		style = 'factory'
		if style == 'factory':
			self.factoryStyle()
	def factoryStyle(self):
		self.frame.setStyleSheet(theme.factoryStyle().frame)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.frame.setAttribute(QtCore.Qt.WA_TranslucentBackground)

