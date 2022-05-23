#characterCounterSpecial
#Write a solution to find the character that has the highest number of occurrences within a certain string, ignoring
#case. If there is more than one character with equal highest occurrences, return the character that appeared first
#within the string.
from collections import Counter
def findMaxOccurenceCharacter(n):
    if n is None:
        return None
    c=Counter(n.upper())
    dict={}
    mx=max(c.values())
    #print(c,mx)
    for i in n.upper():
        if c[i]==mx:
            return(i)

if __name__=="__main__":
    n="Character Assassination"
    print("The character with most occurence:",findMaxOccurenceCharacter(n))