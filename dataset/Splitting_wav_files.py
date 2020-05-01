import sys
import shutil

file = sys.argv[1]

f = open(file+'.csv')

header = 1

for i in f.readlines():
	if header == 1:
		header = 0
	else:
		line = i.split(',')
		shutil.copyfile('all/'+line[0],file+'/'+line[0])
		print(line[0])
