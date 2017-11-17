import csv

reads_list = [32270428,6403667,6220977,1605853,1943338,4432151,3828145,4567791,3907105,2225135,2990136,3417783,2629323,1499026,3295452,4465269, \
              2751426,1034065,1420977,1545798]

f1 = open('/home/lavik/Desktop/lavi/regenerationProject/dataFromBioMart', 'r', newline='')
reader1 = csv.reader(f1)
f2 = open('/home/lavik/Desktop/lavi/regenerationProject/originalDataFromDespina', 'r', newline='')
reader2 = csv.reader(f2)
with open('/home/lavik/Desktop/lavi/regenerationProject/result.csv', 'w', newline='') as f_des:
    des = csv.writer(f_des, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row1 in reader1:
        for row2 in reader2:
            val_list = []
            for i in range(1,21):
                val_list.append(int(row2[i])/reads_list[i-1])
            if row1[0] == row2[0]:
                row1[1] = row1[1].replace(',', '')
                row_res = row1 + row2[1:] + val_list
                des.writerow(row_res)
                break
            row_res = row2 + ['NULL','NULL'] + val_list
            des.writerow(row_res)
f1.close()
f2.close()