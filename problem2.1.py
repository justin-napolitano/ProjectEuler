FibArray = [0,1]

def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n<=len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        if temp_fib <= 4000000:
            FibArray.append(temp_fib)
        return temp_fib



def EvenFibs():
    fibEvens = [0]
    for item in FibArray:
        if item % 2 == 0:
            fibEvens.append(item)
    return fibEvens

def summation(lst):
    total = 0
    for item in lst:
        total = total + item
    return total

print(fibonacci(9))

final = summation(EvenFibs())

print(final)
