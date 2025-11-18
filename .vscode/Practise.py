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

### Creative and Tricky Logical Scenarios

def pointlies(x, y):
    if x == 0 and y == 0:
        return "The point is at the origin."
    elif y == 0:
        return "The point lies on the X-axis."
    elif x == 0:
        return "The point lies on the Y-axis."
    else:
        return "The point is not on any axis."

def pythagoreanTriplet(a, b, c):
    x, y, z = sorted([a, b, c])

    if (z*z == x*x + y*y):
        return "These numbers form a Pythagorean triple."
    else:
        return "These numbers do NOT form a Pythagorean triple."

def validCalender(day, month):
    date = {1: 31, 2: 28, 3: 31, 4: 30, 
            5: 31, 6: 30, 7: 31, 8: 31,
            9: 30, 10: 31, 11: 30, 12: 31}

    if day < 1 or month > 12:
        return "Invalid Input"
    else:
        if 1 <= day <= date[month]:
            return "Valid Date"
        else:
            return "Invalid date: day does not exist for this month."

def clock_angle(hours, minutes):
    # Convert hours to 12-hour format
    if hours >= 12:
        hours = hours % 12

    # Calculate minute hand angle
    minute_angle = minutes * 6

    # Calculate hour hand angle
    hour_angle = hours * 30 + minutes * 0.5

    # Find the difference
    angle = abs(hour_angle - minute_angle)

    # Use if–else to choose the smaller angle
    if angle > 180:
        smaller_angle = 360 - angle
    else:
        smaller_angle = angle

    return smaller_angle

def arithmetic(a, b, c):
    if (a - b) == (b - c):
        return "Yes it's Arithmetic Progression"
    else:
        return "It's not Arithmetic Progression"

def geomatricProgression(a, b, c):
    if a == 0 and b == 0:
        return 
    
    if b * b == a * c:
        return "Yes it's Geomatric Progression"
    else:
        return "No it's not Geomatric Progression"

def sumoffirstandlastdigit(num):
    a = num // 100        # first digit
    b = (num // 10) % 10  # middle digit
    c = num % 10          # last digit

    if (a + c) == b:
        return "Equal to Middle Digit"
    else:
        return "No it's not equal to middle digit"

def check_sum_vs_product(n):
    sum_digits = 0
    prod_digits = 1

    temp = n
    while temp > 0:
        digit = temp % 10
        sum_digits += digit
        prod_digits *= digit
        temp //= 10

    print("Sum of digits =", sum_digits)
    print("Product of digits =", prod_digits)

    if sum_digits > prod_digits:
        print("YES — Sum of digits is greater than the product of digits.")
    else:
        print("NO — Sum of digits is NOT greater than the product of digits.")

def earlier_date(d1, m1, d2, m2):
    if m1 < m2:
        print("First date comes earlier.")
    elif m1 > m2:
        print("Second date comes earlier.")
    else:  # months equal
        if d1 < d2:
            print("First date comes earlier.")
        elif d1 > d2:
            print("Second date comes earlier.")
        else:
            print("Both dates are the same.")

def print_century(year):
    century = (year + 99) // 100

    # Determine suffix
    if 10 < century % 100 < 14:  # 11, 12, 13
        suffix = "th"
    else:
        last_digit = century % 10
        if last_digit == 1:
            suffix = "st"
        elif last_digit == 2:
            suffix = "nd"
        elif last_digit == 3:
            suffix = "rd"
        else:
            suffix = "th"

    print(f"{century}{suffix} century")



if __name__ == "__main__":
    n1 = int(input().strip())
    #n2 = int(input().strip())
    #n3 = int(input().strip())
    #n2 = input().strip()
    print(sumoffirstandlastdigit(n1))

if __name__ == "__main__":
    #n1 = int(input().strip())
    #n2 = int(input().strip())
    #n3 = int(input().strip())
    n2 = input().strip()
    print(password(n2))
