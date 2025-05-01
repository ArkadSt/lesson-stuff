
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

def fun0():
    a = [1,2,3,4,5]
    for i in a:
        print(i)


fun7()