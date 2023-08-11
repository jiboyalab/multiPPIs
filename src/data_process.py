# from numpy import *
# import random
# import math
import os
# import time
# import pandas as pd
# import math
import argparse
import csv
import numpy as np
def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:          
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return

def AllNodeEdgeAttribute(data_path,save_path):
	
    LDAllLncDisease = []
    ReadMyCsv(LDAllLncDisease, data_path+"LDAllLncDisease.csv")
    print('LDAllLncDisease[0]', LDAllLncDisease[0])

    # LM
    LMSNPLncMi = []
    ReadMyCsv(LMSNPLncMi, data_path+"LMSNPLncMi.csv")
    print('LMSNPLncMi[0]', LMSNPLncMi[0])

    # LP
    LPLncRNA2TargetLncProtein3 = []
    ReadMyCsv(LPLncRNA2TargetLncProtein3, data_path+"LPLncRNA2TargetLncProtein3.csv")
    print('LPLncRNA2TargetLncProtein3[0]', LPLncRNA2TargetLncProtein3[0])

    # MD
    MDCuiMiDisease = []
    ReadMyCsv(MDCuiMiDisease, data_path+"MDCuiMiDisease.csv")
    print('MDCuiMiDisease[0]', MDCuiMiDisease[0])

    # MP
    MPmiRTarBaseMiProtein9 = []
    ReadMyCsv(MPmiRTarBaseMiProtein9, data_path+"MPmiRTarBaseMiProtein5.csv")
    print('MPmiRTarBaseMiProtein9[0]', MPmiRTarBaseMiProtein9[0])

    # PDisease
    PDDisGeNETProteinDisease15 = []
    ReadMyCsv(PDDisGeNETProteinDisease15, data_path+"PDDisGeNETProteinDisease20.csv")
    print('PDDisGeNETProteinDisease15[0]', PDDisGeNETProteinDisease15[0])

    # DD
    DDDrugDisease = []
    ReadMyCsv(DDDrugDisease, data_path+"DrugDiseaseDrugDisease.csv")
    print('DDDrugDisease[0]', DDDrugDisease[0])

    # PDrug
    PDDrugBankAllProteinDrug5 = []
    ReadMyCsv(PDDrugBankAllProteinDrug5, data_path+"DPDrugBankDrugProtein5.csv")
    print('PDDrugBankAllProteinDrug5[0]', PDDrugBankAllProteinDrug5[0])

    # PPI
    PPI = []
    ReadMyCsv(PPI, data_path+"PPI.csv")
    print('PPI[0]', PPI[0])

    # AllEdge
    AllEdge = []
    AllEdge.extend(LDAllLncDisease)
    AllEdge.extend(MDCuiMiDisease)
    AllEdge.extend(LMSNPLncMi)
    AllEdge.extend(MPmiRTarBaseMiProtein9)
    AllEdge.extend(LPLncRNA2TargetLncProtein3)
    AllEdge.extend(PDDisGeNETProteinDisease15)
    AllEdge.extend(PDDrugBankAllProteinDrug5)
    AllEdge.extend(DDDrugDisease)
    # AllEdge.extend(PPI)
    print(len(AllEdge))
    print(AllEdge[0])
    StorFile(AllEdge, save_path+'AllEdge.csv')


    


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
    description='A multi-source heterogeneous graph representation learning for protein-protein interaction prediction',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--path', type=str, default='')
    parser.add_argument('--save', type=str, default='')
    args = parser.parse_args()
    data_path=args.path
    save_path=args.save
    if not os.path.exists(data_path):
       os.system('mkdir '+data_path)
    if not os.path.exists(save_path):
       os.system('mkdir '+save_path)
    AllNodeEdgeAttribute(data_path,save_path)
