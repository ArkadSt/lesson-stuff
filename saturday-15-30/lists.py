
def fun1():
    a = ["1","2","3","4"]

    b = [int(i) for i in a]

    c = list(map(int, a))

    # for element in a:
    #     b.append(element*2)

    print(a)
    print(b)
    print(c)

def fun2():
    a = list(range(1,11))#[i for i in range(1,11)]
    b = [i for i in a if i % 2 == 0]
    # for i in a:
    #     if i % 2 == 0:
    #         b.append(i)
    print(a)
    print(b)

def fun3():
    a = list(range(1,11))
    b = [str(i) for i in a if i % 3 == 0]
    print(b) # ['3', '6', '9']

def fun4():
    a = ["apple", "pear", "cherry"]
    b = [i[0] for i in a]
    print(b) # ['a', 'p', 'c']

def fun5():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = ...
    print(b) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

def fun6():
    a = ["apple", "pear", "cherry"]
    b = [len(i) for i in a]
    print(b) # [5, 4, 6]

def fun7():
    a = [1,2,3,4,5]
    b = {i: i*2 for i in a}
    print(b) # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

def fun8():
    a = ["apple", "pear", "cherry"]
    b = {...}
    print(b) # {"apple": 5, "pear": 4, "cherry": 6}

def fun9():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = ...
    print(b) # [2, 4, 6, 8]

def fun10():
    a = ["apple", "banana", "cherry"]
    b = ["Mark", "Marek", "Kristjan"]
    c = ...
    print(c) # [("apple", "Mark"), ("banana", "Marek"), ("cherry", "Kristjan")]

# a = [1,2,3,4]
# for i in range(len(a)):
#     print(a[i])


# Я люблю яблоки и яблоки любят меня
#
# Я: 1
# люблю: 1
# яблоки: 2
# и: 1
# любят: 1
# меня : 1

def fun11():
    a = {"apple": 5, "pear": 4, "cherry": 6}
    b = {a[i]:i for i in a}
    print(b) # {5: "apple", 4: "pear", 6: "cherry"}

def fun0():
    a = [1,2,3,4,5]
    for i in a:
        print(i)


fun7()