import sys 
from PyQt5 import uic
import requests
from PyQt5.QtWidgets import QLabel, QMainWindow, QLineEdit, QTextEdit, QPushButton, QApplication 

class pythonprogram(QMainWindow):

    def __init__(self):
        super(pythonprogram, self).__init__()
        uic.loadUi('untitled.ui', self)

        self.lineedit = self.findChild(QLineEdit, 'lineEdit')
        self.textedit = self.findChild(QTextEdit, 'textEdit')
        self.pushbutton = self.findChild(QPushButton, 'pushButton')

        self.pushbutton.clicked.connect(self.Search)
        self.show()

    def Search(self):
        a = self.lineedit.text()
        url = 'https://google.com/search?q=REPLACE&client=firefox-b-1-e'
        url = url.replace('REPLACE', a)
        curpos = 0
        data = 'url?q='
        endpos = '&amp'
        b = ''
        # page = requests.get(url)
        # if page.status_code != 200:
        #     print("Error grabbing page")
        #     return 
        # else:
        #     dat = page.text 
        #     links = dat.split(data)
        #     linksfound = []
        #     for x in links:
        #         link = x.split(endpos)[0]
        #         if link.startswith('https'):
        #             linksfound.append(link)
            
        #     strlinks = ""
        #     for x in linksfound:
        #         strlinks += x + '\n'
            
        #     self.textedit.setPlainText(strlinks)
        linksfound = []
        strout = ''
        while curpos <= 200:
            
            if curpos == 0:
                req = requests.get(url)

                data = req.text 
                links = data.split('url?q=')
                for x in links:
                    link = x.split('&amp')[0]
                    if link.startswith('https') and not link.startswith('https://accounts') and not link.startswith('https://support'):
                        print(link)
                        txt = self.textedit.toPlainText()
                        txt = txt + link + '\n'
                        self.textedit.setPlainText(txt)
                    
            if curpos > 0:
                url2 = url + '&start=' + str(curpos)
                req = requests.get(url2)

                data = req.text 
                links = data.split('url?q=')
                for x in links:
                    link = x.split('&amp')[0]
                    if link.startswith('https') and not link.startswith('https://support') and not link.startswith('https://accounts'):
                        print(link)
                        txt = self.textedit.toPlainText()
                        txt += link + '\n'
                        self.textedit.setPlainText(txt)


            curpos += 10

app = QApplication(sys.argv)
UIWindow = pythonprogram()
app.exec_()
