import hashlib
"""
bloomFilter.py
"""
class BloomFilter:
 def __init__(self,m,k,hashFun):
  self.m=m
  self.vector=[0]*m
  self.k=k
  self.hashFun=hashFun
  self.data={}
  self.flasePositive=0

 def insert(self,key,value):
  self.data[key]=value
  for i in range(self.k):
   self.vector[self.hashFun(key+str(i))%self.m]=1

 def contains(self,key):
  for i in range(self.k):
   if self.vector[self.hashFun(key+str(i))%self.m]==0:
    return False
  return True

 def get(self,key):
  if self.contains(key):
   try:
    return(self.data[key])
   except KeyError:
    self.falsePositive+=1

def hash_function(x):
 h=hashlib.sha256(x.encode('utf-8'))
 return(int(h.hexdigest(),base=16))

b=BloomFilter(100,10,hash_function)
b.insert("this is a test key","this is a new value")
print(b.get("this is a key"))
print(b.get("this is a test key"))

a="this is a key"
print("\n\nTry:\n",a,"\n",a.encode('utf-8'))