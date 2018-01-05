import csv
import numpy as np




trashold = i/1034065

reads_list = [1605853,1943338,4432151,3828145,4567791,
              3907105,2225135,2990136,3417783,2629323,
              1499026,3295452,4465269,32270428,2751426,
              1034065,1420977,6403667,1545798,6220977]

# merge original data table and data from BioMart. Also normalize num of reads
def join2csv(reader1):
    with open('/home/lavik/Desktop/lavi/regenerationProject/resultCPM.csv', 'w', newline='') as f_des:
        des = csv.writer(f_des, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        minimumNumOfReads = min(reads_list)
        for row1 in reader1:
            for row2 in reader2:
                val_list = []
                for i in range(1, 21):
                    value = int(row2[i]) / reads_list[i - 1]
                    val_list.append((value*10**6) if value > minimum else 0)
                if row1[0] == row2[0]:
                    row1[1] = row1[1].replace(',', '')
                    row_res = row1 + row2[1:] + val_list
                    des.writerow(row_res)
                    break
                row_res = [row2[0], 'NULL', 'NULL'] + row2[1:] + val_list
                des.writerow(row_res)


# removes the lines where all normalized value are 0
def remove_zero_lines(reader):
    with open('/home/lavik/Desktop/lavi/regenerationProject/result1withour0lines.csv', 'w', newline='') as f_des:
        des = csv.writer(f_des, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            for value in row:
                if float(value) > 0:
                    des.writerow(row)
                    break

#flip normalized values to create vectors of different cells
def flip_create_array(reader):
    pass





# main
# f1 = open('/home/lavik/Desktop/lavi/regenerationProject/dataFromBioMart', 'r', newline='')
# reader1 = csv.reader(f1)
# f2 = open('/home/lavik/Desktop/lavi/regenerationProject/originalDataFromDespina', 'r', newline='')
# reader2 = csv.reader(f2)
# join2csv(reader1,reader2)
# f1.close()
# f2.close()
f1 = open('/home/lavik/Desktop/lavi/regenerationProject/onlyCPM.csv', 'r', newline='')
reader = csv.reader(f1)
# x = list(reader)
# result = np.array(x).astype(float)
# for i in range(10):
#     print(result[i])
remove_zero_lines(reader)
f1.close()

#
# if __name__ == '__main__':
#     main()

