# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QFrame,
    QGridLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
import rc_moviolaPod
from functools import partial

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.podFrame = QFrame(self.centralwidget)
        self.setGroupStyles(self.podFrame)

        self.podFrame.setObjectName(u"podFrame")
        self.podFrame.setFrameShape(QFrame.StyledPanel)
        self.podFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.podFrame)
        self.gridLayout.setObjectName(u"gridLayout")

        icon = QIcon()
        icon.addFile(u":/newPrefix/moviola_red.png", QSize(), QIcon.Normal, QIcon.Off)

        self.podButton_9 = QPushButton(self.podFrame)
        self.podButton_9.setObjectName(u"podButton_9")
        self.podButton_9.setEnabled(False)
        self.podButton_9.setIcon(icon)
        self.setButtonStyles(self.podButton_9)

        self.gridLayout.addWidget(self.podButton_9, 3, 2, 1, 1)

        self.podButton_4 = QPushButton(self.podFrame)
        self.podButton_4.setObjectName(u"podButton_4")
        self.podButton_4.setEnabled(False)
        self.podButton_4.setIcon(icon)
        self.setButtonStyles(self.podButton_4)

        self.gridLayout.addWidget(self.podButton_4, 2, 0, 1, 1)

        self.podButton_3 = QPushButton(self.podFrame)
        self.podButton_3.setObjectName(u"podButton_3")
        self.podButton_3.setEnabled(False)
        self.podButton_3.setIcon(icon)
        self.setButtonStyles(self.podButton_3)

        self.gridLayout.addWidget(self.podButton_3, 1, 2, 1, 1)

        self.podButton_6 = QPushButton(self.podFrame)
        self.podButton_6.setObjectName(u"podButton_6")
        self.podButton_6.setEnabled(False)
        self.podButton_6.setIcon(icon)
        self.setButtonStyles(self.podButton_6)

        self.gridLayout.addWidget(self.podButton_6, 2, 2, 1, 1)

        self.podButton_7 = QPushButton(self.podFrame)
        self.podButton_7.setObjectName(u"podButton_7")
        self.podButton_7.setEnabled(False)
        self.podButton_7.setIcon(icon)
        self.setButtonStyles(self.podButton_7)

        self.gridLayout.addWidget(self.podButton_7, 3, 0, 1, 1)

        self.podButton_1 = QPushButton(self.podFrame)
        self.podButton_1.setObjectName(u"podButton_1")
        self.podButton_1.setEnabled(False)
        self.podButton_1.setIcon(icon)
        self.setButtonStyles(self.podButton_1)

        self.gridLayout.addWidget(self.podButton_1, 1, 0, 1, 1)

        self.scanButton = QPushButton(self.podFrame)
        self.scanButton.setObjectName(u"scanButton")

        self.gridLayout.addWidget(self.scanButton, 0, 0, 1, 1)

        self.podButton_5 = QPushButton(self.podFrame)
        self.podButton_5.setObjectName(u"podButton_5")
        self.podButton_5.setEnabled(False)
        self.podButton_5.setIcon(icon)
        self.setButtonStyles(self.podButton_5)

        self.gridLayout.addWidget(self.podButton_5, 2, 1, 1, 1)

        self.podButton_2 = QPushButton(self.podFrame)
        self.podButton_2.setObjectName(u"podButton_2")
        self.podButton_2.setEnabled(False)
        self.podButton_2.setIcon(icon)
        self.setButtonStyles(self.podButton_2)

        self.gridLayout.addWidget(self.podButton_2, 1, 1, 1, 1)

        self.podButton_8 = QPushButton(self.podFrame)
        self.podButton_8.setObjectName(u"podButton_8")
        self.podButton_8.setEnabled(False)
        self.podButton_8.setIcon(icon)
        self.setButtonStyles(self.podButton_8)

        self.gridLayout.addWidget(self.podButton_8, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.podFrame)

        self.detailFrame = QFrame(self.centralwidget)
        self.detailFrame.setObjectName(u"detailFrame")
        self.detailFrame.setFrameShape(QFrame.StyledPanel)
        self.detailFrame.setFrameShadow(QFrame.Raised)
        self.detailFrame.setLineWidth(1)
        self.detailFrame.setEnabled(False)

        self.gridLayout_2 = QGridLayout(self.detailFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.infoEdit = QLineEdit(self.detailFrame)
        self.infoEdit.setObjectName(u"infoEdit")

        self.gridLayout_2.addWidget(self.infoEdit, 2, 1, 1, 1)

        self.nameEdit = QLineEdit(self.detailFrame)
        self.nameEdit.setObjectName(u"nameEdit")

        self.gridLayout_2.addWidget(self.nameEdit, 1, 1, 1, 1)

        self.nameLabel = QLabel(self.detailFrame)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.nameLabel, 1, 0, 1, 1)

        self.selectionLabel = QLabel(self.detailFrame)
        self.selectionLabel.setObjectName(u"selectionLabel")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.selectionLabel.setFont(font)
        self.selectionLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.selectionLabel, 0, 0, 1, 2)

        self.infoLabel = QLabel(self.detailFrame)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.infoLabel, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.detailFrame)

        self.buttonBox = QDialogButtonBox(self.centralwidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)

        MainWindow.setCentralWidget(self.centralwidget)


        QWidget.setTabOrder(self.scanButton, self.nameEdit)
        QWidget.setTabOrder(self.nameEdit, self.infoEdit)
        QWidget.setTabOrder(self.infoEdit, self.podButton_1)
        QWidget.setTabOrder(self.podButton_1, self.podButton_2)
        QWidget.setTabOrder(self.podButton_2, self.podButton_3)
        QWidget.setTabOrder(self.podButton_3, self.podButton_4)
        QWidget.setTabOrder(self.podButton_4, self.podButton_5)
        QWidget.setTabOrder(self.podButton_5, self.podButton_6)
        QWidget.setTabOrder(self.podButton_6, self.podButton_7)
        QWidget.setTabOrder(self.podButton_7, self.podButton_8)
        QWidget.setTabOrder(self.podButton_8, self.podButton_9)

        self.retranslateUi(MainWindow)
        self.scanButton.clicked.connect(MainWindow.startScanClicked)
        self.nameEdit.editingFinished.connect(MainWindow.clientNameEdited)
        self.infoEdit.editingFinished.connect(MainWindow.clientInfoEdited)
        self.buttonBox.accepted.connect(MainWindow.acceptClicked)
        self.buttonBox.rejected.connect(MainWindow.cancelClicked)

        for i in range(1, 10):  # Adjust the range depending on your podButton count
            button = getattr(self, f'podButton_{i}', None)
            if button:
                button.clicked.connect(partial(MainWindow.podClicked, button))

        QMetaObject.connectSlotsByName(MainWindow)

    def setButtonStyles(self, button):
        button.setStyleSheet(
            """
            QPushButton { /* Normal State */
                background-color: #333;
                color: white;
                border: 1px solid #555;
                border-radius: 3px; /* add this line */
            }
            QPushButton:hover { /* Hover State */
                background-color: #555;
                color: white;
                border: 2px solid #777;
                border-radius: 3px; /* add this line */
            }
            QPushButton:pressed { /* Pressed State */
                background-color: #777;
                color: white;
                border: 1px solid #999;
                border-radius: 3px; /* add this line */
            }
            QPushButton:disabled { /* Disabled State */
                background-color: #fff;
                color: #ccc;
                border: 1px solid #999;
                border-radius: 3px; /* add this line */
            }
            """
        )

    def setGroupStyles(self, group):
        group.setStyleSheet(
            """
            QFrame { /* Normal State */
                border: 1px solid #555;
                border-radius: 3px; /* add this line */
            }
            """
        )

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Moviola Pod Sign Editor", None))
        self.podButton_9.setText(QCoreApplication.translate("MainWindow", u"POD-9", None))
        self.podButton_4.setText(QCoreApplication.translate("MainWindow", u"POD-4", None))
        self.podButton_3.setText(QCoreApplication.translate("MainWindow", u"POD-3", None))
        self.podButton_6.setText(QCoreApplication.translate("MainWindow", u"POD-6", None))
        self.podButton_7.setText(QCoreApplication.translate("MainWindow", u"POD-7", None))
        self.podButton_1.setText(QCoreApplication.translate("MainWindow", u"POD-1", None))
        self.scanButton.setText(QCoreApplication.translate("MainWindow", u"START SCAN", None))
        self.podButton_5.setText(QCoreApplication.translate("MainWindow", u"POD-5", None))
        self.podButton_2.setText(QCoreApplication.translate("MainWindow", u"POD-2", None))
        self.podButton_8.setText(QCoreApplication.translate("MainWindow", u"POD-8", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"CLIENT NAME:", None))
        self.selectionLabel.setText(QCoreApplication.translate("MainWindow", u"PRESS SCAN FOR AVAILABLE PODS", None))
        self.infoLabel.setText(QCoreApplication.translate("MainWindow", u"INFO:", None))
    # retranslateUi

