# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YT.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from ast import Global
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QFileDialog 
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(430, 270)
        MainWindow.setMinimumSize(QtCore.QSize(430, 270))
        MainWindow.setMaximumSize(QtCore.QSize(430, 270))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("direct-download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(38, 38, 38); \n"
"color:white; \n"
"font: 14pt \"Kdam Thmor Pro, sans-serif\";\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setStyleSheet("margin-left:3px;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignLeft)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_2.setStyleSheet("QLineEdit{ \n"
"margin-left:35px ;\n"
"padding:2px; \n"
"border:2px solid white; \n"
"border-radius:5px;\n"
"} \n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_6.addWidget(self.lineEdit_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_3.setStyleSheet("QPushButton{  \n"
"padding:5px; \n"
"border:2px solid white; \n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{  \n"
"background-color: rgb(255, 255, 255); \n"
"color:black; \n"
"\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setStyleSheet("QLineEdit{ \n"
"border:2px solid white; \n"
"border-radius:5px; \n"
"padding:3px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{  \n"
"padding:5px; \n"
"border:2px solid white; \n"
"border-radius:8px;\n"
"}\n"
"QPushButton:hover{  \n"
"background-color: rgb(255, 255, 255); \n"
"color:black; \n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_5)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.verticalLayout_2.addWidget(self.frame_5, 0, QtCore.Qt.AlignLeft)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.frame_4)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("QComboBox{  \n"
"border:2px solid white; \n"
"border-radius:6px; \n"
"padding:2px;\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 6, 0)
        self.horizontalLayout_5.setSpacing(8)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.file_size_l = QtWidgets.QLabel(self.frame_6)
        self.file_size_l.setObjectName("file_size_l")
        self.horizontalLayout_5.addWidget(self.file_size_l)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setObjectName("label_4") 
        self.lineEdit_2.setPlaceholderText("Enter URL")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid rgb(38,38,38);\n"
"    border-radius: 6px; \n"
"    height:3px; \n"
"text-align:right; \n"
"margin-right:43px;\n"
"} \n"
"QProgressBar::chunk {\n"
"    background-color:rgb(255, 61, 103); \n"
"    border:8px solid rgb(38,38,38);\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{  \n"
"padding:5px; \n"
"border:2px solid white; \n"
"border-radius:8px; \n"
"}\n"
"QPushButton:hover{  \n"
"background-color: rgb(255, 255, 255); \n"
"color:black; \n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)  
        self.pushButton_3.clicked.connect(self.process)
        self.lineEdit.setText(os.getcwd())
        self.radioButton_2.clicked.connect(self.update) 
        self.radioButton.clicked.connect(self.update) 
        self.pushButton.clicked.connect(self.download) 
        self.pushButton_2.clicked.connect(self.browse)
    global d_o;d_o=dict();global d_t;d_t=dict();global Itag;Itag=0
    def size(self):  
        cur_size=self.comboBox.currentText()
        self.progressBar.setValue(0) 
        self.label_2.setStyleSheet("color:white")
        if cur_size in d_o: 
                self.label_4.setText(str(d_o[cur_size][1])+" MB") 
        else: 
                self.label_4.setText(str(d_t[cur_size][1])+" MB")     
    def download(self): 
            ask_data=self.comboBox.currentText()  
            self.label_2.setStyleSheet("color:white") 
            yt=self.search()[0];flag=self.search()[1] 
            if flag:
                if ask_data in d_o: 
                        Itag=d_o[ask_data][0]  
                        file=yt.streams.get_by_itag(Itag)
                else: 
                        Itag=d_t[ask_data][0]
                        file=yt.streams.get_by_itag(Itag)
                file.download(self.lineEdit.text().strip()) 
    # check for audio or video content
    def update(self): 
            self.progressBar.setValue(0)
            if self.radioButton.isChecked(): 
                    self.comboBox.clear()
                    for i in d_o: 
                            self.comboBox.addItem(i)
                    self.comboBox.activated.connect(self.size) 
                    self.size()
            if self.radioButton_2.isChecked(): 
                    self.comboBox.clear() 
                    for i in d_t: 
                            self.comboBox.addItem(i) 
                    self.comboBox.activated.connect(self.size) 
                    self.size()  
    # for file browser
    def browse(self): 
            fname=QFileDialog.getExistingDirectory(None, 'Select Folder', os.getcwd())
            self.lineEdit.setText(fname)
    def ERROR(self): 
            self.lineEdit_2.setText("ERROR") 
            self.lineEdit_2.setStyleSheet("color:red") 
            self.comboBox.clear() 
            self.label_4.setText("0 MB") 
            self.progressBar.setValue(0)
    def process(self): 
        yt=self.search()[0];flag=self.search()[1]  
        try:
                if flag: 
                        # for videos
                        V_data=yt.streams.filter(progressive=1) 
                        for i in V_data: 
                                self.comboBox.addItem(i.resolution) 
                                d_o[i.resolution]=(i.itag,round(i.filesize/1024.0**2,2)) 
                        # for audios
                        A_data=yt.streams.filter(only_audio=1) 
                        for i in A_data: 
                                self.comboBox.addItem(i.abr) 
                                d_t[i.abr]=(i.itag,round(i.filesize/1024.0**2,2)) 
                        self.update()
                else:  
                        # does nothing
                        pass
        except: 
                self.ERROR()
    # return remaining filesize in bytes
    def prog(self,stream,chunk,bytes_remaining): 
            pro=round(100-bytes_remaining/stream.filesize*100,2) 
            self.progressBar.setValue(round(pro))  
    # call after file  downloaded
    def complete(self,stream,filepath):
            d_t={};d_o={} 
            self.label_2.setStyleSheet("color:#28a745")

    def search(self): 
            l_url=self.lineEdit_2.text().strip()  
            from pytube import YouTube
            if l_url!="": 
                try:
                        yt = YouTube(l_url,on_progress_callback=self.prog,on_complete_callback=self.complete) 
                        self.label_2.setText(yt.title) 
                        self.label_2.setStyleSheet("color:white")
                        return yt,1

                except:  
                        #  url process error
                        yt={0,0}
                        self.label_2.setText("Not Found")
                        self.label_2.setStyleSheet("color:#dc3545")
                        return yt,0
            else: 
                yt={} 
                self.label_2.setText("URL Required") 
                self.label_2.setStyleSheet("color:#ffc107")
                self.comboBox.clear() 
                self.label_4.setText("0 MB")
                return yt,0
                 

                   
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YT Downloader"))
        self.label.setText(_translate("MainWindow", "File Name"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "URL"))
        self.pushButton_3.setText(_translate("MainWindow", "Search"))
        self.label_3.setText(_translate("MainWindow", "Location"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.radioButton.setText(_translate("MainWindow", "Video"))
        self.radioButton_2.setText(_translate("MainWindow", "Audio"))
        self.file_size_l.setText(_translate("MainWindow", "Size -"))
        self.label_4.setText(_translate("MainWindow", "0 MB"))
        self.pushButton.setText(_translate("MainWindow", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
