# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(909, 623)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(50, 70, 811, 391))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.det_image = QPushButton(self.groupBox)
        self.det_image.setObjectName(u"det_image")
        self.det_image.setGeometry(QRect(20, 150, 81, 81))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.det_image.sizePolicy().hasHeightForWidth())
        self.det_image.setSizePolicy(sizePolicy1)
        self.det_video = QPushButton(self.groupBox)
        self.det_video.setObjectName(u"det_video")
        self.det_video.setGeometry(QRect(20, 260, 81, 81))
        sizePolicy1.setHeightForWidth(self.det_video.sizePolicy().hasHeightForWidth())
        self.det_video.setSizePolicy(sizePolicy1)
        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(100, 40, 16, 300))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.input = QLabel(self.groupBox)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(110, 40, 300, 300))
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setScaledContents(True)
        self.input.setAlignment(Qt.AlignCenter)
        self.input.setWordWrap(False)
        self.output = QLabel(self.groupBox)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(440, 40, 300, 300))
        sizePolicy.setHeightForWidth(self.output.sizePolicy().hasHeightForWidth())
        self.output.setSizePolicy(sizePolicy)
        self.output.setScaledContents(True)
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setWordWrap(False)
        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(410, 40, 30, 300))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.pushButton_stop = QPushButton(self.groupBox)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setGeometry(QRect(230, 350, 75, 23))
        self.pushButton_exit = QPushButton(self.groupBox)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(570, 350, 75, 23))
        self.det_model = QPushButton(self.groupBox)
        self.det_model.setObjectName(u"det_model")
        self.det_model.setGeometry(QRect(20, 50, 81, 81))
        sizePolicy1.setHeightForWidth(self.det_model.sizePolicy().hasHeightForWidth())
        self.det_model.setSizePolicy(sizePolicy1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 20, 324, 34))
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(280, 470, 581, 121))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 20, 541, 91))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(50, 470, 211, 121))
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 171, 91))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8def\u9762\u88c2\u7f1d\u68c0\u6d4b\u7cfb\u7edf", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\u533a", None))
        self.det_image.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u68c0\u6d4b", None))
        self.det_video.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u68c0\u6d4b", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u56fe\u50cf", None))
        self.output.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c/\u7ee7\u7eed", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u68c0\u6d4b", None))
        self.det_model.setText(QCoreApplication.translate("MainWindow", u"\u8f7d\u5165\u6a21\u578b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528\u8def\u9762\u88c2\u7f1d\u68c0\u6d4b\u7cfb\u7edf", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u4fe1\u606f", None))
        self.label_2.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u4fe1\u606f", None))
        self.label_3.setText("")
    # retranslateUi

