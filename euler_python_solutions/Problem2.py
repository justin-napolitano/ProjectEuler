FibArray = [0,1]
FibEvenArray = [0]
def fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n<=len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = fibonacci(n-1)+fibonacci(n-2)
        if temp_fib % 2 == 0:
            FibEvenArray.append(temp_fib)
        FibArray.append(temp_fib)
        return temp_fib

def even =
def sumOfevenTerms():
    total = 0
    for item in FibEvenArray:
        total = total + item
    return total


print FibEvenArray
total = sumOfevenTerms()
print total
