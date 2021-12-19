#a Python function that checks whether a passed string is palindrome or not. A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def isPalindrome(s):
    stringWithoutSpaces=s.replace(" ", "")
    return stringWithoutSpaces == stringWithoutSpaces[::-1]


print(isPalindrome("nurses run"))
print(isPalindrome("Sara"))
#a Python function that takes a number as a parameter and checks if the number is prime or not. A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
def isPrime(number):
    
    if number>1:
        for i in range(2,number//2,1):
            if number%i==0:
                return False
                break
        else:
            return True      
    else:
        return False


print(isPrime(50))
print(isPrime(13))
#a Python function to check whether a number is in a given range.
def isInRange(number,range):
    for i in range:
        if number==i:
            return True
            break
    else:
        return False


range=[1,3,4,6,10]
print(isInRange(16,range))
#a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(number):
    if(number<0):
        print("sorry,factorial doesn't exist for negative integers")
    elif (number==0): return 1
    else:
        fact=1
        for i in range(1,number+1,1):
            fact=fact*i

        return fact


print(factorial(5))
#a Python program to reverse a string.
def reverse(s):
    return s[::-1]


print(reverse("hello"))
#a Python function to sum all the numbers in a list.
def sumList(list):
    sum=0
    for i in list:
        sum=sum+i
    return sum


l=[5,4,8,0,3,11]
print(sumList(l))
#a Python function to find the Max of three numbers.
def maxOfThree(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        max=n1
    elif n2>=n1 and n2>=n3:
        max=n2
    else:
        max=n3

    return max


print(maxOfThree(2,4,3))