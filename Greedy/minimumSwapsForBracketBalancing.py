"""
minimumSwapsForBracketBalancing
"""

def minimumSwapsForBracketBalancing(strng):
	if strng is None:
		return None
	n=len(strng)
	countLeft=0
	countRight=0
	swap=0
	imbalance=0
	for i in range(n):
		if strng[i]=="[":
			countLeft+=1
			if imbalance>0:
				swap+=imbalance
				imbalance-=1
		elif strng[i]=="]":
			countRight+=1
			imbalance=(countRight-countLeft)
	return swap

s=["[]][][","[[][]]"]
for strng in s:
	print(strng,minimumSwapsForBracketBalancing(strng))