# -*- coding: utf-8 -*-
"""
Created on Thu May  5 18:56:33 2022

@author: ezgis
"""

from tkinter import Spinbox
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import sys
import os
import numpy as np
import pickle
from pytictoc import TicToc
from itertools import combinations
from matplotlib.patches import Circle
import matplotlib.pyplot as plt


class Window(QWidget):
    def _init_(self):

        super()._init_()

        self.setGeometry(50, 50, 640, 480)
        self.setWindowTitle("ARM APP")

        self.algoritma = str()
        self.database = str()
        self.minsupp = int()
        self.minkulc = int()
        self.minconf = int()
        self.fis_list = list()
        self.result = list()

        self.init_ui()

        self.show()

    def init_ui(self):

        self.mainLayout = QVBoxLayout()

        self.tab = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        hbox = QHBoxLayout()
        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        v_fourth = QVBoxLayout()

        self.tab.addTab(self.tab1, "Dosya Seç")
        self.tab.addTab(self.tab2, "Algoritma Seç")
        self.tab.addTab(self.tab3, "Min Supp Gir")
        self.tab.addTab(self.tab4, "Min Conf ve Min Int Gir")
        self.tab.addTab(self.tab5, "Arm Rules")

        #   Dosya açma sekmesi işlemleri
        v_dosya_ac = QVBoxLayout()
        self.dosya_ac = QPushButton("Dosya Aç", self)
        self.dosya_ac.resize(250, 250)
        self.dosya_label = QLabel("", self)
        hbox.addStretch()
        hbox.addWidget(self.dosya_ac)
        hbox.addStretch()

        v_dosya_ac.addStretch()
        v_dosya_ac.addLayout(hbox)
        v_dosya_ac.addStretch()
        v_dosya_ac.addWidget(self.dosya_label)
        self.dosya_ac.clicked.connect(self.dosyaAc)
        # ---------------------------

        #   Algoritma seçme sekmesi işlemleri
        v_box = QVBoxLayout()
        self.apriori = QPushButton("Apriori", self)
        self.eclat = QPushButton("Eclat", self)
        self.fptree = QPushButton("FPTree", self)
        self.h_mine = QPushButton("H Mine", self)
        self.second_tab_label = QLabel("", self)
        v_box.addStretch()
        v_box.addWidget(self.apriori)
        v_box.addWidget(self.eclat)
        v_box.addWidget(self.fptree)
        v_box.addWidget(self.h_mine)
        v_box.addStretch()
        v_box.addWidget(self.second_tab_label)
        h_box1.addLayout(v_box)
        self.apriori.clicked.connect(self.second_tab_click)
        self.eclat.clicked.connect(self.second_tab_click)
        self.fptree.clicked.connect(self.second_tab_click)
        self.h_mine.clicked.connect(self.second_tab_click)
        # -----------------------------------------------------

        #   Min supp ve FIS sekmesi işlemleri
        v_spinbox = QVBoxLayout()
        h_spinbox = QVBoxLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.spinbox_label = QLabel("Min supp seçiniz...", self)
        h_spinbox.addWidget(self.spinbox_label)
        h_spinbox.addWidget(self.slider)
        h_spinbox.addStretch()
        v_spinbox.addLayout(h_spinbox)
        self.spin_box_value = QLabel("", self)
        self.fis_label = QLabel("", self)
        self.fis_title_label = QLabel("", self)
        self.calculate_fis = QPushButton("Hesapla", self)
        h_spinbox2 = QHBoxLayout()
        h_spinbox2.addStretch()
        self.slider.valueChanged.connect(self.sliderFunc)
        h_spinbox2.addWidget(self.spin_box_value)
        h_spinbox2.addWidget(self.calculate_fis)
        h_spinbox2.addStretch()
        self.calculate_fis.clicked.connect(self.fisHesapla)

        h_box2.addLayout(v_spinbox)
        v_spinbox.addWidget(self.slider)
        v_spinbox.addLayout(h_spinbox2)
        v_spinbox.addStretch()
        v_spinbox.addStretch()
        v_spinbox.addWidget(self.fis_title_label)
        v_spinbox.addWidget(self.fis_label)

        # -----------------------------------------------------------

        #   min conf ve min kulc girildikten sonra arm sekmesi işlemleri

        h_top = QHBoxLayout()
        h_mid = QHBoxLayout()

        self.slider_kulc = QSlider(Qt.Horizontal)
        self.slider_kulc.setMinimum(0)
        self.slider_kulc.setMaximum(100)
        self.slider_kulc.setTickInterval(1)
        self.slider_kulc.setTickPosition(QSlider.TicksBelow)
        self.kulc_label = QLabel("Min kulc seçiniz...", self)
        self.kulc_value = QLabel("", self)
        self.slider_kulc.valueChanged.connect(self.slider_kulc_func)

        self.slider_conf = QSlider(Qt.Horizontal)
        self.slider_conf.setMinimum(0)
        self.slider_conf.setMaximum(100)
        self.slider_conf.setTickInterval(1)
        self.slider_conf.setTickPosition(QSlider.TicksBelow)
        self.conf_label = QLabel("Min conf seçiniz...", self)
        self.conf_value = QLabel("", self)
        self.slider_conf.valueChanged.connect(self.slider_conf_func)

        self.hesapla_button = QPushButton("Hesapla", self)

        v_fourth.addWidget(self.kulc_label)
        v_fourth.addWidget(self.slider_kulc)
        h_top.addStretch()
        h_top.addWidget(self.kulc_value)
        h_top.addStretch()
        v_fourth.addLayout(h_top)

        v_fourth.addWidget(self.conf_label)
        v_fourth.addWidget(self.slider_conf)
        h_mid.addStretch()
        h_mid.addWidget(self.conf_value)
        h_mid.addStretch()
        v_fourth.addLayout(h_mid)
        v_fourth.addWidget(self.hesapla_button)
        self.hesapla_button.clicked.connect(self.arm_func)

        # -------------------------------------------------------------

        #   ARM rules sekmesi işlemleri
        v_rules = QVBoxLayout()
        self.arm_title_label = QLabel("", self)
        self.arm_label = QLabel("", self)
        v_rules.addWidget(self.arm_title_label)
        v_rules.addWidget(self.arm_label)
        v_rules.addStretch()

        # -------------------------------------------------------------

        self.tab1.setLayout(v_dosya_ac)
        self.tab2.setLayout(h_box1)
        self.tab3.setLayout(h_box2)
        self.tab4.setLayout(v_fourth)
        self.tab5.setLayout(v_rules)
        self.mainLayout.addWidget(self.tab)

        self.setLayout(self.mainLayout)

    def arm_func(self):

        if self.slider_conf.value() and self.slider_kulc.value():
            arm_str = str()

            if self.algoritma == "H Mine":
                self.result = H_mine(
                    self.database, self.minsupp * 10000, self.minkulc, self.minconf
                )
            elif self.algoritma == "Apriori":

                self.result = Apriori(
                    self.database, self.minsupp * 10000, self.minkulc, self.minconf
                )

                for arm in self.result:
                    arm_str = arm_str + arm + "\n"

            elif self.algoritma == "Eclat":
                pass
            elif self.algoritma == "FPTree":
                pass
            else:
                QMessageBox.information(
                    self, "Information", "Lütfen algoritma seçiniz.."
                )
            self.arm_title_label.setText("Arm Rules:")

            self.arm_label.setText(arm_str)

        else:
            QMessageBox.information(
                self,
                "Information",
                "Lütfen önce minconf ve minkulc değerlerini seçiniz",
            )

    def fisHesapla(self):

        if self.slider.value():

            fis_str = str()

            if self.algoritma == "H Mine":
                H_mine(self.database, self.minsupp * 10000)
            elif self.algoritma == "Apriori":

                self.fis_list = Apriori(self.database, self.minsupp * 10000)
                for fis in self.fis_list:
                    fis_str = fis_str + fis + "\n"
            elif self.algoritma == "Eclat":
                pass
            elif self.algoritma == "FPTree":
                pass
            else:
                QMessageBox.information(
                    self, "Information", "Lütfen algoritma seçiniz.."
                )

            self.fis_title_label.setText("Frequent Item Sets:")
            self.fis_label.setText(fis_str)

        else:
            QMessageBox.information(
                self, "Information", "Lütfen önce minsupp değerini seçiniz"
            )

    def slider_kulc_func(self):

        self.kulc_value.setText(f"Min kulc : {self.slider_kulc.value()/100} ")
        self.minkulc = self.slider_kulc.value() / 100

    def slider_conf_func(self):

        self.conf_value.setText(f"Min conf : {self.slider_conf.value()/100} ")
        self.minconf = self.slider_conf.value() / 100

    def sliderFunc(self):
        self.spin_box_value.setText(f"Min sup : {self.slider.value()/100} ")
        self.minsupp = self.slider.value()

    def second_tab_click(self):
        sender = self.sender()
        self.algoritma = sender.text()
        self.second_tab_label.setText(f"Seçilen algoritma : {sender.text()} ")

    def dosyaAc(self):

        dosya_ismi = QFileDialog.getOpenFileName(self, "Dosya Aç", os.getenv("HOME"))
        dosya_uzantisi = str()

        for i in range(len(dosya_ismi[0])):
            if dosya_ismi[0][i] == ".":
                dosya_uzantisi = [
                    dosya_ismi[0][i] for i in range(i, len(dosya_ismi[0]))
                ]

        dosya_uzantisi_str = ""

        for item in dosya_uzantisi:
            dosya_uzantisi_str += item

        if dosya_uzantisi_str != ".pckl":
            QMessageBox.information(
                self, "Information", "Lütfen pckl uzantılı bir database seçiniz..."
            )
        else:
            self.database = dosya_ismi[0]
            self.dosya_label.setText(f"Seçilen dosya : {self.database} ")


def Apriori(_database, _minsupp, _minkulc=None, _minconf=None):
    with open(_database, "rb") as f:
        DATABASE, SingleItems = pickle.load(f)

    database = DATABASE
    singleItems = SingleItems

    def DoesExist(itm, transaction):
        if sum(transaction[itm]) == len(itm):
            E = 1
        else:
            E = 0
        return E

    def CalcAbsSupp(itm, database):
        absSupp = 0
        for i in range(0, database.shape[0]):
            transaction = database[i, :]
            if DoesExist(itm, transaction):
                absSupp += 1
        return absSupp

    def CandidateGeneration(fkm1):
        ck = []
        for i in range(0, len(fkm1) - 1):
            for j in range(i + 1, len(fkm1)):

                itemset1 = fkm1[i]
                itemset2 = fkm1[j]

                if all(itemset1[1:] == itemset2[:-1]):
                    NewItem = np.hstack((np.array(itemset1), np.array(itemset2[-1])))
                    ck.append(NewItem)

        return ck

    minsupp = _minsupp

    NumOfTransaction = database.shape[0]
    initial_SUPPORTSs = np.sum(database, axis=0)
    ItemsToBeRemained = np.nonzero(minsupp <= initial_SUPPORTSs)[0]
    database = database[:, ItemsToBeRemained]
    singleItems = singleItems[ItemsToBeRemained]

    FREQUENTITEMSETS = []
    SUPPORTS = []
    fk = []

    NumOfItems = database.shape[1]
    NumOfTrs = database.shape[0]

    ItemsetIndices = np.arange(0, NumOfItems)

    # k=1
    for i in range(0, NumOfItems):
        itm = np.array([i])
        abssupp = CalcAbsSupp(itm, database)
        if abssupp >= minsupp:
            fk.append(itm)
            FREQUENTITEMSETS.append(itm)
            SUPPORTS.append(abssupp)
            # print(FREQUENTITEMSETS[i], abssupp)

    # print(fk)
    # k=2
    loop = 1

    while loop:
        fkm1 = fk
        fk = []
        ck = CandidateGeneration(fkm1)
        for i in range(0, len(ck)):
            adayOgeseti = ck[i]
            abssupp = CalcAbsSupp(adayOgeseti, database)
            if abssupp >= minsupp:
                fk.append(adayOgeseti)
                FREQUENTITEMSETS.append(adayOgeseti)
                SUPPORTS.append(abssupp)
                # k += 1
        if len(ck) * len(fk) == 0:
            loop = 0

    I = np.argsort(-np.array(SUPPORTS))
    FREQUENTITEMSETS = [FREQUENTITEMSETS[i] for i in I]
    SUPPORTS = [SUPPORTS[i] for i in I]
    fis_list = list()
    for i in range(0, len(FREQUENTITEMSETS)):
        itemset = FREQUENTITEMSETS[i]
        tmp = " "
        for j in itemset:
            tmp = tmp + singleItems[j]
        fis_list_str = f"# {i+1} {tmp} Supp: {SUPPORTS[i]}"

        fis_list.append(fis_list_str)

    with open("FIMresults", "wb") as f:
        pickle.dump([FREQUENTITEMSETS, SUPPORTS, singleItems, database], f)

    try:
        from IPython import get_ipython

        get_ipython().magic("clear")
        get_ipython().magic("reset -f")
    except:
        pass

    def ShowDatabase(database, singleItems):
        for i in range(0, database.shape[0]):
            tr = database[i, :]
            I = np.nonzero(tr > 0)[0]
            itemset = ""
            for itm in singleItems[I]:
                itemset = itemset + str(itm)
            print(i, ":", itemset)
        return

    def FindIndex(itemset, FREQUENTITEMSETS):
        I = []
        for k in range(0, len(FREQUENTITEMSETS)):
            tmp = FREQUENTITEMSETS[k]
            if tmp.shape[0] == itemset.shape[0]:
                if all(itemset == tmp):
                    I = k
                    break
        return I

    with open("FIMresults", "rb") as f:
        FREQUENTITEMSETS, SUPPORTS, singleItems, database = pickle.load(f)
    NumOfTransaction = database.shape[0]
    SUPPORTS = [support / NumOfTransaction for support in SUPPORTS]

    if _minkulc == None:
        return fis_list
    else:
        MinKulc = _minkulc
        MinConf = _minconf
    result = list()
    for itemset in FREQUENTITEMSETS:
        L = itemset.shape[0]

        if 1 < L:
            I = FindIndex(itemset, FREQUENTITEMSETS)
            SUPPORTitemset = SUPPORTS[I]
            for j in range(1, L):
                CBMN = list(combinations(np.arange(0, L), j))
                CBMN = np.matrix(CBMN)
                for k in range(0, len(CBMN)):
                    PrefixIndex = np.array(CBMN[k, :])[0]
                    tmp = np.ones(L, dtype="int8")
                    tmp[PrefixIndex] = 0
                    SuffixIndex = np.nonzero(tmp == 1)[0]
                    Prefix = itemset[PrefixIndex]
                    Suffix = itemset[SuffixIndex]
                    tmpPrefix = ""
                    for kk in range(0, np.size(Prefix)):
                        tmpPrefix = tmpPrefix + singleItems[Prefix[kk]]
                    tmpSuffix = ""
                    for kk in range(0, np.size(Suffix)):
                        tmpSuffix = tmpSuffix + singleItems[Suffix[kk]]
                    I = FindIndex(Prefix, FREQUENTITEMSETS)
                    SUPPORTPrefix = SUPPORTS[I]
                    Confidence = SUPPORTitemset / SUPPORTPrefix
                    I = FindIndex(Suffix, FREQUENTITEMSETS)
                    SUPPORTSuffix = SUPPORTS[I]
                    Kulc = 0.5 * (
                        SUPPORTitemset / SUPPORTPrefix + SUPPORTitemset / SUPPORTSuffix
                    )
                    Kulc = 2 * (Kulc - 0.5)
                    if MinKulc <= Kulc:
                        if MinConf <= Confidence:
                            temp_str = str()
                            temp_str = "{} ---> {}   supp.: {:.3f} conf.: {:.3f}  Kulc.: {:.3f} ".format(
                                tmpPrefix, tmpSuffix, SUPPORTitemset, Confidence, Kulc
                            )
                            result.append(temp_str)
                            # print(
                            #    tmpPrefix,
                            #    "-->",
                            #    tmpSuffix,
                            #    "  supp.:",
                            #    "{:.3f}".format(SUPPORTitemset),
                            #    "conf.:",
                            #    "{:.3f}".format(Confidence),
                            #    "Kulc.:",
                            #    "{:.3f}".format(Kulc),
                            # )
                            # print(temp_str)
                            # result.append(temp_str)
                            # = list(
                            #    tmpPrefix,
                            #    "-->",
                            #    tmpSuffix,
                            #    "  supp.:",
                            #    "{:.3f}".format(SUPPORTitemset),
                            #    "conf.:",
                            #    "{:.3f}".format(Confidence),
                            #    "Kulc.:",
                            #    "{:.3f}".format(Kulc),
                            # )

    return result


def Eclat(_database, _minsupp, _minkulc=None, _minconf=None):

    t = TicToc()

    with open(_database, "rb") as f:
        DATABASE, SingleItems = pickle.load(f)

    database = DATABASE
    singleItems = SingleItems

    def showDatabase(database, singleItems):
        for i in range(database.shape[0]):
            tr = database[i, :]
            I = np.nonzero(tr > 0)[0]
            print(i, ":", singleItems[I])
        return

    def transposeDB(database, trs, sI):
        transposeTemp = database.T
        for i in range(transposeTemp.shape[0]):
            tr = transposeTemp[i, :]
            idx = np.nonzero(tr > 0)[0]
            print(sI[i], ":", trs[idx])
        return

    # -----------------------------------------------------------------------------
    #                   A  B  C  D  E
    # DATABASE = np.array(
    #    [
    #        [1, 0, 1, 1, 0],
    #        [0, 1, 1, 0, 1],
    #        [1, 1, 1, 0, 1],
    #        [0, 1, 0, 0, 1],
    #        [1, 1, 1, 0, 1],
    #    ],
    # )
    #
    #
    # singleItems = np.array(["A", "B", "C", "D", "E"])
    trsItems = np.array(["T1", "T2", "T3", "T4", "T5"])
    minSupp = _minsupp

    # -----------------------------------------------------------------------------
    def eclatDfsLoop(
        itemset,
        itemsetTIDList,
        TIDList,
        minSupp,
        frequentItemSets,
        supports,
        numOfItems,
    ):
        # print(singleItems[itemset],
        #       '  -->  ', trsItems[itemsetTIDList], '\n')
        print(singleItems[itemset], "  -->  ", itemsetTIDList, "\n")
        temp = itemset[-1]
        for i in range(temp + 1, numOfItems):

            newItemSet = 1 * itemset
            newItemSet.append(i)
            newItemSetTIDList = []
            suffixTIDList = 1 * TIDList[i]
            newItemSetTIDList = np.intersect1d(itemsetTIDList, suffixTIDList)
            suppOfNewItemSet = len(newItemSetTIDList)
            if minSupp <= suppOfNewItemSet:
                frequentItemSets.append(newItemSet)
                supports.append(suppOfNewItemSet)
                (frequentItemSets, supports) = eclatDfsLoop(
                    newItemSet,
                    newItemSetTIDList,
                    TIDList,
                    minSupp,
                    frequentItemSets,
                    supports,
                    numOfItems,
                )
        return frequentItemSets, supports

    # -----------------------------------------------------------------------------

    t.tic()

    TIDList = []
    frequentItemSets = []
    supports = []
    initialSupports = np.sum(database, axis=0)
    numOfItems = database.shape[1]

    # determine TID list
    for i in range(0, numOfItems):
        idx = np.nonzero(database[:, i] > 0)[0]
        TIDList.append(list(idx))

    print(TIDList)

    # preperation frequent item sets and supports
    for i in range(0, numOfItems):
        frequentItemSets.append([i])
        supports.append(initialSupports[i])

    # eclat dfs starting down here
    print("\nItemsets and TID Lists:\n")
    for item in range(0, numOfItems):
        itemset = [item]
        itemsetTIDList = TIDList[item]
        print(
            "-----------------------------------------------------------------------------"
        )
        # print('DFS ', item+1, '. döngü', ' - itemset:', itemset,
        #       singleItems[itemset], ' - itemsetTIDList:', itemsetTIDList, trsItems[itemsetTIDList], '\n')
        print(
            "DFS ",
            item + 1,
            ". döngü",
            " - itemset:",
            itemset,
            singleItems[itemset],
            " - itemsetTIDList:",
            itemsetTIDList,
            "\n",
        )
        (frequentItemSets, supports) = eclatDfsLoop(
            itemset,
            itemsetTIDList,
            TIDList,
            minSupp,
            frequentItemSets,
            supports,
            numOfItems,
        )

    t.toc()

    I = np.argsort(-np.array(supports))
    frequentItemSets = [frequentItemSets[i] for i in I]
    supports = [supports[i] for i in I]
    print("\nSUPPORTS:\n")
    for i in range(0, len(frequentItemSets)):
        itemset = frequentItemSets[i]
        tmp = " "
        for j in itemset:
            tmp = tmp + singleItems[j]
        print("#", i + 1, tmp, "Supp:", (supports[i] * 2) / 10, " => ", supports[i])

    with open("EclatResults", "wb") as f:
        pickle.dump([frequentItemSets, supports, singleItems, database, trsItems], f)


def FpTree():

    DATABASE = np.array(
        [
            [1, 1, 1, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 1],
            [1, 0, 0, 1, 1],
            [1, 1, 1, 0, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
        ],
    )

    SingleItems = np.array(["A", "B", "C", "D", "E"])
    # ------------------------------------------------------------------------------

    def ConstructTree(DATABASE, OCCS, SingleItems, MinAbsSupp):
        supports = np.sum(DATABASE * OCCS.reshape(-1, 1), axis=0)
        I = np.argsort(-supports)
        DATABASE = DATABASE[:, I]
        SingleItems = SingleItems[I]
        supports = supports[I]
        NODES = np.array([-1])
        treeItems = np.array([-1])
        counts = np.array([-1])
        I = np.nonzero(MinAbsSupp <= supports)[0]
        if I.shape[0] > 0:
            for trind in range(0, DATABASE.shape[0]):
                transaction = DATABASE[trind, :]
                if sum(transaction) > 0:
                    transactionIndices = np.nonzero(transaction == 1)[0]
                    if trind == 0:
                        NODES = np.array([-1])
                        treeItems = np.array([-1])
                        counts = np.array([-1])
                        for j in range(0, len(transactionIndices)):
                            NODES = np.hstack((NODES, [j]))
                            treeItems = np.hstack((treeItems, [transactionIndices[j]]))
                            counts = np.hstack((counts, [OCCS[trind]]))
                    else:
                        parentIndex = 0
                        index = 0
                        loop = 1
                        while loop:
                            I = np.nonzero(NODES == parentIndex)[0]
                            childNodeItems = []
                            childNodeIndices = []
                            for i in I:
                                childNodeItems.append(treeItems[i])
                                childNodeIndices.append(i)
                            I = np.nonzero(transactionIndices[index] == childNodeItems)[
                                0
                            ]
                            if I.shape[0] > 0:
                                counts[childNodeIndices[I[0]]] += OCCS[trind]
                                parentIndex = childNodeIndices[I[0]]
                                index += 1
                            else:
                                loop = 0
                            if index == transactionIndices.shape[0]:
                                loop = 0

                        for i in range(index, transactionIndices.shape[0]):
                            NODES = np.hstack((NODES, [parentIndex]))
                            treeItems = np.hstack((treeItems, [transactionIndices[i]]))
                            counts = np.hstack((counts, [OCCS[trind]]))
                            parentIndex = len(NODES) - 1
                PlotTree(NODES, treeItems, counts, SingleItems)
        return NODES, treeItems, counts, DATABASE, SingleItems

    # ------------------------------------------------------------------------------

    def mean(numbers):
        return float(sum(numbers)) / max(len(numbers), 1)

    # ------------------------------------------------------------------------------

    def FindEqualTo(itm, X):
        I = [i for i in range(0, len(X)) if X[i] == itm]
        return I

    # ------------------------------------------------------------------------------

    def FindTheLeavesInTheTree(parent, Leaves, dpth, DEPTH, NODES):
        IndexOfChilds = np.array(FindEqualTo(parent, NODES))
        if len(IndexOfChilds) == 0:
            Leaves.append(parent)
        else:
            dpth = dpth + 1
            DEPTH[IndexOfChilds] = dpth
            for i in range(0, IndexOfChilds.size):
                parent = IndexOfChilds[i]
                [Leaves, DEPTH] = FindTheLeavesInTheTree(
                    parent, Leaves, dpth, DEPTH, NODES
                )
        return Leaves, DEPTH

    # ------------------------------------------------------------------------------

    def treelayout(NODES):
        parent = 0
        Leaves = []
        dpth = 1
        DEPTH = np.ones((len(NODES)), dtype=int)
        [Leaves, DEPTH] = FindTheLeavesInTheTree(parent, Leaves, dpth, DEPTH, NODES)
        MaxDepth = max(DEPTH)

        dx = 1 / (len(Leaves) + 1)
        dy = 1 / (MaxDepth + 1)

        # ...vertical coordinates
        y = 1 - DEPTH * dy

        # ...horizontal coordinates of the leaves
        x = np.zeros(len(y), dtype="float64")
        for i in range(0, len(Leaves)):
            itm = Leaves[i]
            x[itm] = (i + 1) * dx

        # ...horizontal coordinates of remaining nodes
        for dpth in range(MaxDepth - 1, 0, -1):
            items = np.array(FindEqualTo(dpth, DEPTH))
            for i in range(0, len(items)):
                parent = items[i]
                IndexOfChilds = np.array(FindEqualTo(parent, NODES))
                if DEPTH[parent] == dpth:
                    if len(IndexOfChilds) > 0:
                        x[parent] = mean(x[IndexOfChilds])
        return x, y

    # ------------------------------------------------------------------------------

    def PlotTree(NODES, TREEITEMS, COUNTS, SingleItems):
        fig, ax = plt.subplots()

        [x, y] = treelayout(NODES)
        plot_loop(0, x, y, NODES)

        circle_facecolor = [0.2, 0.8, 1, 1]
        circle_edgecolor = [0.2, 0.8, 1, 1]
        nodeindex_color = [0, 0, 0, 1]
        circle = Circle(
            (x[0], y[0]),
            0.03,
            fc=circle_facecolor,
            ec=circle_edgecolor,
            fill=True,
            linewidth=0.5,
        )
        ax.add_patch(circle)
        plt.text(
            x[0],
            y[0],
            "root",
            weight="bold",
            color=nodeindex_color,
            fontsize=10,
            family="calibri",
            style="normal",
            horizontalalignment="center",
            verticalalignment="center",
        )
        for j in range(1, len(x)):
            circle = Circle(
                (x[j], y[j]),
                0.03,
                fc=circle_facecolor,
                ec=circle_edgecolor,
                fill=True,
                linewidth=0.5,
            )
            ax.add_patch(circle)
            plt.text(
                x[j],
                y[j],
                str(j),
                weight="bold",
                color=nodeindex_color,
                fontsize=10,
                family="calibri",
                style="normal",
                horizontalalignment="center",
                verticalalignment="center",
            )

        for j in range(1, len(x)):
            tmp = SingleItems[TREEITEMS[j]]
            plt.text(
                x[j] + 0.03,
                y[j],
                tmp + ":" + str(COUNTS[j]),
                color=[1, 0, 0, 1],
                fontsize=10,
                family="consolas",
                style="normal",
                horizontalalignment="left",
                verticalalignment="center",
            )
            plt.text(
                x[j] + 0.03,
                y[j],
                tmp,
                color=[0, 0, 0, 1],
                fontsize=10,
                family="consolas",
                style="normal",
                horizontalalignment="left",
                verticalalignment="center",
            )

        ax.spines["bottom"].set_color("white")
        ax.spines["top"].set_color("white")
        ax.spines["right"].set_color("white")
        ax.spines["left"].set_color("white")
        ax.tick_params(axis="x", colors="white")
        ax.tick_params(axis="y", colors="white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.show()
        return

    # -----------------------------------------------------------------------------

    def plot_loop(parent, x, y, NODES):
        IndexOfChilds = np.array(FindEqualTo(parent, NODES))
        for i in range(0, len(IndexOfChilds)):
            child = IndexOfChilds[i]
            plt.plot(
                x[[parent, child]],
                y[[parent, child]],
                color=[0.2, 0.8, 1, 1],
                linewidth=0.5,
            )
            plot_loop(child, x, y, NODES)
        return

    # ------------------------------------------------------------------------------

    OCCS = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    MinAbsSupp = 2
    ConstructTree(DATABASE, OCCS, SingleItems, MinAbsSupp)


def H_mine(_database, _minsupp):
    # -----------------------------------------------------------------------------
    with open(_database, "rb") as f:
        DATABASE, SingleItems = pickle.load(f)

    database = DATABASE
    singleItems = SingleItems

    # -----------------------------------------------------------------------------
    def hminLoop(newItem, database, minsupp, frequentItemSets, supports):
        indices = np.nonzero(np.sum(database[:, newItem], axis=1) == len(newItem))[0]
        projectedDB = database[indices, :]
        initialSupports = np.sum(projectedDB, axis=0)
        suffixes = np.nonzero(initialSupports >= minsupp)[0]
        suffixes = suffixes[np.nonzero(suffixes > newItem[-1])[0]]
        for suffix in suffixes:
            itemSet = 1 * newItem
            itemSet.append(suffix)
            frequentItemSets.append(itemSet)
            supports.append(initialSupports[suffix])
            (frequentItemSets, supports) = hminLoop(
                itemSet, projectedDB, minsupp, frequentItemSets, supports
            )
        return (frequentItemSets, supports)

    minsupp = _minsupp
    # -----------------------------------------------------------------------------

    #
    initialSupports = np.sum(database, axis=0)

    # items to be remained
    itemsToBeRemained = np.nonzero(initialSupports >= minsupp)[0]

    # new database with items to be remained
    database = database[:, itemsToBeRemained]

    # new single items of items to be remained
    singleItems = singleItems[itemsToBeRemained]

    # initial supports of items to be remained
    initialSupports = initialSupports[itemsToBeRemained]

    # num of items of to be remained
    numOfItems = singleItems.shape[0]

    frequentItemSets = []
    supports = []

    # -----------------------------------------------------------------------------
    for item in range(0, numOfItems):
        newItem = [item]
        frequentItemSets.append(newItem)
        supports.append(initialSupports[item])
        (frequentItemSets, supports) = hminLoop(
            newItem, database, minsupp, frequentItemSets, supports
        )

    # -----------------------------------------------------------------------------
    I = np.argsort(-np.array(supports))
    frequentItemSets = [frequentItemSets[i] for i in I]
    supports = [supports[i] for i in I]
    for i in range(0, len(frequentItemSets)):
        itemset = frequentItemSets[i]
        tmp = " "
        for j in itemset:
            tmp = tmp + singleItems[j]
        print("#", i + 1, tmp, "Supp:", (supports[i] * 2) / 10, " => ", supports[i])

    with open("FIMresults", "wb") as f:
        pickle.dump([frequentItemSets, supports, singleItems, database], f)


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())