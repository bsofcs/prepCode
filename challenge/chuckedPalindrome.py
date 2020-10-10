"""
chuckedPalindrome
for example:

input: geeksforgeeks	#is not a palindrome
output: 3
but (geeks)(for)(geeks) is and the number of words formed is 3

input: merchant
output:1 (merchant)
"""
def chuckedPalindrome(str,count=0):
	if str is None:
		return 0
	n=len(str)
	if n<=1:
		return count+1
	i,j=0,n-1
	for i in range(n//2):
		j=n-1-i
		print(str[:i+1],str[i+1:j],str[j:],count)
		if str[:i+1]==str[j:]:
			return 2+chuckedPalindrome(str[i+1:j],count+2)
	return 1

s=["geeksforgeeks","ghiabcdefhelloadamhelloabcdefghi","merchant","antaprezatepzapreanta","v","volvo","volvov"]
for str in s:
	print(str,":",chuckedPalindrome(str))