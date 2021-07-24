from PyQt5 import QtCore, QtGui, QtWidgets
from NhanDang import NhanDang
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import pyodbc
import datetime
from PyQt5.Qt import QTableWidgetItem, QAbstractItemView
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(987, 600)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Hinh = QtWidgets.QLabel(self.centralwidget)
        self.label_Hinh.setGeometry(QtCore.QRect(10, 50, 451, 421))
        self.label_Hinh.setText("")
        self.label_Hinh.setPixmap(QtGui.QPixmap(""))
        self.label_Hinh.setScaledContents(True)
        self.label_Hinh.setObjectName("label_Hinh")
        self.groupBox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox1.setGeometry(QtCore.QRect(10, 50, 451, 421))
        self.groupBox1.setObjectName("groupBox")
        self.btnNhanDang = QtWidgets.QPushButton(self.centralwidget)
        self.btnNhanDang.setGeometry(QtCore.QRect(300, 500, 91, 41))
        self.btnNhanDang.setObjectName("btnNhanDang")

        self.btnChupAnh = QtWidgets.QPushButton(self.centralwidget)
        self.btnChupAnh.setGeometry(QtCore.QRect(200, 500, 91, 41))
        self.btnChupAnh.setObjectName("btnChupAnhDang")

        self.btnVieo = QtWidgets.QPushButton(self.centralwidget)
        self.btnVieo.setGeometry(QtCore.QRect(100, 500, 91, 41))
        self.btnVieo.setObjectName("btnVieo")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(470, 50, 511, 192))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        
        self.btnCapNhat = QtWidgets.QPushButton(self.centralwidget)
        self.btnCapNhat.setGeometry(QtCore.QRect(490, 270, 95, 23))
        self.btnCapNhat.setObjectName("btnCapNhat")
        self.btnThem = QtWidgets.QPushButton(self.centralwidget)
        self.btnThem.setGeometry(QtCore.QRect(590, 270, 75, 23))
        self.btnThem.setObjectName("btnThem")
        self.btnXoa = QtWidgets.QPushButton(self.centralwidget)
        self.btnXoa.setGeometry(QtCore.QRect(690, 270, 75, 23))
        self.btnXoa.setObjectName("btnXoa")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(490, 310, 441, 271))
        self.groupBox.setObjectName("groupBox")
        self.textEdit_BienSo = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_BienSo.setGeometry(QtCore.QRect(150, 10, 271, 41))
        self.textEdit_BienSo.setObjectName("textEdit_BienSo")
        self.textEdit_Ten = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_Ten.setGeometry(QtCore.QRect(150, 60, 271, 31))
        self.textEdit_Ten.setObjectName("textEdit_Ten")
        self.textEdit_Ngay = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_Ngay.setGeometry(QtCore.QRect(150, 100, 271, 31))
        self.textEdit_Ngay.setObjectName("textEdit_Ngay")
        self.textEdit_Gio = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_Gio.setGeometry(QtCore.QRect(150, 140, 271, 31))
        self.textEdit_Gio.setObjectName("textEdit_Gio")
        self.textEdit_LoaiXe = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_LoaiXe.setGeometry(QtCore.QRect(150, 180, 271, 31))
        self.textEdit_LoaiXe.setObjectName("textEdit_LoaiXe")
        self.lbBienSo = QtWidgets.QLabel(self.groupBox)
        self.lbBienSo.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.lbBienSo.setObjectName("lbBienSo")
        self.label_Ten = QtWidgets.QLabel(self.groupBox)
        self.label_Ten.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.label_Ten.setObjectName("label_Ten")
        self.label_Ngay = QtWidgets.QLabel(self.groupBox)
        self.label_Ngay.setGeometry(QtCore.QRect(10, 100, 101, 31))
        self.label_Ngay.setObjectName("label_Ngay")
        self.label_Gio = QtWidgets.QLabel(self.groupBox)
        self.label_Gio.setGeometry(QtCore.QRect(10, 150, 101, 21))
        self.label_Gio.setObjectName("label_Gio")
        self.label_DiaChi = QtWidgets.QLabel(self.groupBox)
        self.label_DiaChi.setGeometry(QtCore.QRect(10, 180, 101, 31))
        self.label_DiaChi.setObjectName("label_DiaChi")
        self.label_LoaiXe = QtWidgets.QLabel(self.groupBox)
        self.label_LoaiXe.setGeometry(QtCore.QRect(10, 230, 101, 31))
        self.label_LoaiXe.setObjectName("label_LoaiXe")
        self.textEdit_LoaiXe_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_LoaiXe_2.setGeometry(QtCore.QRect(150, 230, 271, 31))
        self.textEdit_LoaiXe_2.setObjectName("textEdit_LoaiXe_2")
        self.btnTimKiem = QtWidgets.QPushButton(self.centralwidget)
        self.btnTimKiem.setGeometry(QtCore.QRect(790, 270, 75, 23))
        self.btnTimKiem.setObjectName("btnTimKiem")
        self.label_TenNhom = QtWidgets.QLabel(self.centralwidget)
        self.label_TenNhom.setGeometry(QtCore.QRect(636, 10, 101, 20))
        self.label_TenNhom.setScaledContents(True)
        self.label_TenNhom.setObjectName("label_TenNhom")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnNhanDang.clicked.connect(self.nhandang)
        self.btnCapNhat.clicked.connect(self.loadData)
        self.btnThem.clicked.connect(self.updata)
        self.btnXoa.clicked.connect(self.deledata)
        self.btnTimKiem.clicked.connect(self.tim)
        self.tableWidget.clicked.connect(self.on_Click)
        self.btnChupAnh.clicked.connect(self.chupHinh1)
        self.btnVieo.clicked.connect(self.video)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnNhanDang.setText(_translate("MainWindow", "Nhan Dang"))
        self.btnChupAnh.setText(_translate("MainWindow", "Chup Anh"))
        self.btnVieo.setText(_translate("MainWindow", "Vieo"))
        self.btnCapNhat.setText(_translate("MainWindow", "Xem Danh sách"))
        self.btnThem.setText(_translate("MainWindow", "Them"))
        self.btnXoa.setText(_translate("MainWindow", "Xoa"))
        self.groupBox.setTitle(_translate("MainWindow", "Thong Tin"))
        self.groupBox1.setTitle(_translate("MainWindow", "Thong Tin Anh"))
        self.lbBienSo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Bien so :</span></p></body></html>"))
        self.label_Ten.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Ten :</span></p></body></html>"))
        self.label_Ngay.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Ngay :</span></p></body></html>"))
        self.label_Gio.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Gio :</span></p></body></html>"))
        self.label_DiaChi.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Loại Xe</span></p><p><br/></p></body></html>"))
        self.label_DiaChi.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Dia Chi :</span></p></body></html>"))
        self.label_LoaiXe.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Loại Xe</span></p><p><br/></p></body></html>"))
        self.label_LoaiXe.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Loai xe :</span></p></body></html>"))
        self.btnTimKiem.setText(_translate("MainWindow", "Tim Kiem"))
        self.label_TenNhom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Nhóm 19</span></p></body></html>"))
    def chupHinh1(self):
        a = NhanDang()
        b = a.chupHinh()
        self.label_Hinh.setPixmap(QtGui.QPixmap(r"E:\ITS-N13\Cropped Images-Text\fileXuLy.png"))
        c = a.xuly(r"E:\ITS-N13\Cropped Images-Text\fileXuLy.png")
        self.textEdit_BienSo.setText(c)
        if self.tim1() == 1:
            self.textEdit_Ten.setText("Đã Đăng Ký")
        else:   
            self.textEdit_Ten.setText("Không xác định")
            self.textEdit_LoaiXe.setText("Không xác định")
            self.textEdit_LoaiXe_2.setText("Không xác định")
        
        self.loadTime()
    def video(self):
        a = NhanDang()
        b=  a.chuongTrinhNhanDienXe()
 

    def nhandang(self):
        self.textEdit_BienSo.setText("")
        self.textEdit_Ten.setText("")
        self.textEdit_Ngay.setText("")
        self.textEdit_Gio.setText("")
        self.textEdit_LoaiXe.setText("")
        self.textEdit_LoaiXe_2.setText("")
        hinh1 = ""
        a = NhanDang()
        hinh1 = self.browserfiler()
        b = a.xuly(hinh1)
        self.textEdit_BienSo.setText(b)
        if self.tim1() == 1:
            self.textEdit_Ten.setText("Đã Đăng Ký")
        else:   
            self.textEdit_Ten.setText("Không xác định")
            self.textEdit_LoaiXe.setText("Không xác định")
            self.textEdit_LoaiXe_2.setText("Không xác định")
        
        self.loadTime()
        
    def loadTime(self):
        DateTime = datetime.datetime.now()
        self.textEdit_Ngay.setText('Date: %s/%s/%s'%(DateTime.year,DateTime.month,DateTime.day))
        self.textEdit_Gio.setText('%s Gio -%s Phut -%s Giay'%(DateTime.hour,DateTime.minute,DateTime.second))

    def loadData(self):
        SQL_STATEMENT = 'SELECT * FROM dbo.BienSo'
        SERVER_NAME = "DESKTOP-TAG6L7K\\SQLEXPRESS"
        DATABASE_NAME = "QuanLyBienSoXe"
        connString = f'DRIVER={{SQL Server}};'\
                     f'SERVER={SERVER_NAME};'\
                     f'DATABASE={DATABASE_NAME}'
        conn = pyodbc.connect(connString)
        cursor = conn.cursor()
        result = cursor.execute(SQL_STATEMENT)  
        self.tableWidget.setRowCount(0)
        for row_number, rown_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number , data in enumerate(rown_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
    def updata(self):
        SERVER_NAME = "DESKTOP-TAG6L7K\\SQLEXPRESS"
        DATABASE_NAME = "QuanLyBienSoXe"
        connString = f'DRIVER={{SQL Server}};'\
                     f'SERVER={SERVER_NAME};'\
                     f'DATABASE={DATABASE_NAME}'
        conn = pyodbc.connect(connString)
        cursor = conn.cursor()
        result = cursor.execute('INSERT INTO dbo.BienSo ( BienSo ,Ten ,Ngay ,Gio ,DiaChi ,LoaiXe) VALUES  (?,?,?,?,?,?)',
                                (self.textEdit_BienSo.toPlainText(),self.textEdit_Ten.toPlainText(),self.textEdit_Ngay.toPlainText(),self.textEdit_Gio.toPlainText(),self.textEdit_LoaiXe.toPlainText(),self.textEdit_LoaiXe_2.toPlainText())
            )
        conn.commit()
        self.loadData()

        a = NhanDang()
        b = a.luuAnh(self.textEdit_Ten.toPlainText())

    def deledata(self):
        SERVER_NAME = "DESKTOP-TAG6L7K\\SQLEXPRESS"
        DATABASE_NAME = "QuanLyBienSoXe"
        connString = f'DRIVER={{SQL Server}};'\
                     f'SERVER={SERVER_NAME};'\
                     f'DATABASE={DATABASE_NAME}'
        conn = pyodbc.connect(connString)
        cursor = conn.cursor()
        result = cursor.execute("DELETE FROM dbo.BienSo WHERE BienSo=?",(self.textEdit_BienSo.toPlainText())    )
        conn.commit()
        a = NhanDang()
        b = a.xoaAnh(self.textEdit_Ten.toPlainText())
        self.loadData()
    def tim(self):
        SERVER_NAME = "DESKTOP-TAG6L7K\\SQLEXPRESS"
        DATABASE_NAME = "QuanLyBienSoXe"
        connString = f'DRIVER={{SQL Server}};'\
                     f'SERVER={SERVER_NAME};'\
                     f'DATABASE={DATABASE_NAME}'
        conn = pyodbc.connect(connString)
        cursor = conn.cursor()
        result = cursor.execute(" SELECT * FROM dbo.BienSo WHERE BienSo=?",(self.textEdit_BienSo.toPlainText()))
        #conn.commit()
        self.tableWidget.setRowCount(0)
        for row_number, rown_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number , data in enumerate(rown_data):
                self.tableWidget.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
                #print(data)

    def tim1(self):
        SERVER_NAME = "DESKTOP-TAG6L7K\\SQLEXPRESS"
        DATABASE_NAME = "QuanLyBienSoXe"
        connString = f'DRIVER={{SQL Server}};'\
                     f'SERVER={SERVER_NAME};'\
                     f'DATABASE={DATABASE_NAME}'
        conn = pyodbc.connect(connString)
        cursor = conn.cursor()
        result = cursor.execute(" SELECT COUNT(*) FROM dbo.BienSo WHERE BienSo=?",(self.textEdit_BienSo.toPlainText()))
        #self.tableWidget.setRowCount(0)
        for row_number, rown_data in enumerate(result):
            for colum_number , data in enumerate(rown_data):
                str(data)
        return data

        

    def  on_Click(self):
        index=(self.tableWidget.selectionModel().currentIndex())
        ax = (self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows))
        #value=index.sibling(index.row(),index.column()).data()
        indexes = self.tableWidget.selectionModel().selectedRows()
        for index1 in sorted(indexes):
            #print('Row %d is selected' % index1.row())
            #print(index1.sibling(index1.row(),0).data())
            self.textEdit_BienSo.setText(index1.sibling(index1.row(),0).data())
            self.textEdit_Ten.setText(index1.sibling(index1.row(),1).data())
            self.textEdit_Ngay.setText(index1.sibling(index1.row(),2).data())
            self.textEdit_Gio.setText(index1.sibling(index1.row(),3).data())
            self.textEdit_LoaiXe.setText(index1.sibling(index1.row(),4).data())
            self.textEdit_LoaiXe_2.setText(index1.sibling(index1.row(),5).data())
            

            
        
        #print(value)
    def browserfiler(self):
        file_name,_ = QFileDialog.getOpenFileName(None,"Open Image File",r"Car Images")
        #file_name,_ = QFileDialog.getOpenFileName(None,"Open Image File",r"E:\ITS-N13\Car Images")
        self.label_Hinh.setPixmap(QtGui.QPixmap(file_name))
        return file_name


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

