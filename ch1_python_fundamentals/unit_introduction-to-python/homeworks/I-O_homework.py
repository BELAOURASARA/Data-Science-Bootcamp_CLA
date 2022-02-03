
#read the information from a file
file=open('.\inputs\student_names.txt')
students=file.read()
print(students)





#write in a file some random names
import names #this module is for random names generation

max_names=10 #fix the number of names that we would generate
randomNames=""
for i in range(max_names):
    name=names.get_full_name()+"\n"
    randomNames=randomNames+name

file=open('.\inputs\student_names.txt','w')
file.write(randomNames)
file.close()



#read the n first lines from the file
n=3
file=open('.\inputs\student_names.txt','r')
for j in range(n):
    print(next(file).strip())



#read the n last lines from the file
for line in (file.readlines() [-n:]):
    print(line, end ='')





#check if a name x is in the file
x="Doris Finch\n"
file=open('.\inputs\student_names.txt','r')
isInFile=False
for line in (file.readlines()):
    if line==x:
        isInFile=True
        print("the name :"+x+" exists in this file")
        break
if isInFile==False:
    print("the name :"+x+" doesn't exist in this file")





#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
path=".\output\\"
j=65
for i in range(26):
    filename=path+chr(j)+".txt"
    file=open(filename,'w')
    file.close()
    j+=1
  
    