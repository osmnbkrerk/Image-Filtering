import cv2 as cv
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1085, 767)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dosyaSecBtn = QPushButton(self.centralwidget)
        self.dosyaSecBtn.setObjectName(u"dosyaSecBtn")
        self.dosyaSecBtn.setGeometry(QRect(560, 20, 101, 31))
        self.dosyaSecBtn.clicked.connect(self.butonEventHandler)

        self.dosyaYolu = QLabel(self.centralwidget)
        self.dosyaYolu.setObjectName(u"dosyaYolu")
        self.dosyaYolu.setGeometry(QRect(40, 20, 511, 31))
        font = QFont()
        font.setBold(False)
        self.dosyaYolu.setFont(font)
        self.dosyaYolu.setAutoFillBackground(False)
        self.resim = QLabel(self.centralwidget)
        self.resim.setObjectName(u"resim")
        self.resim.setGeometry(QRect(40, 150, 991, 561))
        self.resim.setScaledContents(True)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(40, 80, 251, 31))
        self.horizontalScrollBar = QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setGeometry(QRect(530, 80, 521, 21))
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)
        self.horizontalScrollBar.setValue(3)

        self.kernelLabel = QLabel(self.centralwidget)
        self.kernelLabel.setObjectName(u"kernelLabel")
        self.kernelLabel.setGeometry(QRect(540, 110, 81, 31))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(620, 110, 131, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 80, 101, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.horizontalScrollBar.valueChanged.connect(self.scrollEvent)


        QMetaObject.connectSlotsByName(MainWindow)


    # setupUi

    def scrollEvent(self):
        yOffset = self.horizontalScrollBar.value()
        self.plainTextEdit.setPlainText(str(yOffset)+","+str(yOffset))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.dosyaSecBtn.setText(QCoreApplication.translate("MainWindow", u"Dosya Se\u00e7", None))
        self.dosyaYolu.setText(QCoreApplication.translate("MainWindow", u"Dosya se\u00e7iniz.", None))
        self.resim.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Filtreleme Y\u00f6ntemi Se\u00e7iniz",
                                                                None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Averaging Blur", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Gaussian Blur", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Median Blur", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Bilateral Blur", None))

        self.kernelLabel.setText(QCoreApplication.translate("MainWindow", u"Kernel Boyutu : ", None))
        self.plainTextEdit.setPlainText("3,3")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Resmi G\u00f6ster", None))
        self.pushButton.clicked.connect(self.fonk)

    def fonk(self):
        yol = str(self.dosyaYolu.text())
        img = cv.imread(yol)
        k1, k2 = self.plainTextEdit.toPlainText().split(",")

        if self.comboBox.currentText() == "Averaging Blur":
            average = cv.blur(img, (int(k1), int(k2)))
            cv.imwrite(yol+"_Averaging",average)
            self.plainTextEdit.setPlainText(str(k1)+","+str(k2))
            pixmap = QPixmap(yol+"_Averaging")
            self.resim.setPixmap(pixmap)
            self.resim.resize(pixmap.width(), pixmap.height())

        elif self.comboBox.currentText() == "Gaussian Blur":
            gauss = cv.GaussianBlur(img, (int(k1), int(k2)), 0)
            cv.imwrite(yol+"_Gaussian",gauss)
            self.plainTextEdit.setPlainText(str(k1)+","+str(k2))
            pixmap = QPixmap(yol+"_Gaussian")
            self.resim.setPixmap(pixmap)
            self.resim.resize(pixmap.width(), pixmap.height())

        elif self.comboBox.currentText() == "Median Blur":
            median = cv.medianBlur(img, int(k1))
            cv.imwrite(yol+"_Median",median)
            self.plainTextEdit.setPlainText(str(k1)+","+str(k2))
            pixmap = QPixmap(yol+"_Median")
            self.resim.setPixmap(pixmap)
            self.resim.resize(pixmap.width(), pixmap.height())

        elif self.comboBox.currentText() == "Bilateral Blur":
            bilateral = cv.bilateralFilter(img, 10, 35, 25)
            cv.imwrite(yol+"_Bilateral",bilateral)
            self.plainTextEdit.setPlainText(str(k1)+","+str(k2))
            pixmap = QPixmap(yol+"_Bilateral")
            self.resim.setPixmap(pixmap)
            self.resim.resize(pixmap.width(), pixmap.height())

        else:
            pass

    def butonEventHandler(self):
        print("Butona basıldı...")
        self.dialogKutusuAc()

    def dialogKutusuAc(self):
        dosyaAd = QFileDialog.getOpenFileName()
        yol = dosyaAd[0]
        self.dosyaYolu.setText(str(yol))



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
