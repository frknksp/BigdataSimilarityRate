import sys
from PyQt5.QtWidgets import  *
from PyQt5 import uic
import getdatapand
import cleardataframe
import specquerypandas
import os


class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI,self).__init__()
        self.threadtimers = []
        self.threadcount = 1
        self.selectedcolumnname = "Product"
        self.complaint_id = ""
        uic.loadUi("mygui.ui", self)
        self.wdgsimrate.setColumnWidth(0,250)
        self.wdgsimrate.setColumnWidth(1,250)
        self.wdgsimrate.setColumnWidth(2,150)
        self.wdgAllthread.setColumnWidth(0, 60)
        self.wdgAllthread.setColumnWidth(1, 270)

        self.thcountButton.clicked.connect(self.getThreadCount)
        self.thcountButton.clicked.connect(self.loaddatathreadtime)
        self.listButton.clicked.connect(self.getColumnName)
        # self.listButton.clicked.connect(self.loaddatasimrate)
        self.listButton.clicked.connect(self.getSimRate)
        self.listCompidButton.clicked.connect(self.getCompId)


    def loaddatathreadtime(self):
        row=0
        self.wdgAllthread.setRowCount(len(self.threadtimers))
        for thread in self.threadtimers:
            self.wdgAllthread.setItem(row, 0, QTableWidgetItem(thread["thread_index"]))
            self.wdgAllthread.setItem(row, 1, QTableWidgetItem(str(thread["time"])))
            row=row+1

    def loaddatasimrate(self,sim_rate):
        resultquery = ""
        if os.path.isfile("cleardf.csv"):
            print("cleardf file exists")
        else:
            print("cleardf file not exists,creating file")
            cleardataframe.cleardf()
        if not self.complaint_id == "":
            resultquery = specquerypandas.querypanda(self.complaint_id,self.selectedcolumnname)
        result = getdatapand.fonks(int(self.threadcount),self.selectedcolumnname)
        allvaluess = result[0]
        self.threadtimers = result[1]
        showvalues = []
        self.loaddatathreadtime()
        if self.complaint_id != "":
            for i in allvaluess:
                if (i["firststr"] == resultquery or i["secondstr"] == resultquery) and i["rate"] > int(sim_rate):
                    # print(i["rate"])
                    # print(i["firststr"])
                    # print(i["secondstr"])
                    showvalues.append(i)
        else:
            for i in allvaluess:
                if i["rate"] > int(sim_rate):
                    # print(i["rate"])
                    # print(i["firststr"])
                    # print(i["secondstr"])
                    showvalues.append(i)

        row=0
        self.wdgsimrate.setRowCount(len(showvalues))
        for value in showvalues:
            self.wdgsimrate.setItem(row, 0, QTableWidgetItem(value["firststr"]))
            self.wdgsimrate.setItem(row, 1, QTableWidgetItem(value["secondstr"]))
            self.wdgsimrate.setItem(row, 2, QTableWidgetItem(str(value["rate"])))
            row=row+1



    def getThreadCount(self):
        threadsayisi = self.threadsayibox.text()
        self.threadcount = threadsayisi

    def getColumnName(self):
        column_name = self.columnnamebox.currentText()
        self.selectedcolumnname = column_name

    def getSimRate(self):
        sim_rate = self.simratebox.text()
        self.loaddatasimrate(sim_rate)

    def getCompId(self):
        compid = self.compidbox.text()
        self.complaint_id = compid
        # specquerypandas.querypanda(self.complaint_id,self.selectedcolumnname)
        print(self.complaint_id)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MyGUI()
    windows.show()
    app.exec_()

