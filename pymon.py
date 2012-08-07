#!/usr/bin/python

import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure
from PyQt4 import QtCore, QtGui
#from PyQt4.QtCore import QObject


class GuiPyMon(object):

    def __init__(self,forwid):
        forwid.setObjectName("forma1")
        forwid.resize(292,114)
        forwid.setWindowTitle("Aplicacion pymongo y qt")
        forwid.setStyleSheet("#forma1{background:black;} QPushButton{color:black;background:white;border-width:1px;border-radius:5;font-size:12px;padding-left:5px;padding-right:5px;} QLabel{color:white}")
    
    def conn(self,forwid):
      #  conn=pymongo.Connection('mongodb://localhost:27017')
       # self.lbl2=QtGui.QLabel(forwid)
        #self.lbl2.setGeometry(0,50,150,50)
       
        """ Connect to MongoDB """
        try:
            c = Connection(host="localhost", port=27017)
            print "Connected successfully"
        except ConnectionFailure, e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)


    def nbntconn(self,forwid):

        self.pbtn = QtGui.QPushButton(forwid)
        self.pbtn.setText("Conectar")
        self.pbtn.clicked.connect(self.conn)
        #self.pbtn.clicked.connect(self.lbl(forwid,"Conexion exitosa"))
        #QtCore.QMetaObject.connectSlotsByName(forwid)
        self.pbtn.show()
    
    def lbl(self,forwid):
        self.lbl = QtGui.QLabel(forwid)
        self.lbl.setGeometry(0,50,100,50)
        self.lbl.setText("Soy una label")
        self.lbl.show()

    def refresh(self,forwid):
        self.nbntconn(forwid)
        self.lbl(forwid)
    

    
   # print conn

#Conecta a una bd
#db = conn.mydb
#db = conn['mydb']

# Agregando algunos datos
#db.things.save({"Some": "data"})

#Insertar mejor explicito
#db.things.insert({"Hello": "Florence!"})
#Buscando datos
#db.things.find()

#Retornando la primer pareja
#db.things.find_one()

#Buscando datos

#Query
app=QtGui.QApplication(sys.argv)
miforma=QtGui.QWidget()
miui=GuiPyMon(miforma)
miforma.show()
miui.refresh(miforma)
sys.exit(app.exec_())
