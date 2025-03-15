# a, b = input().split(' ')
# print(a, b)

# def testing():
#     return 5


# 5! = 5*4*3*2*1
# 5! = 5*4*3*2*1*1
# 0! = 1



def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
def add(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + add(numbers[1:])


print(fact(5)) # 120
print(fact(6))
print(fact(1000))
print(add([5,5,4,2])) # 16

# [5,5,4,2]
# 5 + 5 + 4 + 2 + 0