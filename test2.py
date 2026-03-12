def square(y):
	print("{} 的平方為 {}".format(y, y*y)) 

x = int(input("請輸入一個正整數："))
#x += 10
	#print("您輸入的值+10的結果是:",x)

if (x<=0):
	print(f"您輸入的數字是{x},小於等於0")
else:
	print(f"您輸入的數字是{x},大於0")
	for i in range(x):
		#print(i,end=";")
		square(i)
		