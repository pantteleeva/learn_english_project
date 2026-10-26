# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vxod.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: #FDECEC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(150, 100, 150, 100)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: white;\n"
"border-radius: 20px;\n"
"box-shadow: 0 4px 18px rgba(198, 40, 40, 0.08);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 20, 411, 361))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 10, 20, 10)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 32px;\n"
"font-family: Inter;\n"
"font-weight: bold;")

        self.verticalLayout_4.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 11pt;\n"
"    color: #6E4F53; \n"
"    font-weight: normal;\n"
"    padding-bottom: 4px; \n"
"}\n"
"")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    font-family: \"Inter\";\n"
"    font-size: 11pt;\n"
"    color: #2B1114; \n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #EBD6D8; \n"
"    border-radius: 14px; \n"
"    padding-left: 16px;\n"
"    padding-right: 16px;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 8px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #C62828; \n"
"}\n"
"\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #C62828; \n"
"    background-color: #FFF7F6;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.lineEdit)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 11pt;\n"
"    color: #6E4F53; \n"
"    font-weight: normal;\n"
"    padding-bottom: 4px; \n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"    font-family: \"Inter\";\n"
"    font-size: 11pt;\n"
"    color: #2B1114; \n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #EBD6D8; \n"
"    border-radius: 14px; \n"
"    padding-left: 16px;\n"
"    padding-right: 16px;\n"
"    padding-top: 8px;\n"
"    padding-bottom: 8px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid #C62828; \n"
"}\n"
"\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #C62828; \n"
"    background-color: #FFF7F6;\n"
"}\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF; \n"
"    background-color: #9B1C1C; \n"
"    border: none;\n"
"    border-radius: 18px;\n"
"    padding: 10px 24px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #A82222;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8E1B1B; \n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Inter\";\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"    background-color: #FDECEC;\n"
"    color: #9B1C1C; \n"
"    border: none;\n"
"    border-radius: 20px; \n"
"    padding: 10px 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FAD1D1; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #E6B8B8;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
    # retranslateUi

