# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '2fa.ui'
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
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: #FDECEC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 110, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(202, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: white;\n"
"border-radius: 20px;\n"
"box-shadow: 0 4px 18px rgba(198, 40, 40, 0.08);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(60)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"font-size: 32px;\n"
"font-family: Inter;\n"
"font-weight: bold;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\";\n"
"    font-size: 11pt;\n"
"    color: #6E4F53; \n"
"    font-weight: normal;\n"
"    padding-bottom: 4px;\n"
"}\n"
"")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.lineEdit = QLineEdit(self.frame)
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

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Inter\";\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"    background-color: #C62828;\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 20px; \n"
"    padding: 10px 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A82222; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #8E1B1B; \n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
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


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(202, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 118, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043f\u043e\u0434\u0442\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u0434\u043d\u043e\u0440\u0430\u0437\u043e\u0432\u044b\u0439 \u043a\u043e\u0434", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"6 \u0446\u0438\u0444\u0440", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

