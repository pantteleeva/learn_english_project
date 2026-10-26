# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_export.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(552, 542)
        MainWindow.setStyleSheet(u"background-color: #FDECEC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 15, 20, 15)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #EBD6D8; \n"
"    border-radius: 16px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"    color: #2B1114; \n"
"    padding-bottom: 4px;\n"
"	background-color: none;\n"
"	border:none;\n"
"}")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C;\n"
"    background-color: none;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_7)

        self.comboBox_2 = QComboBox(self.frame_3)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"QComboBox#comboBox_2 {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C; \n"
"    background-color: #FFFFFF;\n"
"    border: 2px solid #C62828; \n"
"    border-radius: 12px;\n"
"    padding: 6px 35px 6px 16px; \n"
"}\n"
"\n"
"QComboBox#comboBox_2:hover {\n"
"    background-color: #FDECEC; \n"
"    border-color: #A82222; \n"
"}\n"
"\n"
"\n"
"QComboBox#comboBox_2 QAbstractItemView {\n"
"    background-color: #FFFFFF;\n"
"    border: 2px solid #C62828;\n"
"    border-radius: 12px;\n"
"    color: #9B1C1C;\n"
"    selection-background-color: #FDECEC; \n"
"    selection-color: #9B1C1C;\n"
"}")

        self.verticalLayout_6.addWidget(self.comboBox_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C;\n"
"    background-color: none;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_5.addWidget(self.label_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_9 = QPushButton(self.frame_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: #9B1C1C; \n"
"    background-color: #FDECEC;\n"
"    border: 2px solid #9B1C1C;\n"
"    border-radius: 12px;\n"
"    padding: 6px 16px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FAD1D1;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: #9B1C1C; \n"
"    background-color: #FDECEC;\n"
"    border: 2px solid #9B1C1C;\n"
"    border-radius: 12px;\n"
"    padding: 6px 16px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FAD1D1;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: #9B1C1C; \n"
"    background-color: #FDECEC;\n"
"    border: 2px solid #9B1C1C;\n"
"    border-radius: 12px;\n"
"    padding: 6px 16px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FAD1D1;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: #9B1C1C; \n"
"    background-color: #FDECEC;\n"
"    border: 2px solid #9B1C1C;\n"
"    border-radius: 12px;\n"
"    padding: 6px 16px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FAD1D1;\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C;\n"
"    background-color: none;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_2 = QLineEdit(self.frame_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #1A1A1A;\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #9B1C1C;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"}")

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.pushButton_19 = QPushButton(self.frame_3)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: #9B1C1C; \n"
"    background-color: #FDECEC;\n"
"    border: 2px solid #9B1C1C;\n"
"    border-radius: 12px;\n"
"    padding: 6px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FAD1D1;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_19)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.pushButton_13 = QPushButton(self.frame_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: white; \n"
"    background-color: #9B1C1C;\n"
"    border: 2px solid #9B1C1C ;\n"
"    border-radius: 12px;\n"
"    padding: 6px 16px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FAD1D1;\n"
"}")
        self.pushButton_13.setInputMethodHints(Qt.InputMethodHint.ImhPreferLatin)

        self.verticalLayout_3.addWidget(self.pushButton_13)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)


        self.verticalLayout_13.addLayout(self.verticalLayout_8)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"CVG", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"JSON", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u".xlsx", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

