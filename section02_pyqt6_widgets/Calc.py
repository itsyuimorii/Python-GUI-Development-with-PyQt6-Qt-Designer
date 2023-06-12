# Form implementation generated from reading ui file 'Calc.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(" verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_first = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_first.setFont(font)
        self.lineEdit_first.setPlaceholderText("")
        self.lineEdit_first.setObjectName("lineEdit_first")
        self.horizontalLayout.addWidget(self.lineEdit_first)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEdit_second = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_second.setFont(font)
        self.lineEdit_second.setObjectName("lineEdit_second")
        self.horizontalLayout_2.addWidget(self.lineEdit_second)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_add = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setObjectName("pushButton_add")

        self.pushButton_add.clicked.connect(self.add)
        self.horizontalLayout_3.addWidget(self.pushButton_add)
        self.pushButton_minus = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setObjectName("pushButton_minus")

        self.pushButton_minus.clicked.connect(self.minus)
        self.horizontalLayout_3.addWidget(self.pushButton_minus)
        self.pushButton_multi = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_multi.setFont(font)
        self.pushButton_multi.setObjectName("pushButton_multi")

        self.pushButton_multi.clicked.connect(self.multiply)
        self.horizontalLayout_3.addWidget(self.pushButton_multi)
        self.pushButton_add_3 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_add_3.setFont(font)
        self.pushButton_add_3.setObjectName("pushButton_add_3")

        self.pushButton_add_3.clicked.connect(self.divide)
        self.horizontalLayout_3.addWidget(self.pushButton_add_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label_result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("QLabel {\n"
"\n"
"color:green\n"
"\n"
"\n"
"}")
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def add(self):
        fnum = int(self.lineEdit_first.text())
        secnum = int(self.lineEdit_second.text())
        result = fnum + secnum
        self.label_result.setText("Addition : {} ".format(result))

    def minus(self):
        fnum = int(self.lineEdit_first.text())
        secnum = int(self.lineEdit_second.text())
        result = fnum - secnum
        self.label_result.setText("Minus : {} ".format(result))


    def multiply(self):
        fnum = int(self.lineEdit_first.text())
        secnum = int(self.lineEdit_second.text())
        result = fnum * secnum
        self.label_result.setText("Multiplication : {} ".format(result))


    def divide(self):
        fnum = int(self.lineEdit_first.text())
        secnum = int(self.lineEdit_second.text())
        result = fnum / secnum
        self.label_result.setText("Divide : {} ".format(result))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "First Number:"))
        self.label_2.setText(_translate("Form", "Second Number:"))
        self.pushButton_add.setText(_translate("Form", "+"))
        self.pushButton_minus.setText(_translate("Form", "-"))
        self.pushButton_multi.setText(_translate("Form", "*"))
        self.pushButton_add_3.setText(_translate("Form", "/"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())