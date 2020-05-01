from googletrans import Translator
import time
fi = open("output2.txt",'w',encoding='utf8')

a=[]
final=[]
F=[]

for i in range(2,31):
    f = open("chap"+str(i)+".txt",  encoding="utf8")
    for x in f:
      a.append(x)

    for y in range(len(a)):
        final.append(a[y].split())

    for t in range(len(final)):
        for j in range(len(final[t])):
            F.append(final[t][j])

#print(len(F))
test_list = list(set(F))
#print(len(test_list))
#print(test_list, file = fi)
# print()
final = [];
translator = Translator();
english_arr = [chr(ord('a')+i) for i in range(0,26)];
english_arr.append(' ')
cnt = 0;
size = 5;
trans_words=[]
for i in range(0,len(test_list),size):
    chunk = test_list[i:min(len(test_list),i+size)]
    chunk = " ".join(chunk)
    ok = translator.translate(chunk,src= 'en',dest='hindi')
    time.sleep(2)
    if ok.extra_data['translation'][1][2] != None:
        my = (ok.extra_data['translation'][1][2])
        my = my.split();
        for word in my:
            tmp = ""
            for c in word:
                if c in english_arr:
                    tmp+=c;
            if len(tmp)>0:
                print(tmp)
                #print(tmp, file =fi)
                trans_words.append(tmp)
    elif ok.extra_data['translation'][-1][-1]!=None:
        my = (ok.extra_data['translation'][-1][-1])
        my = my.split();
        for word in my:
            tmp = ""
            for c in word:
                if c in english_arr:
                    tmp += c;
            if len(tmp) > 0:
                print(tmp)
                #print(tmp, file=fi)
                trans_words.append(tmp)
    else:
        print("HI")
        
test_list.append(trans_words)
print(test_list, file=fi)
fi.close()
