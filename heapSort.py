#heapSort.py
class heap:
    def heapify(self,arr,n,i):
        if arr is None:
            return None
        print(arr,i,arr[i])
        largest=i
        l=2*i+1
        r=2*i+2
        if l<n and arr[i]<arr[l]:
            largest=l
        if r<n and arr[largest]<arr[r]:
            largest=r
        if largest != i:
            arr[i],arr[largest]=arr[largest],arr[i]
            self.heapify(arr,n,largest)
        
    def heapSort(self, arr):
        if arr is None:
            return 
        n=len(arr)
        for i in range(n//2 -1, -1,-1):
            self.heapify(arr,n,i)
        print("intermediate:",arr)
        for i in range(n-1,0,-1):
            arr[i],arr[0]=arr[0],arr[i]
            self.heapify(arr,i,0)

arr=[12, 11, 13, 5, 6, 7]
h=heap()
h.heapSort(arr)
print(arr)