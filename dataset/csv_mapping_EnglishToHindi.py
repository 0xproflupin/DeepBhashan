import csv

ee = open("output6.txt",'r',encoding='utf8')
hh = open ("H.txt",'r',encoding='utf8')
ee1 = ee.readlines()
hh1=hh.readlines()
ee.close()
hh.close()
ee1=ee1[0].split(", ")
hh1=hh1[0].split("', '")
print(len(ee1))
print(len(hh1))
       
with open('train.csv',encoding='utf8') as csv_file,  open('train_1.csv', 'w', encoding='utf8', newline='') as write_obj:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_writer = csv.writer(write_obj)
    line_count = 0
    for row in csv_reader:
        if line_count !=0:
            a = row[2]
            a=a.split()
            #print(a)
            b=""
            for i in range(len(a)):
                dee=0
                for j in range(len(ee1)):
                    if a[i]==ee1[j][1:-1]:
                        b = b + " " + (hh1[j])
                        dee+=1
                        break
                if(dee==0):
                    b= b+" " + "undefined"
            #print(b)
            row.append(b)
            csv_writer.writerow(row)
        line_count+=1
        print(line_count)

