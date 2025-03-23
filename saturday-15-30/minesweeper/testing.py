# a, b = input().split(' ')
# print(a, b)

# def testing():
#     return 5


# 5! = 5*4*3*2*1
# 5! = 5*4*3*2*1*1
# 0! = 1



# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
    
# def add(numbers):
#     if not numbers:
#         return 0
#     else:
#         return numbers[0] + add(numbers[1:])


# print(fact(5)) # 120
# print(fact(6))
# print(fact(1000))
# print(add([5,5,4,2])) # 16

# [5,5,4,2]
# 5 + 5 + 4 + 2 + 0

def all_r(booleans):
    if not booleans:
        return True

    return booleans[0] and all_r(booleans[1:])


print(all_r([True, True, True, True, True, True, True])) # True
print(all_r([True, True, True, False, True, True, True])) # False

def map_r(func, spisok):
    if len(spisok) == 0:
        return []
    return [func(spisok[0])] + map_r(func, spisok[1:])

# [2] + [3] + [4] + [5] + [6] + []
def inc(a):
    return a+1

a = [1,2,3,4,5]
print(map_r(inc, a))

