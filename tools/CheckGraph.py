# from numpy import *
# import numpy as np
# import Tool
#
# import random
# import math
# import os
# import time
# import pandas as pd
#
# import math
# import random
import networkx as nx
import csv
def MyReadCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:         
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return


AllNode = []
MyReadCsv(AllNode, "AllNode.csv")
print('AllNode[0]', AllNode[0])


graph = nx.Graph()
#print('node')

counter1 = 0
while counter1 < len(AllNode):
    graph.add_node(AllNode[counter1][0]) 
    counter1 = counter1 + 1
print('2')
print( graph.number_of_nodes())
print( graph.number_of_edges())

AllEdge = []
MyReadCsv(AllEdge, "AllEdge.csv")
print('AllEdge[0]', AllEdge[0])


graph = nx.Graph()

counter1 = 0
while counter1 < len(AllEdge):
    temp = tuple(AllEdge[counter1])
    graph.add_edge(*temp)  
    # print( graph.number_of_edges())
    # print(counter1)
    counter1 = counter1 + 1

print('3')
print( graph.number_of_nodes())
print( graph.number_of_edges())
#print( graph.nodes())
