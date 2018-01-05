import re
import csv
import numpy as np
from itertools import permutations

# consts for num of members in group cluster
CELLLINESIZE = 5
DAYSSIZE = 4


# pattern for different cell lines
listCellTypePatterns = ["^Sca","^K15\+D","^K15\+/","^CD34\+D"]
# patterns for days
listDaysPatterns = ["\+D0","\+D1","\+D3$","\+D7","\+D30"]



# func for calculation distance from cluster by cell lines
# input: list of strings, patterns list , size of expected cluster
# output: matrix of distance
def distance(listOfClusters,listPatterns,realSize):
    disMat = np.zeros((len(listPatterns), len(listPatterns)), dtype=np.int)
    i = 0
    for cluster in listOfClusters:
        cluster = cluster.split()
        a = []
        sumCluster = 0
        for j in range(len(listPatterns)):
            # search in entire string (used for D*) and match was used for cell line pattern
            a.append([x for x in cluster if re.search(listPatterns[j],x)])
            sumCluster += len(a[j])
        for j in range(len(listPatterns)):
            disMat[i,j] = realSize - 2*len(a[j]) + sumCluster
        i += 1
    print(disMat)
    return disMat


# func for calculation min distance foreach permutation
# input: distance matrix
# output: score of best permutation
def calcMinPermutation(disMat,size):
    minPer = np.inf
    for per in permutations(range(size)):
        sum = 0
        for i in range(size):
            sum += disMat[i,per[i]]
        minPer = min(minPer,sum)
    return minPer


# iterate over csv of clusters by thershold to compute best thershold
# input: csv clustering file with list of string in each row
# output: best threshold
def readTable(reader,listPatterns,realSize):
    # destinationPath = '/home/lavik/Desktop/lavi/regenerationProject/cellsTypesResultOfThreshold'
    destinationPath = '/home/lavik/Desktop/lavi/regenerationProject/daysResultOfThreshold'
    file = open(destinationPath, 'w')
    i = 1
    minThersList = {}
    dicDisMat = {}
    for row in reader:
        dicDisMat[i] = distance(row,listPatterns,realSize)
        minThersList[i] = calcMinPermutation(dicDisMat[i],len(listPatterns))
        value = "For thershold number:{} the minimal score is:{}\n".format(i,minThersList[i])
        file.write(value)
        i += 1
    print(min(minThersList.values()))



# main:
f1 = open('/home/lavik/Desktop/lavi/regenerationProject/outputDays.csv') # for clusters by days
# f1 = open('/home/lavik/Desktop/lavi/regenerationProject/outputCellsTypes.csv') # for clusters by cells types
reader = csv.reader(f1)
readTable(reader,listDaysPatterns,DAYSSIZE) # for clusters by days
# readTable(reader,listCellTypePatterns,CELLLINESIZE) # for clusters by cells types
f1.close()


