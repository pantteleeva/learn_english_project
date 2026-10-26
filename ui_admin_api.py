# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_api.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 585)
        MainWindow.setStyleSheet(u"background-color: #FDECEC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_13 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"QFrame#frame {\n"
"    background-color: #FFFFFF;\n"
"    border: none;\n"
"    border-bottom: 1px solid #F1DEDE;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setStyleSheet(u"background-color: none;")
        self.label.setPixmap(QPixmap(u":/icons/logo.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton#pushButton_2 {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C; \n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton#pushButton_2:hover {\n"
"    background-color: #FDECEC; \n"
"    border-radius: 12px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton#pushButton_3 {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C; \n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton#pushButton_3:hover {\n"
"    background-color: #FDECEC; \n"
"    border-radius: 12px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C; \n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FDECEC; \n"
"    border-radius: 12px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C; \n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FDECEC; \n"
"    border-radius: 12px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C; \n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FDECEC; \n"
"    border-radius: 12px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C; \n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FDECEC; \n"
"    border-radius: 12px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_11)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: #9B1C1C;\n"
"    background-color: #FDECEC; \n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 6px 16px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FAD1D1;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.horizontalSpacer = QSpacerItem(67, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton#pushButton_6 {\n"
"    background-color: none;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/notification.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_6)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel#label_6 {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"    color: #2B1114;\n"
"	background-color: none;\n"
"}")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton#pushButton {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C; \n"
"    background-color: #FDECEC;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 6px 16px;\n"
"}\n"
"QPushButton#pushButton:hover {\n"
"    background-color: #FAD1D1;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_12.addWidget(self.frame)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 30, 10, 30)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #EBD6D8; \n"
"    border-radius: 16px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setSpacing(12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 15, 20, 15)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"    color: #2B1114; \n"
"    padding-bottom: 4px;\n"
"	background-color: none;\n"
"	border:none\n"
"}")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.frame_2)
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

        self.verticalLayout_5.addWidget(self.label_9)

        self.lineEdit_2 = QLineEdit(self.frame_2)
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

        self.verticalLayout_5.addWidget(self.lineEdit_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C;\n"
"    background-color: none;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_7.addWidget(self.label_10)

        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #1A1A1A;\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #9B1C1C;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"}")

        self.verticalLayout_7.addWidget(self.lineEdit_3)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C;\n"
"    background-color: none;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_8.addWidget(self.label_11)

        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #1A1A1A;\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #9B1C1C;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"}")

        self.verticalLayout_8.addWidget(self.lineEdit_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C;\n"
"    background-color: none;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_9.addWidget(self.label_12)

        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #1A1A1A;\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #9B1C1C;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"}")

        self.verticalLayout_9.addWidget(self.lineEdit_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.pushButton_14 = QPushButton(self.frame_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"")

        self.verticalLayout_10.addWidget(self.pushButton_14)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)


        self.horizontalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #EBD6D8; \n"
"    border-radius: 16px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"    color: #2B1114; \n"
"    padding-bottom: 4px;\n"
"	background-color: none;\n"
"	border:none\n"
"}")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C;\n"
"    background-color: none;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout.addWidget(self.label_4)

        self.comboBox_2 = QComboBox(self.frame_3)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"QComboBox#comboBox_2 {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C;\n"
"    background-color: #FFFFFF;\n"
"    border: 2px solid #C62828;\n"
"    border-radius: 12px;\n"
"    padding: 6px 35px 6px 16px;\n"
"}\n"
"\n"
"QComboBox#comboBox_2:hover {\n"
"    background-color: #FDECEC;\n"
"    border-color: #A82222;\n"
"}\n"
"\n"
"QComboBox#comboBox_2 QAbstractItemView {\n"
"    background-color: #FFFFFF;\n"
"    border: 2px solid #C62828;\n"
"    border-radius: 12px;\n"
"    color: #9B1C1C;\n"
"    selection-background-color: #FDECEC;\n"
"    selection-color: #9B1C1C;\n"
"}")

        self.verticalLayout.addWidget(self.comboBox_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C;\n"
"    background-color: none;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_5)

        self.comboBox_3 = QComboBox(self.frame_3)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"QComboBox#comboBox_3 {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C;\n"
"    background-color: #FFFFFF;\n"
"    border: 2px solid #C62828;\n"
"    border-radius: 12px;\n"
"    padding: 6px 35px 6px 16px;\n"
"}\n"
"\n"
"QComboBox#comboBox_3:hover {\n"
"    background-color: #FDECEC;\n"
"    border-color: #A82222;\n"
"}\n"
"\n"
"QComboBox#comboBox_3 QAbstractItemView {\n"
"    background-color: #FFFFFF;\n"
"    border: 2px solid #C62828;\n"
"    border-radius: 12px;\n"
"    color: #9B1C1C;\n"
"    selection-background-color: #FDECEC;\n"
"    selection-color: #9B1C1C;\n"
"}")

        self.verticalLayout_2.addWidget(self.comboBox_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
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

        self.horizontalLayout_3.addWidget(self.label_7)

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

        self.horizontalLayout_3.addWidget(self.label_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
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
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.frame_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.pushButton_13)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_6.addWidget(self.frame_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"API", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0438", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0438", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b\u044b", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"API", None))
        self.pushButton_6.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"login", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0448\u043d\u0435\u0435 API", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441 API", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447 API", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0430\u0443\u0442, \u0441", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0442\u043e\u0440\u043e\u0432", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0435\u0448 API", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a \u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043a\u0435\u0448\u0430", None))
        self.label_8.setText("")
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043a\u0435\u0448", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0438\u0437 API", None))
    # retranslateUi

