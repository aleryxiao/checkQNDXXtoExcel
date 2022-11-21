import pandas as pd
import re
import os
import time

from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog
from gui import Ui_MainWindow

# 注意 这里选择的父类 要和你UI文件窗体一样的类型
# 主窗口是 QMainWindow， 表单是 QWidget， 对话框是 QDialog
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.iB.clicked.connect(self.input)
        self.ui.oB.clicked.connect(self.output)
        self.ui.rB.clicked.connect(self.calc)

        self.iFilePath=[]
        self.oFilePath=""
        self.className="F2103302"
        self.ui.cT.setText(self.className)

    def input(self):
        self.iFilePath=QFileDialog.getOpenFileNames(caption="选择输入文件（可多选）",filter="表格文件(*.xlsx;*.xls)")[0]  # 起始目录
        self.ui.iT.setText((self.iFilePath[0])[:self.iFilePath[0].rfind('/')]) #第一个文件所在的文件夹

    def output(self):
        self.oFilePath=QFileDialog.getOpenFileName(caption="选择输出文件",filter="表格文件(*.xlsx;*.xls)")[0]  # 起始目录
        self.ui.oT.setText(self.oFilePath)

    def calc(self):
        if self.iFilePath and self.oFilePath:
            self.ui.rT.setText("Running...")
            self.className=self.ui.cT.text()
            try:
                self.ui.rT.setText("Start Processing Files")
                self.processFile()
            except Exception as E:
                self.ui.rT.setText("Run Error")
        else:
            self.ui.rT.setText("Not Ready To Run")

    def processFile(self):
        i = 0
        aStart=time.time()
        for filepath in self.iFilePath:
            i += 1
            start = time.time()
            doneList = []  # 完成名单
            rowList = []  # 需要导入列表的数字
            rd = pd.read_excel(filepath, sheet_name="原始数据",usecols=["团支部", "姓名/学号"])
            data = rd.values
            for info in data:
                if info[0] == self.className:
                    # print(info[1])
                    x = re.sub('[0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~\s]+', "", info[1])
                    # print(x)
                    if x:
                        doneList.append(x)
            # print(doneList)

            rd = pd.read_excel(self.oFilePath,usecols=["姓名"])  # 获取姓名列
            NameList = rd["姓名"].tolist()
            # print(NameList)
            for name in NameList:
                if name in doneList:
                    rowList.append(1)
                else:
                    rowList.append(0)
            # print(rowList)

            writeData(self.oFilePath, rowList, ctimeYMD(filepath))
            self.ui.rT.setText(f"表格{i}处理完毕，用时{time.time()-start}秒")
        
        self.ui.rT.setText(f"{i}个文件已经处理完毕，用时{time.time()-aStart}秒")

def ctimeYMD(file):
    from datetime import datetime
    date_of_created = datetime.strptime(time.ctime(os.path.getctime(
        file)), "%a %b %d %H:%M:%S %Y")  # Convert string to date format
    return ("{}.{}.{}".format(str(date_of_created.year)[2:], str(date_of_created.month), str(date_of_created.day)))

def writeData(file, result, name):
    op = pd.read_excel(file)
    # print(result)
    times = 0
    n = name
    while True:
        try:
            op.insert(3, n, result)  # 1表示插入列的位置（索引）， 'd'是列标题
            break
        except Exception as E:
            times += 1
            n = name + '('+str(times)+')'
    op.style.applymap(lambda x: 'background-color:yellow' if x ==
                      0 else "background-color:white").to_excel(file, index=False)


app = QApplication([])
mainw = MainWindow()
mainw.show()
app.exec()


