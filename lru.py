"""
least recent used memory management
"""
def lru(pages,n,capacity):
	if pages is None or n is None or capacity is None:
		return None
	result=0
	cache={}
	for i in range(n):
		if pages[i] in cache:
			cache.pop(pages[i])
			cache[pages[i]]=i
		elif len(cache)<capacity:
			cache[pages[i]]=i
			result+=1
		else:
			item=min(sorted(cache.values()))
			pg=-1
			for key,val in cache.items():
				if val==item:
					pg=key
					break
			cache.pop(pg)
			cache[pages[i]]=i
			result+=1
	return result
		

if __name__=='__main__':
	t=int(input())
	for i in range(t):
		n=int(input())
		i_p=input()
		pages=[int(i) for i in i_p.split()]
		capacity=int(input())
		result=lru(pages,n,capacity)
		print(result)