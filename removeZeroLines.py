import csv





# removes the lines where all normalized value are 0
def removeZeroLines(reader,filePath):
    print("removing zero lines")
    with open(filePath, 'w', newline='') as f_des:
        des = csv.writer(f_des, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if reader.line_num == 1:
                des.writerow(row)
                continue
            for value in row[1:]: # iterate over values from second col (first is gene ID)
                if float(value) > 0:
                    des.writerow(row)
                    break



# main

files = ["sca","k15","k15cd34","cd34"]


for f in files:
    f1 = open('/home/lavik/Desktop/lavi/regenerationProject/{}.csv'.format(f), 'r', newline='')
    reader = csv.reader(f1)
    filePath = '/home/lavik/Desktop/lavi/regenerationProject/{}NoZero.csv'.format(f)
    removeZeroLines(reader,filePath)
    f1.close()

