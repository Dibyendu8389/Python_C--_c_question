#Question: What are control statements in Python?
#control statement in python means flow or structure of the data control step by differnet comend .
'''
if True:
    print("This runs")
'''


#Question: Write a program to check if a number is positive or negative.
'''
x = (int(input("Enter a number:" )))
if x > 0:
    print(True)
else :
    print(False)
'''


#Question: Write a program to print numbers from 1 to 5 using a "for" loop.
'''
for i in range (1,6):
    print (i)
'''


#Question: Write a program to find the largest of three numbers using if-elif-else.
'''
a = (input("Enter a number for first:" ))
b = (input("Enter a number for second:" ))
c = (input("Enter a number for theird:" ))
if a>b and a>c:
    print("a is largest number",a)
elif b>c:
    print("b is largest number",b)
else:
    print("c is largest number",c)

'''


#Question: Write a program to print even numbers between 1 and 10 using a while loop.
'''
i=1
while i<=10:
    if i % 2 ==0:
        print(i)
    i+=1

'''

'''
#Question: Write a program to check whether a given year is a leap year or not.

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

'''

#Question: Write a program that stops printing numbers when it reaches 5 using break.
'''
for i in range (1,11):
    if i == 6:
        break
    print(i)

'''


#Question: Write a program that skips printing number 5 using continue.
'''
for i in range (1,11):
    if i == 5:
        continue
    print(i)
'''


#Question: Write a program that uses pass in a loop (to be filled later).

for i in range(1, 6):
    if i == 3:
        pass   # Placeholder for future code
    print("Number:", i)
