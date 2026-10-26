# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_copies.ui'
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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1044, 659)
        MainWindow.setStyleSheet(u"background-color: #FDECEC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_12 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setSpacing(12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(20, 15, 20, 15)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame {\n"
"    background-color: #FFFFFF;\n"
"    border: none;\n"
"    border-bottom: 1px solid #F1DEDE;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
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
        self.pushButton_4.setStyleSheet(u"QPushButton#pushButton_4 {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C; \n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton#pushButton_4:hover {\n"
"    background-color: #FDECEC; \n"
"    border-radius: 12px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_8 = QPushButton(self.frame)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
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


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_11.addWidget(self.frame)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 250))
        self.frame_6.setMaximumSize(QSize(16777215, 250))
        self.frame_6.setStyleSheet(u"QFrame#frame_6 {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #EBD6D8; \n"
"    border-radius: 16px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 15, 20, 15)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel#label_2 {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"    color: #2B1114; \n"
"    padding-bottom: 4px;\n"
"	background-color: none;\n"
"}")

        self.verticalLayout_5.addWidget(self.label_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_6)
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

        self.verticalLayout_4.addWidget(self.label_4)

        self.comboBox = QComboBox(self.frame_6)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox#comboBox {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C; \n"
"    background-color: #FFFFFF;\n"
"    border: 2px solid #C62828; \n"
"    border-radius: 12px;\n"
"    padding: 6px 35px 6px 16px; \n"
"}\n"
"\n"
"QComboBox#comboBox:hover {\n"
"    background-color: #FDECEC; \n"
"    border-color: #A82222; \n"
"}\n"
"\n"
"\n"
"QComboBox#comboBox QAbstractItemView {\n"
"    background-color: #FFFFFF;\n"
"    border: 2px solid #C62828;\n"
"    border-radius: 12px;\n"
"    color: #9B1C1C;\n"
"    selection-background-color: #FDECEC; \n"
"    selection-color: #9B1C1C;\n"
"}")

        self.verticalLayout_4.addWidget(self.comboBox)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame_6)
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

        self.comboBox_2 = QComboBox(self.frame_6)
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

        self.verticalLayout_2.addWidget(self.comboBox_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.frame_6)
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

        self.verticalLayout.addWidget(self.label_7)

        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #1A1A1A;\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #9B1C1C;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.pushButton_12 = QPushButton(self.frame_6)
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
"QPushButton:hover {\n"
"    background-color: #FAD1D1;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.pushButton_12)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)


        self.horizontalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.centralwidget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 250))
        self.frame_7.setMaximumSize(QSize(16777215, 250))
        self.frame_7.setStyleSheet(u"QFrame#frame_7 {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #EBD6D8; \n"
"    border-radius: 16px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setSpacing(12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 15, 20, 15)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel#label_3 {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"    color: #2B1114; \n"
"    padding-bottom: 4px;\n"
"	background-color: none;\n"
"}")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_7 = QPushButton(self.frame_7)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_6.addWidget(self.pushButton_7)

        self.pushButton_11 = QPushButton(self.frame_7)
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
"QPushButton:hover {\n"
"    background-color: #FAD1D1;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.pushButton_11)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)


        self.horizontalLayout_5.addWidget(self.frame_7)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel#label_8{\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"    color: #2B1114; \n"
"    padding-bottom: 4px;\n"
"	background-color: none;\n"
"}")

        self.verticalLayout_10.addWidget(self.label_8)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"    background-color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    gridline-color: transparent; \n"
"    color: #1A1A1A;\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    outline: none; \n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 10px;\n"
"    border-bottom: 1px solid #EFEFEF; \n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #E0E0E0; \n"
"    color: #1A1A1A;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #FFFFFF;\n"
"    color: #1A1A1A;\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 10pt;\n"
"    border: none;\n"
"    border-bottom: 2px solid #1A1A1A; \n"
"    padding: 8px;\n"
"    text-align: left; \n"
"}\n"
"\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"    background-color: #FFFFFF;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #F5F5F5;\n"
"    width: 8px;\n"
"    margin: 0px 0px 0px 0px;\n"
""
                        "    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #C2C2C2;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #A8A8A8;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"    height: 0px;\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.tableView)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0438", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0438", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0438", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0416\u0443\u0440\u043d\u0430\u043b\u044b", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"API", None))
        self.pushButton_6.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"login", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u0430\u044f \u043a\u043e\u043f\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u043e\u043f\u0438\u0439", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 \u0434\u043b\u044f \u043a\u043e\u043f\u0438\u0439", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u043e\u043f\u0438\u044e \u0441\u0435\u0439\u0447\u0430\u0441", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0438\u0437 \u043a\u043e\u043f\u0438\u0438", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u044b\u0445 \u043a\u043e\u043f\u0438\u0439", None))
    # retranslateUi

