def number(num1, num2, num3):
    if (num1 > num2):
        return num1
    elif (num2 > num3):
        return num2
    else:
        return num3
        

print(number(40, 30, 20))

def temp(num):
    if num <= 20:
        return "Cold"
    elif(num >= 21 and num <= 25):
        return "Warm"
    elif(num < 40):
        return "Hot"
    else:
        return "Enjoy"

print(temp(24))

def vowel(ch):
    lst = "AEIOUaeiou"
    if ch in lst:
        return "Yes it is Vowel"
    else:
        return "No it is Consonents"
        
print(vowel("o"))

def case(ch):
    
    if len(ch) == 0:
        return "Please Enter the String"
        
    if ch.isupper():
        return "yes it is Uppercase"
    elif ch.islower():
        return "Yes It is in lower case"
    elif ch.isdigit():
        return "Yes it is a number"
    else:
        return "It is a Special Character"
        
print(case("BHUSHAN"))

def validTriangle(a, b, c):
    if( (a + b <= c) or (a + c <= b) or (b + c <= a)):
        return "Invalid"
    else:
        return "Valid"
        
print(validTriangle(20,10,5))

def validTri(x,y,z):
    if x == y == z:
        return "equilateral"
    elif x == y or y == z or x == z:
        return "Isosceles"
    else:
        return "Scalene"

print(validTri(8,7,9))


def grade(grade):
    if (grade > 90):
        return "A"
    elif(grade >= 75):
        return "B"
    elif(grade >= 65):
        return "C"
    elif(grade >= 35):
        return "D"
    else:
        return "Fail"

def multipleofother(a, b):
    if a % b == 0:
        return "Yes it is multiple of secound number"
    else:
        return "No"

def hoursoftheDay(n):
    if (n > 5 and n < 12):
        return "Good Morning"
    elif (n >= 12 and n <= 15):
        return "Good Afternoon"
    elif (n >= 15 and n <= 22):
        return "Good Evening"
    else:
        return "Good Night"

def votingeligibity(age):
    if age >= 18:
        return "Eligible for Voting"
    else:
        return "Not Eligible for voting"

def evenodd(n1, n2):
    if n1 % 2 == 0 and n2 % 2 == 0:
        return "N1 and N2 is Even Number"
    elif n1 % 2 != 0 and n2 % 2 != 0:
        return "N1 and N2 is Odd Number"
    else:
        return "One number is even and the other is odd"

def alpahbet(ch):
    ch = ch.lower()
    if('a' <= ch <= 'm'):
        return "Yes it's lie between a and m"
    elif('n' <= ch <= 'z'):
        return "Yes it's lie between n and z"

def daynumber(n):
    if n == 1:
        return "Monday"
    elif n == 2:
        return "Tuesday"
    elif n == 3:
        return "Wednesday"
    elif n == 4:
        return "Thursday"
    elif n == 5:
        return "Friday"
    elif n == 6:
        return "Saturday"
    elif n == 7:
        return "Sunday"
    else:
        return "Please Enter the proper Number"

def daynumber1(n):

    lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if 1 <= n <= 7:
        return lst[n - 1]
    else:
        return "Please enter the proper Number"

def monthnumber(n):
    if n in (1, 3, 5, 7, 8, 10, 12):
        return "31 Day"
    elif n in (4, 6, 9, 11):
        return "30 Day"
    elif n == 2:
        return "28 Day"
    else:
        return "Enter the Proper number"

######## Math and Number Logic

def threedigit(n1, n2, n3):
    if(n1 != n2 and n2 != n3 and n1 != n3):
    #if n1 != n2 != n3:
        return "Yes it's distinct"
    else:
        return "It's not ditinct"

def determinedigit(n1, n2, n3):
    a = num // 100        # first digit
    b = (num // 10) % 10  # middle digit
    c = num % 10          # last digit

    if b > a and b > c:
        return "Middle digit is the largest"
    elif b < a and b < c:
        return "Middle digit is the smallest"
    else:
        return "Middle digit is neither largest nor smallest"

def fourdigit(num):
    first = num // 1000
    last = num % 10

    if first == last:
        return "First and last digits are equal"
    else:
        return "First and last digits are NOT equal"

def givenintis(nums):
    n = abs(nums)

    if n < 10:
        return "Singal Digit"
    elif n < 100:
        return "Double Digit"
    else:
        return "Multi-Digit"

def checkmultiple(nums):
    if nums % 7 == 0:
        return "Yes Multiple of 7"
    elif str(abs(nums)).endswith('7'):
        return "End with 7"
    else:
        return "Neither"

def find_quadrant(x, y):
    if x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return "Lies on Y-axis"
    elif y == 0:
        return "Lies on X-axis"
    elif x > 0 and y > 0:
        return "Quadrant 1"
    elif x < 0 and y > 0:
        return "Quadrant 2"
    elif x < 0 and y < 0:
        return "Quadrant 3"
    else:
        return "Quadrant 4"

def can_divide(amount):
    if amount % 100 != 0:
        return "Cannot be divided into 2000, 500, 100 notes"
    else:
        return "Can be divided into 2000, 500, 100 notes"

def can_amount(amt):
    if 100 <= amt <= 999:
        return "Yes"
    else:
        return "No"

def third_angle(a, b):
    # Check if given angles are valid (greater than 0 and less than 180)
    if a > 0 and b > 0 and (a + b) < 180:
        c = 180 - (a + b)
        return f"The third angle is {c}"
    else:
        return "Invalid triangle angles"

def is_perfect_square(n):
    if n < 0:
        return "Negative numbers cannot be perfect squares"
    
    i = 0
    while i * i <= n:
        if i * i == n:
            return "Perfect Square"
        i += 1
    
    return "Not a Perfect Square"

#### Logical Operater & Compound Statement

def character(s):
    if s.isalpha():
        return "Yes It's letter"
    elif s.isdigit():
        return "Yes it's digit"
    else:
        return "Neither"

def logic(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return

def median_of_three(a, b, c):
    if (a > b and a < c) or (a > c and a < b):
        return a
    elif (b > a and b < c) or (b > c and b < a):
        return b
    else:
        return c

def hourstime(hour):
    if 0 <= hour <= 12:
        return "AM"
    elif 12 <= hour <= 24:
        return "PM" 
    else:
        return "Invalid Input"

def incomeage(age, income):
    if(age > 18 and income >= 500000):
        return "Yes Should have to filled Tax Return"
    else:
        return "No need to fill tax return"

def checkifeligible(n1, n2):
    if(n1 > 0 and n2 > 0):
        if (n1 + n2) <= 100:
            return "Sum Positive"
        else:
            return "both number is positive but sum is more than 100"
    else:
        return "May be one or both number is Negative"

def Singaldigit(n):

    if (n <= 9):
        if n == 0:
            return "Zero"
        elif n == 1:
            return "One"
        elif n == 2:
            return "Two"
        elif n == 3:
            return "Three"
        elif n == 4:
            return "Four"
        elif n == 5:
            return "Five"
        elif n == 6:
            return "Six"
        elif n == 7:
            return "Seven"
        elif n == 8:
            return "Eight"
        elif n == 9:
            return "Nine"
    else:
        return "Please enter the number between 1 - 9"

def weekday(num):
    if 0 <= num <= 7:
        if(num <= 5):
            return "It's Weekdays"
        else:
            return "It's Weekend"

def electricity_bill(units):
    if units < 0:
        return "Invalid input! Units cannot be negative."
    elif units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    elif units <= 300:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    else:  # units > 300
        bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 15

    return f"Electricity bill for {units} units is ${bill}"

def password(s):
    if len(s) >= 8 and any(char.isdigit() for char in s):
        return "Yes it's valid Password"
    else:
        return "Please Enter Valid Password"

### Creative and Tricky Logical Scenarios

if __name__ == "__main__":
    #n1 = int(input().strip())
    #n2 = int(input().strip())
    #n3 = int(input().strip())
    n2 = input().strip()
    print(password(n2))
