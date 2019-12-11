import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMessageBox
from PyQt5.QtGui import QIcon
from unicode import Ui_Form
class my_app(QWidget,Ui_Form):
    def __init__(self):
        super(my_app,self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('res/image.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_pyqt_form =my_app()
    my_pyqt_form.show()
    sys.exit(app.exec_())
