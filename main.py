from PyQt5.QtWidgets import (QApplication)
import sys
import app

class App(app.interface):
	def __init__(self):
		super().__init__()
		self.__adjust__()
		self.show()
	

class Main:
	def __init__(self):
		app = QApplication(sys.argv)
		ui =App()
		sys.exit(app.exec_())

		

if __name__ == '__main__':
	Main()
