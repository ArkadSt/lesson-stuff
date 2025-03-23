def fun(a,b):
	print (f"Tervist fun funktsioonist! Antud parameetrid on {a} ja {b}")

fun(1,2)

def viis():
	return 5

a = viis()
print(a) # 5

def sum(a,b):
    # liida a ja b
	return a + b

def sub(a,b):
	return a-b

def div(a,b):
	return a/b

def mult(a,b):
	# korruta a ja b
	return a*b

# 5-2
sum(5, -2)

# print((2+1)*2) # 6
print(mult(sum(2,1),2)) # 6

