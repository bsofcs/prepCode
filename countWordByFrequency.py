#countWordByFrequency
from collections import OrderedDict
f=open("sampleFile.txt","r")
dict={}
for line in f:
    for word in line.split(' '):
        if word.upper() in dict:
            dict[word.upper()]+=1
        else:
            dict[word.upper()]=1
#print(OrderedDict(sorted(dict.items())))
#print(sorted(dict,key=dict.get))
dict_tuples=sorted(dict.items(),key=lambda item: item[1],reverse=True)
print(dict_tuples)