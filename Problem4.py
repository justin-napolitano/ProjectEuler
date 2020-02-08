#Project Euler Problem4


#Create two lists up to 999
#multiply each number by the other
#check if a palindrome
#if so save as largest palindrome yet



#palindromes = []
largest = 0
largestfactor1 = 0
largestfactor2 = 0

for number in range(1000):
    factor1 = number
    for number2 in range(1000):
        factor2 = number2
        test = factor1 * factor2
        if test == int(str(test)[::-1]) and test != 0 and test > largest:
            #palindromes.append(test)
            largest = test
            largestfactor1 = factor1
            largestfactor2 = factor2

#for palindrome in palindromes:
#    if palindrome > largest:
#        largest = palindrome
print (largest)
print (largestfactor1)
print (largestfactor2)
print (largestfactor1 * largestfactor2)
