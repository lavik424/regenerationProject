
#===============================================================================
# Imports
#===============================================================================
import csv
import numpy as np

NUMOFTHERSHOLD = 20

# readsList = [1605853,1943338,4432151,3828145,4567791,
#               3907105,2225135,2990136,3417783,2629323,
#               1499026,3295452,4465269,32270428,2751426,
#               1034065,1420977,6403667,1545798,6220977]


# reads original data and normalize it by CPM (Counts Per Million reads)
# creates 10 different output files each with different threshold i/min(num of reads in the samples)
def NormalizeDataByThershold(filePath):
    ncols = 0
    with open(filePath,'rb') as f:
        ncols = len(str(f.readline()).split(',')) # compute number of cols in file
    mat = np.loadtxt(open(filePath,'rb'), delimiter=',', skiprows=1, dtype=int, usecols=range(1,ncols))
    readsList = mat.sum(axis=0) # sums each col
    minimumNumOfReads = min(readsList)
    for i in range(1, NUMOFTHERSHOLD):
        print("starting {} iteration".format(i))
        thershold = i / minimumNumOfReads
        destinationPath = 'output/CPMThershold{}.csv'.format(i)
        with open(destinationPath, 'w', newline='') as f_des:
            des = csv.writer(f_des, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            data = np.genfromtxt(filePath, delimiter=',', dtype='U', skip_header=1)
            for row in range(len(data)):
                valList = [data[row][0]]
                for j in range(1,len(data[row])):
                    value = int(data[row][j]) / readsList[j-1]
                    valList.append((value * 10 ** 6) if value > thershold else 0)
                des.writerow(valList)



# removes the lines where all normalized value are 0
def removeZeroLines(reader,filePath):
    print("removing zero lines")
    with open(filePath, 'w', newline='') as f_des:
        des = csv.writer(f_des, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # adds cols names
        row = "GeneID	Sca1+D0	Sca+D1	Sca+D3	Sca+D7	Sca+D30	K15+D0	K15+D1	K15+D3	K15+D7	K15+D30	K15+/CD34+D0" \
              "	K15+/CD34+D1	K15+/CD34+D3	K15+/CD34+D7	K15+/CD34+D30	CD34+D0	CD34+D1	CD34+D3	CD34+D7	CD34+D30"
        des.writerow(row.split("\t"))
        for row in reader:
            for value in row[1:]:
                if float(value) > 0:
                    des.writerow(row)
                    break


def main():

    filePath = 'data/originalSortedCols.csv'
    NormalizeDataByThershold(filePath)
    for i in range(1,NUMOFTHERSHOLD):
        f1 = open('output/CPMThershold{}.csv'.format(i), 'r', newline='')
        reader = csv.reader(f1)
        filePath = 'output/CPMNoZeroLinesThershold{}.csv'.format(i)
        removeZeroLines(reader,filePath)
        f1.close()



if __name__ == '__main__':
    main()