# translate.py
#!/usr/bin/python
# -*- coding: utf-8 -*-

from googletrans import Translator
import fitz
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFParser, PDFDocument
import sys
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication
from matplotlib.style import context
from yaml import parse
from app import Ui_Form
import importlib
from fpdf import FPDF


importlib.reload(sys)


#

#


# 初始化

translator = Translator(service_urls=['translate.google.cn'])
# 处理PDF
# 读取PDF的内容 filename是待处理的PDF的名字


class MyUi(QWidget, Ui_Form):
    def __init__(self):
        super(MyUi, self).__init__()  # 分别调用了2个父类的初始化函数
        self.setupUi(self)  # UI界面控件的初始化
        self.signal_connect()  # 信号与槽函数绑定

    def signal_connect(self):
        self.bnt_add_file.clicked.connect(self.bnt_add_file_slot)
        self.bnt_delete_file.clicked.connect(self.bnt_delete_file_slot)
        self.bnt_translate.clicked.connect(self.bnt_translate_slot)

    def bnt_add_file_slot(self):
        fnames, _ = QFileDialog.getOpenFileNames(
            self, '选择文件', "./", "Files(*.pdf *.txt)")
        """
                 参数一：设置父组件
                 参数二：QFileDialog的标题
                 参数三：默认打开的目录，“.”点表示程序运行目录，/表示当前盘符根目录
                 参数四：对话框的文件扩展名过滤器Filter，比如使用 Image files(*.jpg *.gif) 表示只能显示扩展名为.jpg或者.gif文件
                 设置多个文件扩展名过滤，使用双引号隔开；
                 “All Files(*);;PDF Files(*.pdf);;Text Files(*.txt)”
        """
        try:
            if fnames:
                # 如果列表非空，则添加到文件列表中去
                for f in fnames:
                    self.files_listWidget.addItem(f)

        except Exception as ex:
            print(ex)

    def bnt_translate_slot(self):
        Directory = QFileDialog.getExistingDirectory(self, '结果保存到目录', './')
        num = self.files_listWidget.count()
        # 遍历翻译所有文件
        print("# 遍历翻译所有文件")
        for _ in range(num):
            filename = self.files_listWidget.item(0).text()
            if filename.find('pdf') >= 3:
                content = self.getDataFromPDF(filename)
            elif filename.find('txt') >= 3:
                content = self.getDataFromTxt(filename)
            else:
                content = ""
                print("读取文件失败")
                return
            print("读取文件成功")

            f = filename.split('/')
            CNtextfile = Directory + '/CN_' + f[-1]
            chinese = ""
            # 遍历翻译所有句子
            print("# 遍历翻译所有句子")
            parse = fitz.open(filename)
            try:
                for page in parse:
                    t = page.getText()
                    chinese += (self.translate(t))
                self.saveText(chinese, CNtextfile)
                # self.savePdf(chinese, CNtextfile)
                print("翻译结束，ok")
                self.files_listWidget.takeItem(0)
                print("删除文件")
            except Exception as ex:
                print(ex)

    def bnt_delete_file_slot(self):
        num = self.files_listWidget.currentRow()
        self.files_listWidget.takeItem(num)
        print("删除文件")
    # 使用fitz读取

    def getDataFromPDF(self, filename):
        try:
            parse = fitz.open(filename)
            context = ''
            for page in parse:
                t = page.getText()
                context += t
            return context
        except Exception as ex:
            print(ex)

    def getDataFromTxt(self, filename):
        try:
            with open(filename, "r", encoding='utf-8') as f:
                text = f.read()
                print(text)
                content = text.replace("\n", "")  # 去掉换行符 因为排版问题 有的换行导致句子中断
                f.close()
                return content
        except Exception as ex:
            print(ex)
    # 将读取的content以txt格式存放到本地

    def saveText(self, content, Textfile):
        with open(Textfile, "w", encoding='utf-8') as f:
            f.write(content)

    def savePdf(self, content,Textfile):
        # 创建一个pdf文档分析器
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(40,10,'Hello World!')
        pdf.output(Textfile, 'F')

    # 翻译从pdf提取的content

    def translate(self, content):
        try:
            translation = translator.translate(content, dest='zh-cn')
            return translation.text
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    try:
        # 实例化一个应用对象，sys.argv是一组命令行参数的列表。Python可以在shell里运行，这是一种通过参数来选择启动脚本的方式。
        app = QApplication(sys.argv)
        myshow = MyUi()
        myshow.show()
        sys.exit(app.exec_())  # 确保主循环安全退出
    except Exception as ex:
        print(ex)
