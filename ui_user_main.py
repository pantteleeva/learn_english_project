# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_proverka.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1065, 625)
        MainWindow.setStyleSheet(u"background-color: #FDECEC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
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
"    font-weight: bold;\n"
"    color: #9B1C1C;\n"
"    background-color: #FDECEC; \n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 6px 16px;\n"
"}\n"
"QPushButton#pushButton_2:hover {\n"
"    background-color: #FAD1D1;\n"
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton#pushButton_5 {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 10pt;\n"
"    color: #9B1C1C; \n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton#pushButton_5:hover {\n"
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


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addWidget(self.frame)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame#frame_2 {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #EBD6D8; \n"
"    border-radius: 16px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit#textEdit {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 11pt;\n"
"    color: #2B1114; \n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #EBD6D8; \n"
"    border-radius: 12px;\n"
"    padding: 12px;\n"
"}\n"
"QTextEdit#textEdit:focus {\n"
"    border: 1px solid #C62828;\n"
"}")

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_9 = QPushButton(self.frame_2)
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
"QPushButton:hover {\n"
"    background-color: #FAD1D1;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton#pushButton_7{\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-size: 11pt;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF; \n"
"    background-color: #9B1C1C; \n"
"    border: none;\n"
"    border-radius: 18px;\n"
"    padding: 10px 24px;\n"
"}\n"
"QPushButton#pushButton_7:hover {\n"
"    background-color: #A82222;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_7)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel#label_3 {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"    color: #9B1C1C; \n"
"    padding-bottom: 4px;\n"
"}")

        self.verticalLayout_2.addWidget(self.label_3)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setStyleSheet(u"QTextEdit#textEdit_2 {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #EBD6D8; \n"
"    border-radius: 16px;\n"
"    padding: 12px;\n"
"}")

        self.verticalLayout_2.addWidget(self.textEdit_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setStyleSheet(u"QLabel#label_4 {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"    color: #9B1C1C; \n"
"    padding-bottom: 4px;\n"
"}")

        self.verticalLayout_3.addWidget(self.label_4)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame#frame_3 {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #EBD6D8; \n"
"    border-radius: 16px;\n"
"}\n"
"QFrame#frame_3 QLabel {\n"
"    font-family: \"Inter\", sans-serif;\n"
"    color: #2B1114;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u0430\u044f", None))
        self.label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0440\u0430\u0436\u043d\u0435\u043d\u0438\u044f", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0435\u0441\u0441", None))
        self.pushButton_6.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"login", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043b\u0438 \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0435 \u043e\u0448\u0438\u0431\u043a\u0438:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0438\u043b\u043e:", None))
    # retranslateUi

