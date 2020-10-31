"""
bitMagic
"""
print("1.Bitwise Left Shift: it results to 2^i")
for i in range(4):
	print(i,"(",bin(i).replace("0b",""),"):",1<<i,"(",bin(1<<i).replace("0b",""),")")

print("\n2.Bitwise Left Shift for multiplying a number by power of 2 (ex:3)")
for i in range(4):
	print(i,"(",bin(i).replace("0b",""),"):",3<<i,"(",bin(3<<i).replace("0b",""),")")

print("3.Bitwise Right Shift: it results to 2^-i")
for i in range(4):
	print(i,"(",bin(i).replace("0b",""),"):",8>>i,"(",bin(8>>i).replace("0b",""),")")

print("\n4.Bitwise Left Shift for dividing a number by power of 2 (ex:24)")
for i in range(4):
	print(i,"(",bin(i).replace("0b",""),"):",24>>i,"(",bin(24>>i).replace("0b",""),")")

print("\n5.Bitwise Complement")
for i in range(4):
	print(i,"(",bin(i),"):",~i,"(",bin(~i),")")