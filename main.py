import requests
from bs4 import BeautifulSoup
import lxml
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets

root = 'http://www.gsmarena.com/'

class Ui_PythonScraper(object):
    def setupUi(self, PythonScraper):
        PythonScraper.setObjectName("PythonScraper")
        PythonScraper.resize(879, 624)
        self.groupBox = QtWidgets.QGroupBox(PythonScraper)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 851, 91))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 161, 21))
        self.label.setObjectName("label")
        self.btnScrap = QtWidgets.QPushButton(self.groupBox)
        self.btnScrap.setGeometry(QtCore.QRect(470, 40, 191, 28))
        self.btnScrap.setObjectName("btnScrap")
        self.cmbPhones = QtWidgets.QComboBox(self.groupBox)
        self.cmbPhones.setGeometry(QtCore.QRect(230, 40, 161, 22))
        self.cmbPhones.setObjectName("cmbPhones")
        self.cmbPhones.addItem("")
        self.cmbPhones.addItem("")
        self.cmbPhones.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(PythonScraper)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 100, 861, 521))
        self.groupBox_2.setObjectName("groupBox_2")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(9, 16, 841, 501))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 839, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.txtResult = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.txtResult.setGeometry(QtCore.QRect(3, 6, 831, 481))
        self.txtResult.setObjectName("txtResult")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.retranslateUi(PythonScraper)
        QtCore.QMetaObject.connectSlotsByName(PythonScraper)



    def retranslateUi(self, PythonScraper):
        _translate = QtCore.QCoreApplication.translate
        PythonScraper.setWindowTitle(
            _translate("PythonScraper", "Python Scraper"))
        self.groupBox.setTitle(_translate("PythonScraper", "URL to Scrap"))
        self.label.setText(_translate(
            "PythonScraper", "http://www.gsmarena.com/"))
        self.btnScrap.setText(_translate("PythonScraper", "Scarp"))
        self.cmbPhones.setItemText(0, _translate("PythonScraper", "IPhones"))
        self.cmbPhones.setItemText(
            1, _translate("PythonScraper", "Sony Mobiles"))
        self.cmbPhones.setItemText(2, _translate(
            "PythonScraper", "Samsung Mobiles"))
        self.groupBox_2.setTitle(_translate("PythonScraper", "Result"))



# pyuic5 -x gui.ui -o main.py
#============== Scraper Function ==================

def scrap(ui):
    temp = str(ui.cmbPhones.currentText())
    url = ""
    if temp == "IPhones":
        url = "apple-phones-48.php"
    elif temp == "Sony Mobiles":
        url = "sony-phones-7.php"
    elif temp == "Samsung Mobiles":
        url = "samsung-phones-9.php"

    r = requests.get(root + url)
    soup = BeautifulSoup(r.content, 'lxml')
    li_list = soup.find('div', id='review-body').find('ul').find_all('li')
    ui.txtResult.setText('Number of peoducts: {}'.format(len(li_list)))
    for li in li_list:
        a = li.find('a')
        product_name = a.get_text()
        product_url = root + a['href']
        image = a.find('img')
        product_image_url = image['src']
        ui.txtResult.append('\nproduct name: {}'.format(product_name))
        ui.txtResult.append('Phone page url: {}'.format(product_url))
        ui.txtResult.append('Image url: {}'.format(product_image_url))

#============== Main ==================

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PythonScraper = QtWidgets.QDialog()
    ui = Ui_PythonScraper()
    ui.setupUi(PythonScraper)
    PythonScraper.show()

    ui.btnScrap.clicked.connect(partial(scrap,ui))

    sys.exit(app.exec_())