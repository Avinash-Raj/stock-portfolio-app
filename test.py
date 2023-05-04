import sys

from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QStyledItemDelegate, QStyle
from PyQt6.QtGui import QTextDocument
from PyQt6.QtCore import QRectF, QSize

data = {'col1': ['<h1>Big Title</h1>', '<a href="https://www.stackoverflow.com">I love stackoverflow</a>', 'just normal plain text'],
        'col2': ['<p style="color:red">cool</p>', 'car', '<p>&#128512;</p>'],
        'col3': ['<p style="background-color:powderblue;">123</p>', '<b>truck</b>', '<p style="color:green">pizza</p>']}


class TableView(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setData(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)


class HTMLDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        self.initStyleOption(option,index)
        painter.save()
        doc = QTextDocument()
        doc.setHtml(option.text)
        #option.text = ''
        #option.widget.style().drawControl(QStyle.ControlElement.CE_ItemViewItem, option, painter)
        painter.translate(option.rect.left(), option.rect.top())
        clip = QRectF(0, 0, option.rect.width(), option.rect.height())
        doc.drawContents(painter, clip)
        painter.restore()


def main(args):
    app = QApplication(args)
    table = TableView(data, 3, 3)
    table.setItemDelegate(HTMLDelegate())
    table.resizeColumnsToContents()
    table.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main(sys.argv)