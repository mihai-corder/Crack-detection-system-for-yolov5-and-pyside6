# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(947, 907)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 851, 651))
        self.Imglabel = QLabel(self.groupBox)
        self.Imglabel.setObjectName(u"Imglabel")
        self.Imglabel.setGeometry(QRect(30, 50, 781, 571))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 710, 821, 151))
        self.Infolabel = QLabel(self.groupBox_2)
        self.Infolabel.setObjectName(u"Infolabel")
        self.Infolabel.setGeometry(QRect(20, 40, 681, 61))
        self.OpenVideoBtn = QPushButton(self.centralwidget)
        self.OpenVideoBtn.setObjectName(u"OpenVideoBtn")
        self.OpenVideoBtn.setGeometry(QRect(20, 680, 201, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 947, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Flower Classifier", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u7a97\u53e3", None))
        self.Imglabel.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u663e\u793a\u7a97\u53e3", None))
        self.Infolabel.setText("")
        self.OpenVideoBtn.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u89c6\u9891", None))
    # retranslateUi

