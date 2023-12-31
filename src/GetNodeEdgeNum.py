import csv
from numpy import *
# import numpy as np
# import random
# import math
# import os
# import time
# import pandas as pd
#
# import math
# import random


def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:          
        SaveList.append(row)
    return

def ReadMyCsv2(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        for i in range(len(row)):      
            row[i] = float(row[i])
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return


AllNode = []
ReadMyCsv(AllNode, "AllNode.csv")
print('len(AllNode)', len(AllNode))
print('AllNode[0]', AllNode[1])

AllEdge = []
ReadMyCsv(AllEdge, "AllEdge.csv")
print('len(AllEdge)', len(AllEdge))
print('AllEdge[0]', AllEdge[0][1])

#  nonhsat090275.2,glioma --》1490,3530
AllEdgeNum = []
counter = 0
while counter < len(AllEdge):

    flag1 = 0
    counter1 = 0
    while counter1 < len(AllNode):
        if AllEdge[counter][0] == AllNode[counter1][0]:
            flag1 = 1
            break
        counter1 = counter1 + 1

    flag2 = 0
    counter2 = 0
    while counter2 < len(AllNode):
        if AllEdge[counter][1] == AllNode[counter2][0]:
            flag2 = 1
            break
        counter2 = counter2 + 1

    if flag1 == 1 and flag2 == 1:
        pair = []
        pair.append(str(counter1))
        pair.append(str(counter2))
        AllEdgeNum.append(pair)

    counter = counter + 1

print(len(AllEdgeNum))


StorFile(AllEdgeNum, 'AllEdgeNum.csv')

AllNodeNum = []
counter = 0
while counter < len(AllNode):
    pair = []
    pair.append(str(counter))
    AllNodeNum.append(pair)
    counter = counter + 1

StorFile(AllNodeNum, 'AllNodeNum.csv')
