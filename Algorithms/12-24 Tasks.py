"""
12.	Ask for the total price of the bill, then ask how many diners there are. Divide the total
bill by the number of diners and show how much each person must pay
"""

i = int(input("What's price of the bill?  "))
j = int(input("How many diners there are?  "))
each_price = i / j
print("Each diners is owes this amout " + str(each_price))

"""
13.	Write a program that will ask for a number of days and then will show how many hours, 
minutes and seconds are in that number of days.
"""

i = int(input("How many a number of days?  "))
hours = (i * 24)
miutes = hours * 60
seconds = miutes * 60
print("Your numbers of days includ: " + str(hours) + " hours " + "or " + str(miutes) + " minutes " + "or " + str(seconds)+" seconds.")

"""
14.	Task the user to enter a number over 100 and then enter a number under 10 and tell 
them how many times the smaller number goes into the larger number in a user-friendly format.
"""

i = int(input("Can you enter a number over 100?  "))
j = int(input("Ok. Now could you enter a number under 10?  "))
result = i / j
print("Your second number is smaller than first in  " + str(result) + " times!")

"""
15.	Ask the integer number and return the second power of this number.
"""

i = int(input("Can you give me a integer number? "))
result = i ** 2
print("The second power of this number is: " + str(result) + ".")

"""
16.	Ask the integer number and power what you would like to get. Return result
"""

i = int(input("Can you give me a integer number? "))
j = i * 6
result = j
print("Your result is: " + str(result) + ".")

"""
17.	Ask the user to enter their first name and then display the length of their name. 
"""

i = input("Could you say me your first name? ")
result = len(i)
print("Your name has " + str(result) + " letters.")

"""
18.	Ask the user to enter their first name and then ask them to enter their surname. 
Join them together with a space between and display the name and the length of the whole name. 
"""

i = input("Could you say me your first name? ")
p = input("Could you say me your last name? ")
result = len(i) + len(p)
print("Your full name is: " + i + " " + p + " and it has " + str(result) + " letters.")

"""
19.	Ask the user to enter their first name and surname in lower case.
 Change the case to title case and join them together. Display the finished result.
"""

i = input("Could you print your first name in lower case?  ")
p = input("Could you print your last name in lower case?  ")
full_name = i.capitalize() + " " + p.capitalize()
print(full_name)

"""
20.	Enter a random string, which includes only digits.
 Write a function sum_digits which will find a sum of digits in this string
"""
k = input("Type ane digits: ")
sum_digits = 0
for i in k:
    sum_digits += int(i)
print("Your sum of the numbers is " + str(sum_digits))

"""
21.	Ask the user to enter their favorite color. If they enter “red”, “RED” 
or “Red” display the message “I like red too”, otherwise display the message “I don’t like [color], I prefer red”. 
"""

i = input("What's your favorit color? ")
if i == "red" and "RED" and "Red":
    print("I like red too")
else:
    print("I don’t like " + i + "," + " I prefer red")

"""
22.	Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, 
display the message “You can learn to drive”, if they are 16, display the message “You can buy a lottery ticket”,
if they are under 16, display the message “You can go Trickor-Treating”.  
"""

i = int(input("What's your age? "))
if i >= 18:
    print("You can vote")
elif i == 17:
    print("You can learn to drive")
elif i == 16:
    print("You can buy a lottery ticket")
else:
    print("You can go Trickor-Treating")

