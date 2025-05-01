                                                             #___________Basic Input/Output____________#

# WAP to print "hello world"
print("Hello World")

# WAP to take two integers as input and print their sum
a=10
b=20
c=a+b
print(c)

# WAP to calculate the area of a rectangle.
base=20
height=30
area=1/2*base*height
print(area)

# WAP to check if a number is even or odd.
n=int(input("enter the number: "))
if (n/2==0):
    print("even")
else:
    print("odd")

# WAP to take a string as input and print it is reverse order.
string = input("Enter A String : ")
print(string[::-1])

# WAP to convert temperature from Celsius to Fahrenheit.
celsius = float( input("Enter Temperature in Celsius : ") )
fahrenheit = (celsius*9/5)+32
print("Fahrenheit : ",fahrenheit)

#WAP to take a list of numbers and print their sum.
n=[1,2,3,4,5]
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)

# WAP to swap two variables without using a temporary variable.
a = int( input("Enter A Number : ") )
b = int( input("Enter B Number : ") )
a = a+b
b = a-b
a = a-b
print("A = ",a)
print("B = ",b)

# WAP to find the length of a string.
string = input("Enter A String : ")
print("Length of String is : ",len(string))

                                                                               #________IF_ELSE_LOOPS_________#

# WAP to check whether a number is positive,negative,or zero.
n=int(input("enter the number: "))
if (n>0):
    print("positive")
elif (n<0):
    print("negative")
else:
    print("zero")

# WAP to find the largest among three number
a = int( input("Enter A Number : ") )
b = int( input("Enter B Number : ") )
c = int( input("Enter C Number : ") )
if( (a>b) and (a>c) ):
    print(a," is Greater!")
elif( (b>a) and (b>c) ):
    print(b," is Greater!")
else:
    print(c," is Greater!")

# WAP to print all prime numbers between 1 and 100.
for i in range(2,101):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count=count+1
            break
    if(count==0):
        print(i)
        
# WAP to calculate the factorial of a number.
num = int( input("Enter A Number : ") )
fact = 1
for i in range(1,num+1):
    fact=fact*i
print("Factorial : ",fact)

# WAP to print the Fibonacci sequence up to n terms.
a = 0 
b = 1
n = int( input("Enter Range : ") )
for i in range(n):
    c = a+b
    print(c,end=" ")
    a = b
    b = c
# WAP to check if a year is a leap year.
year = int( input("Enter Year : ") )
if(year%4==0):
    print("It's A Leap Year")
else:
    print("It's not A Leap Year")

# WAP to find the greatest common divisor (GCD) of two numbers.
num1 = int( input("Enter A Number : ") )
num2 = int( input("Enter B Number : ") )
gcd = 1
for i in range(1,num1+1):
    if( (num1%i==0) and (num2%i==0) ):
        gcd = i
print("GCD/HCF : ",gcd)

# WAP to print the sum of all numbers in a given range.
start = int( input("Enter Start Range : ") )
end = int( input("Enter End Range : ") )
add = 0
for i in range(start,end+1):
    add=add+i
print("Sum of All Natural Number : ",add)

# WAP to find whether a given number is Armstrong or not.
# if you have a number 153, 
# And you want to add the cube root of every digit like,
# Then it will again come the same number
# 1^3+5^3+3^3 == 153
# So, 153 is an Armstrong Number

num = int( input("Enter A Number : ") )
temp = num
total = 0
while(num>0):
    rem = num%10
    total = total+rem*rem*rem
    num = int(num/10)
if(temp==total):
    print("Number is Armstrong")
else:
    print("Number is Not Armstrong")

# WAP to print all even numbers between 1 and 50.
print("All Even Numbers From 1 to 50")
for i in range(1,51):
    if(i%2==0):
        print(i,end=" ")

                                                              #_______________LISTS AND TUPLES__________________#

# WAP to find the max and min number in a list.
list1=[3,4,5,2,5,6,78,56,99,345,343]
min = list1[0]
max = list1[0]
for i in list1:
    if(i<min):
        min=i
    if(i>max):
        max=i
print(list1)
print("min val: ",min)
print("max val: ",max)

# WAP to reverse a list.
list1=[2,3,4,5,6,7,8]
print(list1)
list1.reverse()
print(list1)

# WAP to find the sum of all elements in a list.
list1=[2,34,5,6,7]
sum=0
for i in list1:
    sum= sum+i
print(list1)
print(sum)

# WAP to count the number of occurrences of an element in a list.
list1=[2,3,4,5,6,7,8,9,3,4,2,5,7,8,9,5,4,3,2]
print(list1)
num=int(input("Enter Element To Find Occurence: "))
count=0
for i in list1:
    if(i==num):
        count=count+1
print("Occurence: ",count)

# WAP to merge two lists into a single list.
list1 = [2,3,4,5,6,7,8,3]
list2 = [4,2,6,8,6,4,3,6]
list3 = list1+list2
print("List1 : ",list1)
print("List2 : ",list2)
print("Merged List : ",list3)

# WAP to remove deplicates from a list.
list1=[2,2,3,4,5,6,7,6,5,4,3,5,6,4,3,2,4,6,7,4,3,2,2,2]
print(list1)
list1=list(set(list1))
print(list1)

# WAP to find the second largest number in a list.
li1=[2,34,32,2,45,3,55,67,54]
print(li1)
if(len(li1)>1):
    li1.sort(reverse=True)
    print("second largest value: ",li1[1])
else:
    print("list has less than 2 elements only!")

# WAP to check if an element exists in a list.
list1 = [ 32,5,78,6,4,32,43,65,78,67,34,23,45 ]
print("List : ",list1)
num = int( input("Enter A Number : ") )
if(num in list1):
    print("Item Exists!")
else:
    print("Item is not exist in List!")

# WAP to find the intersection of two lists.
# HINT : common elements in both List
li1=[2,4,5,6,5,4,3,4,3,6,7,8,6,5]
li2=[9,7,8,7,6,7,5,4,4,3,2,5,6,6]
print("list1: ",li1)
print("list2: ",li2)
list3=[ ]
for i in li1:
    for j in li2:
        if(i==j):
            list3.append(j)
            li2.remove(j)
            break
print("list3: ",list3)

# WAP to convert a list of tuples into a dictionary.
list1 = [ ('a',23),('b',35),('c',35),('d',67),('e',36) ]
dict1 = dict(list1)
print("List1 : ",list1)
print("Dictionary : ",dict1)

                                                                                           #_________STRING_____________#

# WAP to count the number of vowels in a string.
str1 = input("Enter A String/Sentence : ")
print("Your String : ",str1)
count = 0
for i in str1:
    if(i in "aeiouAEIOU"):
        count=count+1
print("Occurences of Vowel is : ",count)

# WAP to check if a string is a palindrome.
# HINT : An Sgring is Palindrome if any string is same if it is in its reverse form
# Example : MADAM , MADAM (Reverse) (Palindrome)
# Example : MOHAN , NAHOM (Reverse) (Not Palindrome)
str1 = input("Enter A String : ")
start = 0
end = len(str1)-1
flag = 1
while(start<end):
    if(str1[start]!=str1[end]):
        flag = 0
        break
    start=start+1
    end=end-1
if(flag==1):
    print("It's A Palindrome String!")
else:
    print("It's Not A Palindrome String!")

# WAP to find the frequency of characters in a string.
str1 = "aman is my best friend forever"
print("String : ",str1)
tempList = [ ]
for i in list(str1):
    if(i != " "):
        if i not in tempList:
            print("Occurency of ",i," is : ",str1.count(i))
            tempList.append(i)

# WAP to remove all spaces from a string.
str1 = "We Are Learning Python"
print("String : ",str1)
strList = str1.split(" ")
str2 = ""
for i in strList:
    str2=str2+i
print("Removed All Spaces : ",str2)

# WAP to check if two strings are anagrams.
# HINT : If all the characters are same in both string even occurency.
# so, pair of this strings are Anagram
str1 = "LISTEN"
str2 = "SILENT"
list1 = list(str1)
list2 = list(str2)
if(len(list1)==len(list2)):
    count = 0
    for i in list1:
        if(i in list2):
            count=count+1
            list2.remove(i)
    if(count==len(list1)):
        print("Strings Are Anagram!")
    else:
        print("Strings Are Not Anagram!")
else:
    print("Strings Are Not Anagram!")

# WAP to capitalize the first letter of each word in a string.
str1 = "we are learning python programming"
print("String : ",str1)
strList = str1.split(" ")
str2 = ""
for i in strList:
    str2=str2+i[0].upper()+i[1:]+" "
print("New String : ",str2)

# WAP to reverse the words in a given sentence.
str1 = "We Are Leaning Python Programming"
print("String : ",str1)
strList = str1.split(" ")
revStr = ""
for i in strList:
    i=list(i)
    i.reverse()
    for j in i:
        revStr = revStr+j
    revStr=revStr+" "
print("Reversed String : ",revStr)

# WAP to find the longest word in a sentence.
str1 = "We Are Learning Programming in Python"
print("String : ",str1)
strList = str1.split(" ")
maxStr = ""
for i in strList:
    if(len(maxStr)<len(i)):
        maxStr=i
print("Longest String : ",maxStr)

# WAP to replace all occurrences of a substring in a string.
str1 = "Hello India Hello World!"
print("String : ",str1)
str2 = str1.replace("Hello","Namaste")
print("New String : ",str2)

# WAP to count the number of words in a string.
str1 = "We Are Learning Python Programming"
strList = str1.split(" ")
print("String : ",str1)
print("Number of Words in String : ",len(strList))

                                                                        #______________FUNCTION__________________#

# WAF to check if a number is prime.
def Prime(num):
    for i in range(2,int(num/2)):
        if(num/i==0):
            return False
        return True
num = int(input("Enter A Number: "))
if(Prime(num)):
    print("number is prime!")
else:
    print("number is not prime!")

# WAF to calculate the sum of all elements in a list.
def SumOfList(li1):
    total = 0
    for i in li1:
        total = total+i
    return total
li1=[23,4,67,34,3,3]
print("list: ",li1)
print("Sum Of All Elements: ",SumOfList(li1))

# WAF that returns the factorial of a number.
def findfact(num):
    fact=1
    for i in range(2,num+1):
        fact=fact*i
    return fact
num= int(input("enter a number: "))
print("Factorial: ",findfact(num))

# WAF to find the max of three numbers.
def findlargest(tuple1):
    return max(tuple1)
num1=int(input("enter a number: "))
num2=int(input("enter b number: "))
num3=int(input("enter c number"))
print("_____________largest value: ",findlargest((num1,num2,num3)))

#WAF to reverse a string.
def reversestring(str1):
    revstr=""
    for i in range(len(str1),0,-1):
        revstr=revstr+str1[i-1]
    return revstr
str1=input("enter a string: ")
print("reverse string: ",reversestring(str1))

# WAF to check if a number is a perfect square.
def checkperfectsquare(num):
    a=1
    while(a*a<=num):
        if(a*a==num):
            return True
        a=a+1
    return False
num= int(input("enter a number: "))
if(checkperfectsquare(num)):
    print("it is a perfect square number!")
else:
    print("it is not a perfect square number!")

# WAF that returns the greatest common divisor (GCD) of two numbers.
def findGCD(num1,num2):
    a = 1
    gcd = a
    while(a<=num1):
        if( num1%a==0 and num2%a==0 ):
            gcd=a
        a=a+1
    return gcd
num1 = int(input("Enter A Number : "))
num2 = int(input("Enter B Number : "))
print("GCD : ",findGCD(num1,num2))

# WAF to check if a number is a palindrome.
# HINT:-  if you reverse a number so, if new number is exactly matched 
# with old one is Palindrome.
def findReverse(num):
    rev = 0
    while(num>0):
        rem = num%10
        rev = rev*10+rem
        num=int(num/10)
    return rev
num = int(input("Enter A Number : "))
if(num==findReverse(num)):
    print("Number is Palindrome!")
else:
    print("Number is Not Palindrome!")


# WAF to convert a decimal number to binary.
def convertToBinary(num):
    binary = ""
    while(num>0):
        rem = num%2
        binary = str(rem)+binary
        num=int(num/2)
    return binary
num = int(input("Enter A Decimal Number : "))
print("Binary Number : ",convertToBinary(num))

# WAF that accepts a list and returns a new list with unique elements.
def findUnique(list1):
    return list(set(list1))
list1 = [2,5,3,7,8,5,9,7,6,9]
print("List : ",list1)
print("Unique List : ",findUnique(list1))

                                                             #__________________DICTIONARIES___________________#

# WAP to create a dictionary from two lists.
li1=['A','B','C','D','E','F']
li2=[23,32,45,67,54,34]
dic=dict()
for i in range (0,len(li1)):
    dic.update({li1[i]:li2[i]})
print(dic)

# WAP to merge two dictionaries.
dic1={'A':34,'B':46,'C':36}
dic2={'D':37,'E':76}
dic1.update(dic2)
print(dic1)

# WAP to get the keys of a dictionary.
dic={'A':46,'B':89,'C':37,'D':26}
for keys in dic.keys():
    print(keys,end=' ')

# WAP to get the values of a dictionary.
dic = {'A':46,'B':89,'C':37,'D':26}
for keys in dic.values():
    print(keys,end=" ")

# WAP to check if a key exists in a dictionary.
dic={'A':46,'B':67,'C':75,'D':84}
key=input("enter any key to find: ")
if(dic.get(key)!=None):
    print("Found!")
else:
    print("Not Found!")

# WAP to update the value of a key in a dictionary.
dic = {'A':46,'B':89,'C':37,'D':26}
print("Your Dic : ",dic)
key = input("Enter Any Key To Find : ")
if(dic.get(key)!=None):
    value = input("Enter Value To Update : ")
    dic.update({key:value})
    print("Your Updated Dic : ",dic)
else:
    print("Key Not Found!")

# WAP to remove a key from a dictionary.
dic = {'A':46,'B':89,'C':37,'D':26}
print("Your Dic : ",dic)
key = input("Enter Any Key To Delete : ")
if(dic.get(key)!=None):
    del dic[key]
    print("Your Updated Dic : ",dic)
else:
    print("Key Not Found!")

                                                                             #__________________SETS___________________#

#WAP to create a set and add elements to it.
s={"mukul","ritika","atul","priyanshu"}
print(s)
s.add("prateek")
s.add("arjun")
s.add("vikas")
print("\nUpdated set= ",s)

#WAP to find the union of two sets.
s1={1,2,3,4,5}
s2={4,5,6,7}
print(s1|s2)

#WAP to find the intersection of two sets.
s1={1,2,3,4,5}
s2={4,5,6,7}
print(s1&s2)

#WAP to find the difference between two sets.
s1={1,2,3,4,5}
s2={4,5,6,7}
print(s1-s2)
print(s2-s1)

#WAP to check if a set is a subset of another set.
s1={1,2,3,4,5}
s2={4,5,6,7}
print(s1.issubset(s2))

#WAP to remove an element from a set.
s={"mukul",1,"mukku",2,3,4,"don"}
print(s)
s.remove("mukku")
print(s)

#WAP to check if an elements exists in a set.
s={'arjun', 'prateek', 'ritika', 'atul', 'vikas', 'priyanshu', 'mukul'}
value=chr("enter the sets: ")
if(s.get(value)!=None):
    print("found!")
else:
    print("not found!")

#WAP to convert a list into a set.
li=[1,2,4,56,78,65,44]
print(set(li))

#WAP to clear all elements from a set.
s1={'arjun', 'prateek', 'ritika', 'atul', 'vikas', 'priyanshu', 'mukul'}
print(s1)
s1.clear()
print(s1)

#WAP to find the symmetric diff between two sets.
s1={'arjun', 'prateek', 'ritika', 'atul', 'vikas', 'priyanshu', 'mukul'}
s2={"mukul",1,"mukku",2,3,4,"don"}
s1.symmetric_difference_update(s2)
print(s1)

                                                                    #___________________FILE_HANDLING_________________#

#WAP to open a file and read its contents.
file=open("file.txt","r")
data=file.read()
print(data)
file.close()

#WAP to count the number of lines in a text file.
file=open("temp.txt","a")
file.write("data science and machine learning")
file.close()

file=open("temp.txt","r")
data=file.readlines()
print("Total Lines in This Text File: ",len(data))
file.close()

#WAP to append text to a file
file=open("temp.txt","a")
file.write("\nThis text is append by question on 53\n")
print("Text Append Successfully!")
file.close()

# Write a Python program to read a file line by line.
file = open("temp.txt","r")
for line in file.readlines():
    print(line)
file.close()

# Write a program to copy the contents of one file to another.
file1 = open("temp.txt","r")
file2 = open("copy.txt","w")
data = file1.read()
file2.write(data)
print("Content Copied Successfully!")
file1.close()
file2.close()

#Write a program to write a list of numbers to a text file.
file=open("43.txt","w")
st=""
for a in range(1,101):
    st=st+str(a)+"\n"
    file.write(st)
    print("fille written successfully!")
file.close()    

file=open("43.txt","r")
print(file.read(file))
file.close()

# Write a Python program to read a CSV file.
file = open("58.csv","w")
data = file.write("my world")
print(data)
file.close()

file = open("58.csv","r")
data = file.read()
print(data)
file.close()

                                                #______________LAMBDA | MAP | FILTER | REDUCE_____________#

cube=lambda n:n*n*n
print(cube(6))

add=lambda a,b:a+b

print(add(100,20))

#MAP
li=[x for x in range(1,11)]

li=list(map(lambda x:x*x,li))
print(li)

# WAP to find factorial of all numbers of a list.
li=[1,2,3,4,5]
def fact(num):
    f=1
    if num!=0:
        for i in range(1,num+1):
            f=f*i
        return f
    else:
        return 1
li=list(map(fact,li))
print(li)
            
# filter

li= [x for x in range (1,31)]

li=list(filter(lambda n: n%2==0,li))
print(li)

#WAP to find only palondrome string using filter
li=["RAM","NAMAN","MADAN","RIYA","ANU","MAM","SIYA"]
li=list(filter(lambda n: n==n[::-1],li))
print(li)    

# reduce

from functools import reduce

li=[x for x in range (1,101)]

s=reduce(lambda a,b: a+b, li)
print(s)

                                                                      #___________ERROR_HANDLING____________#

# WAP to handle division by zero.
a=34
b=30
try:
    result=a/b
except ZeroDivisionError:
    result='undefined'
print(result)

# WAP that raises an exception if the input is not a number.
while True:
    try:
        a=int(input("input a number: "))
        break
    except ValueError:
        print("this is not a number.Try Again...")

# WAP to catch multiple exception.
print("NameError: 1")
print("TypeError: 2")
print("ZeroDivisionError: 3")
ch=int(input("enter your choice: "))
try:
    if ch==1:
        print(num)
    elif ch==2:
        x="ABC" + 10
    else:
        x=100/0

except NameError:
    print("A NameError Exception Occurrred!")
except TypeError:
    print("a typeerror exception occurred!")
except ZeroDivisionError:
    print("a zerodivisionerror exception occurred!")

# WAP to handles a type error.
try:
    str1="data science"
    list1=[1,2,3,4]
    print(str1+list1)
except TypeError as e:
    print("The Operand Data Type Need To Be Same\n",e)

#WAP that uses a try-finally block.
try:
    exec(input("Enter code: "))
except ZeroDivisionError:
    print("cannot divided by 0")
except Exception:
    print("Some other error")
else:
    print("code executed successfully")
finally:
    print("this  will always execute")















        
