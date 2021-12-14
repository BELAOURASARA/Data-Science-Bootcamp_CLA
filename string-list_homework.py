
#Create a list that contains all the even numbers between 1 and 299.
listOfNumbers=[i for i in range(1,300)]
listEvenNumbers=[]

for x in listOfNumbers:
    if x % 2==0 :
        listEvenNumbers.append(x)

print(listEvenNumbers)

#Iterate through the previously created list and print first the length of the list then all the squared values of the list.
print(len(listEvenNumbers))
for x in listEvenNumbers:
    print(x**2)

#In one line check if 57 is in the list using one line of python.
print("is 57 in the list ? :", 57 in listEvenNumbers)