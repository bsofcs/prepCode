#reduceArraySizeToTheHalf.py
def minSetSize(arr):
    if arr is None:
        return None
    total=len(arr)
    s=dict()
    for i in arr:
        if i in s:
            s[i]+=1
        else:
            s[i]=1
    freq=sorted([s[i] for i in s.keys()],reverse=True)
    print("Freq:",freq)
    i=0
    count=0
    result=0
    while i<=len(freq):
        if result+freq[i]>=total//2:
            return count
        count+=1
        result+=freq[i]
        i+=1


if __name__=='__main__':
    arr = [3,3,3,3,5,5,5,2,2,7]
    print(arr,minSetSize(arr))
    arr = [1,9]
    print(arr,minSetSize(arr))
    arr = [1000,1000,3,7]
    print(arr,minSetSize(arr))
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(arr,minSetSize(arr))
    arr = [7,7,7,7,7,7]
    print(arr,minSetSize(arr))
    