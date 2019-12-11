import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox
from PyQt5.QtGui import QIcon
from untitled import Ui_Form
from multiprocessing import Process
class MyPyQT_Form(QWidget,Ui_Form):
    def __init__(self):
        super(MyPyQT_Form,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('res/image.ico'))





if __name__ == '__main__':

    app = QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())

