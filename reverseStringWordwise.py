"""
reverseStringWordwise.py
Input: "The Monk who sold his Ferrai"
Output:"Ferrai his sold who Monk The"
"""
def reverse_words_in_sentence(arr):
 lst_arr=arr.split(" ")
 return(" ".join(lst_arr[::-1]))
 

arr="The Monk who sold his Ferrai"
print(reverse_words_in_sentence(arr))