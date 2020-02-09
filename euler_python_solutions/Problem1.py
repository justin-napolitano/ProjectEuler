def listOfMultiples(n):
    i = 0
    listOfMultiples = []
    while i < n:
        if i % 3 == 0:
            listOfMultiples.append(i)
        elif i % 5 == 0:
            listOfMultiples.append(i)
        i +=1
    return listOfMultiples
def sumOfMultiples(lst):
    total = 0
    for number in lst:
        total = total + number
    return total

test = listOfMultiples(1000)
total = sumOfMultiples(test)
print(total)
