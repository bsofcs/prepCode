"""
smallestWindowHavingOneInAnother

Given a string S and text T. Output the smallest window in the string S having all characters of the text T. Both the string S and text T contains lowercase english alphabets
"""
no_of_chars=256
def findSubString(string,pat):
	len1=len(string)
	len2=len(pat)
	if len1<len2:
		print("No such window")
		return None
	
	