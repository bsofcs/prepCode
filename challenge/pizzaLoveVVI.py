"""
pizzaLoveVVI
"""
def maxPizza( n, arr):

    incl = 0

    excl = 0

     
    for i in a:
	 
        new_excl = excl if excl>incl else incl
	 
        incl = excl + i
	 
        excl = new_excl
 
    return (excl if excl>incl else incl) 