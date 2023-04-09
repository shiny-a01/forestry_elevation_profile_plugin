# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogIorxco.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.select_points_button = QPushButton(Dialog)
        self.select_points_button.setObjectName(u"select_points_button")
        self.select_points_button.setGeometry(QRect(10, 10, 161, 23))
        self.calculate_button = QPushButton(Dialog)
        self.calculate_button.setObjectName(u"calculate_button")
        self.calculate_button.setGeometry(QRect(10, 40, 161, 23))
        self.slope_degree_label = QLabel(Dialog)
        self.slope_degree_label.setObjectName(u"slope_degree_label")
        self.slope_degree_label.setGeometry(QRect(10, 70, 161, 16))
        self.slope_percentage_label = QLabel(Dialog)
        self.slope_percentage_label.setObjectName(u"slope_percentage_label")
        self.slope_percentage_label.setGeometry(QRect(10, 90, 161, 16))
        self.slope_distance_label = QLabel(Dialog)
        self.slope_distance_label.setObjectName(u"slope_distance_label")
        self.slope_distance_label.setGeometry(QRect(10, 110, 161, 16))
        self.degree_value = QLabel(Dialog)
        self.degree_value.setObjectName(u"degree_value")
        self.degree_value.setGeometry(QRect(180, 70, 211, 16))
        self.percentage_value = QLabel(Dialog)
        self.percentage_value.setObjectName(u"percentage_value")
        self.percentage_value.setGeometry(QRect(180, 90, 211, 16))
        self.distance_value = QLabel(Dialog)
        self.distance_value.setObjectName(u"distance_value")
        self.distance_value.setGeometry(QRect(180, 110, 211, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Elevation Profile and Gradient Calculator", None))
        self.select_points_button.setText(QCoreApplication.translate("Dialog", u"Select Points on Map", None))
        self.calculate_button.setText(QCoreApplication.translate("Dialog", u"Calculate Elevation Profile and Gradient", None))
        self.slope_degree_label.setText(QCoreApplication.translate("Dialog", u"Slope (Degrees):", None))
        self.slope_percentage_label.setText(QCoreApplication.translate("Dialog", u"Slope (Percentage):", None))
        self.slope_distance_label.setText(QCoreApplication.translate("Dialog", u"Slope Distance:", None))
        self.degree_value.setText("")
        self.percentage_value.setText("")
        self.distance_value.setText("")
    # retranslateUi

