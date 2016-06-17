from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ui.loginwindow import Ui_Form


from utils.gui_ini import GuiIni

class MyWindow(QWidget,Ui_Form):
	_signal1 = pyqtSignal()
	_signal2 = pyqtSignal(str)


	def __init__(self,parent = None):
		super(MyWindow,self).__init__(parent = None)
		self.setupUi(self)
		self.btnLogin.clicked.connect(self.login)
		self._signal1.connect(self.mysignalslot1)
		self._signal2.connect(self.mysignalslot2)

	def login(self):
		self.edtID.setText("adsfs")
		self._signal1.emit()
		self._signal2.emit("test")

	def mysignalslot1(self):
		print("da")

	def mysignalslot2(self,parameter):
		print(parameter)

def RunMainWindow():
	import sys
	app = QApplication(sys.argv)
	window = MyWindow()
	window.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	RunMainWindow()
