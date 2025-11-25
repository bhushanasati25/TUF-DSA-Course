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


## Looping & Patterns (Iteration & Flow)

def Printnumber1to10(n):
    for i in range(1, n):
        print(i)

def evennumber(n):
    for i in range(1, n):
        if i % 2 == 0:
            print(i)

def oddNumber(n):
    for i in range(n):
        if i % 2 != 0:
            print(i)

def downnumber(n):
    for i in range(n, 0, -1):
        print(i)

def table(n):
    for i in range(1, 11):
        print(i * n)

'''
def naturalnumber(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
'''
def naturalnumber(n):
    total = n * (n + 1) // 2
    return total

def sumofallevennumber(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += i
    return count

def sumofalloddnumber(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            count += i
    return count

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def productofgivendigit(n):
    product = 1
    while (n > 0):
        digit = n % 10
        product *= digit
        n //= 10
    return product

def primenum(n):
    if n <= 1:
        return False

    for i in range(2, n + 1):
        if n % 2 == 0:
            return "it's not prime number"
        else:
            return "Yes It's is a Prime Number"

### Number Based Looping Logic

def countnumberofdigit(n):

    if n == 0:
        return 1
    count = 0
    while n > 0:
        digit = n % 10
        count += 1
        n //= 10
    
    return count

def reversenumber(n):
    rev = 0
    while n > 0:
        lastdigit = n % 10
        n = n // 10
        rev = (rev * 10) + lastdigit
    return rev 
    
def palindromenumber(n):
    original = n
    rev = 0 
    while n > 0:
        lastdigit = n % 10
        n //= 10
        rev = (rev * 10) + lastdigit
    return rev == original

def sumofdigit(n):
    sumadd = 0
    while n > 0:
        digit = n % 10
        n //= 10
        sumadd += digit

    return sumadd

def armstrongnumber(n):
    origin = n
    smdadd = 0 
    digits = len(str(n))
    while n > 0:
        digit = n % 10
        n //= 10
        smdadd += digit ** digits

    return smdadd == origin

def perfectnumber(n):

    if n <= 0:
        return False
    
    ori = n
    sumofdivisior = 0

    for i in range(1, n):
        if n % i == 0:
            sumofdivisior += i

    return sumofdivisior == n

def primeNum(n):
    for num in range(2, n + 1):
        isprime = True
        for i in range(2, num):
            if(num % i == 0):
                isprime = False
                break
    
        if isprime:
            print(num)

def prime(n):
    for i in range(2, n):
        if(n % i == 0):
            return "It is not Prime Number"
    return "It is Prime Number"

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

def fibonacci(n):
    a, b = 0, 1
    count = 0

    while count < n:
        print(a)
        a, b = b, a + b
        count += 1

def sum_fibonacci(n):
    a, b = 0, 1
    total = 0

    for _ in range(n):
        total += a      # add current Fibonacci number
        a, b = b, a + b # generate next number

    return total

### Mathematical & Logical Patterns

def squarenumber(n):
    for i in range(1, n + 1):
        print(i * i)

def cube(n):
    for i in range(1, n + 1):
        print(i * i * i)

def printallnumberaandb(a, b):
    for i in range(a, b + 1):
        if i % 7 == 0:
            print(i)

def gcd(n1, n2):
    ans = []

    for i in range(1, min(n1,n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            ans.append(i)

    return ans[-1]

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

    def LCM(n1, n2):
        return (n1 * n2) // gcd(n1, n2)

def factor(n1):
    for i in range(1, n1 + 1):
        if n1 % i == 0:
            print(i)

'''
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

    def is_strong(n):
    original = n          # store original number
    total = 0             # to store sum of factorials

    while n > 0:
        digit = n % 10                   # extract last digit
        total += factorial(digit)        # add factorial of digit
        n //= 10                         # remove last digit

    return total == original
'''

def print_AP(a, d, n):
    term = a
    for i in range(n):
        print(term)
        term += d

def print_GP(a, r, n):
    term = a
    for i in range(n):
        print(term)
        term *= d





def starprinting():
    print("*")
    print("****")

def printnstar(n):
    for i in range(n):
        print("*", end = " ")

def printsquareofstar(n):
    for i in range(n):
        for j in range(n):
            print("*", end = "")
        print()

def printanincreasingTriangleofstar(n):
    for i in range(n):
        for j in range(i):
            print("*" , end ="")
        print()

def rightAlignedTriangleofstar(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(i):
            print("*" ,end = "")
        print()

def printStarsinEvenNumber(n):
    for i in range(n + 1):
        for j in range(2 * i):
            print("*", end ="")
        print()

def starinOddNumber(n):
    for i in range(n):
        for j in range(2 * i + 1):
            print("*", end="")
        print()

def printCenteredpyramidofstar(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        print()

def printstarandspaces(n):
    for i in range(n):
        for j in range(n - i - 1):
            print("b", end ="")
        for j in range(i):
            if(j % 2 == 0):
                print("*", end ="")
            else:
                print("b", end ="")
        print()

def printnumberinanincresingsequences(n):
    for i in range(n):
        for j in range(1, i + 1):
            print(j, end = "")
        print()

def printrepeatednumberperrow(n):
    for i in range(n):
        for j in range(1, i + 1):
            print(i, end ="")
        print()

def pattern1(n):
    num = 1
    for i in range(1, n):
        for j in range(1, i + 1):
            print(str(num) + " ", end= "")
            num += 1
        
        print()

def pattern2(n):
    num = 1
    for i in range(1, n):
        for j in range(1, i + 1):
            print(str((num % 10)) + " ", end = "")
            num += 1
        print()

def pattern3(n):
    for i in range(1, n):
        for j in range(1, i + 1):
            val = (i + j) % 2
            print(str(val) + " ", end="")
        print()

def pattern4(rows):
    for i in range(1, rows + 1):
        # odd row → start with 1, even row → start with 0
        val = 1 if i % 2 != 0 else 0
        for j in range(1, i + 1):
            print(val, end=" ")
            val = 1 - val  # flip between 1 and 0
        print()

def pattern5(n):
    ch = 'A'
    for i in range(1,n + 1):
        for j in range(1, i + 1):
            print(ch, end=" ")
            ch = chr(ord(ch) + 1)
        print()

def pattern6(n):
    for i in range(n):
        ch = chr(ord("A") + i)   
        for j in range(i + 1):
            print(ch, end=" ")  
        print()

def pattern7(n):
    for i in range(n):
        for j in range(i):
            ch = chr(ord("A") + j)
            print(ch, end = " ")
        print()

def pattern8(n):
    ch = 'A'
    for i in range(1, n + 1):
        for j in range(i, n):
            print(" ", end = "")
        
        for j in range(2 * i - 1):
            print(ch, end = " ")
            ch = chr(ord(ch) + 1)
        print()

def pattern9(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end = "")
        print()


def pattern10(n):
    for i in range(1, n + 1):
        for j in range(i, n):
            print(" ", end="")
        
        for j in range(1, i + 1):
            print(j, end = "")
        
        for j in range(i - 1, 0, -1):
            print(j, end ="")
        print()

def pattern11(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print("*", end = "")
        print()



## Logical Loop Combination

def printallnumber(n):
    sumofdigit = []

    for i in range(1, n + 1):
        digit_sum = sum(int(d) for d in str(i))
        if digit_sum % 2 == 0:
            sumofdigit.append(i)
    
    return sumofdigit


def countnumber(n):
    res = []

    for i in range(1, n + 1):
        if i % 7 == 0 and i % 5 != 0:
            res.append(i)
    
    return res


def printallthepalindromenumber(n):
    res = []

    for i in range(1, n + 1):
        original = i
        rev = 0
        temp = i
        while temp > 0:
            lastdigit = temp % 10
            temp //= 10
            rev = (rev * 10) + lastdigit
        
        if rev == original:
            res.append(i)

    return res

def multipleof3(n):
    res = []

    for i in range(1, n + 1):
        temp = i
        sumofc = 0
        while temp > 0:
            digit = temp % 10
            sumofc += digit
            temp //= 10
        
        if sumofc % 3 == 0:
            res.append(i)

    return res


def smallestandlargestdigit(n):
    smallest = 9
    lar = 0
    while n > 0:
        digit = n % 10
        n //= 10

        if digit < smallest:
            smallest = digit
        
        if digit > lar:
            lar = digit

    return smallest, lar


def even_binary_ones(n):
    res = []
    for i in range(1, n + 1):
        binary = bin(i)[2:]       # convert to binary string
        ones = binary.count('1')  # count 1s
        if ones % 2 == 0:
            res.append(i)
    return res  

def patternrow(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i * i, end= " ")
        print()

            
def squared_grid_pattern(n):
    for i in range(1, n + 1):
        for j in range(n):
            print(i * i, end=" ")
        print()


def sum_odd_even_digits(n):
    odd_sum = 0
    even_sum = 0

    while n > 0:
        digit = n % 10
        n //= 10

        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return odd_sum, even_sum

def number(n):
    sumofnozero = 0

    while n > 0:
        digit = n % 10
        n //= 10

        if digit != 0:
            sumofnozero += digit
        elif digit == 0:
            continue
    return sumofnozero


## Recursion (Thinking in Self - Reference)

def onetoNusingRecursion(i, n):
    if i > n:
        return 0
    print(i, end = " ")
    print()
    onetoNusingRecursion(i + 1, n)

def nToDown(n):
    if n == 0:
        return 0
    
    print(n)
    nToDown(n - 1)
    
def oneToNEvenNumber(n):
    if n == 0:
        return 0 

    oneToNEvenNumber(n - 1)
    if n % 2 == 0:
        print(n)

def oneTonOddNumber(n):
    if n == 0:
        return 0

    oneTonOddNumber(n - 1)
    if n % 2 != 0:
        print(n)

def sumofNnaturalNumber(n):
    if n == 0:
        return 0 
    return n + sumofNnaturalNumber(n - 1)

def factorialnumber(n):
    if n == 0:
        return 1 
    
    return n * factorialnumber(n - 1)

def power(x, n):
    if n == 0:
        return 1

    return x * power(x, n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(n, current=0):
    if current == n:
        return
    
    print(fibonacci(current))
    print_fibonacci_series(n, current + 1)

def sumofdigit(n):
    if n == 0 :
        return 0
    return (n % 10) + sumofdigit(n // 10)

## Number-Based Recursive Thinking

def CountNumberofDigit(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + CountNumberofDigit(n // 10)

def reverse_number(n):
    n = str(n)
    if len(n) == 1:
        return n
    return reverse_number(n[1:]) + n[0]

def palindrome_number(n):
    n = str(n)
    if len(n) == 1:
        return n
    return reverse_number(n[1:]) + n[0] == n 

def productofdigit(n):
    n = abs(n)
    if n < 10:
        return n 

    return (n % 10) * productofdigit(n // 10)
    
def gcd(a, b):
    # Base case: when b becomes 0, a is the GCD
    if b == 0:
        return a
    # Recursive step: gcd(b, a % b)
    return gcd(b, a % b)

def to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    return to_binary(n // 2) + str(n % 2)

def print_in_words(n):
    words = ["zero", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]

    # Handle negative numbers
    if n < 0:
        return "minus " + print_in_words(-n)

    # Base case: single digit
    if n < 10:
        return words[n]

    # Recursive case: process all digits except last, then last
    return print_in_words(n // 10) + " " + words[n % 10]

def sum_even(n):
    # Base case
    if n == 1:
        return 2   # first even number is 2
    
    # Recursive case
    return 2 * n + sum_even(n - 1)

def sum_odd(n):
    # Base case: the first odd number is 1
    if n == 1:
        return 1
    
    # Recursive case: nth odd number + sum of previous odd numbers
    return (2 * n - 1) + sum_odd(n - 1)

def nCr(n, r):
    # Base cases
    if r == 0 or r == n:
        return 1
    # Pascal's recursive relation
    return nCr(n - 1, r - 1) + nCr(n - 1, r)

## Recursion (Thinking in Self - Reference)

def onetoNusingRecursion(i, n):
    if i > n:
        return 0
    print(i, end = " ")
    print()
    onetoNusingRecursion(i + 1, n)

def nToDown(n):
    if n == 0:
        return 0
    
    print(n)
    nToDown(n - 1)
    
def oneToNEvenNumber(n):
    if n == 0:
        return 0 

    oneToNEvenNumber(n - 1)
    if n % 2 == 0:
        print(n)

def oneTonOddNumber(n):
    if n == 0:
        return 0

    oneTonOddNumber(n - 1)
    if n % 2 != 0:
        print(n)

def sumofNnaturalNumber(n):
    if n == 0:
        return 0 
    return n + sumofNnaturalNumber(n - 1)

def factorialnumber(n):
    if n == 0:
        return 1 
    
    return n * factorialnumber(n - 1)

def power(x, n):
    if n == 0:
        return 1

    return x * power(x, n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(n, current=0):
    if current == n:
        return
    
    print(fibonacci(current))
    print_fibonacci_series(n, current + 1)

def sumofdigit(n):
    if n == 0 :
        return 0
    return (n % 10) + sumofdigit(n // 10)

## Number-Based Recursive Thinking

def CountNumberofDigit(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + CountNumberofDigit(n // 10)

def reverse_number(n):
    n = str(n)
    if len(n) == 1:
        return n
    return reverse_number(n[1:]) + n[0]

def palindrome_number(n):
    n = str(n)
    if len(n) == 1:
        return n
    return reverse_number(n[1:]) + n[0] == n 

def productofdigit(n):
    n = abs(n)
    if n < 10:
        return n 

    return (n % 10) * productofdigit(n // 10)
    
def gcd(a, b):
    # Base case: when b becomes 0, a is the GCD
    if b == 0:
        return a
    # Recursive step: gcd(b, a % b)
    return gcd(b, a % b)

def to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    return to_binary(n // 2) + str(n % 2)

def print_in_words(n):
    words = ["zero", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine"]

    # Handle negative numbers
    if n < 0:
        return "minus " + print_in_words(-n)

    # Base case: single digit
    if n < 10:
        return words[n]

    # Recursive case: process all digits except last, then last
    return print_in_words(n // 10) + " " + words[n % 10]

def sum_even(n):
    # Base case
    if n == 1:
        return 2   # first even number is 2
    
    # Recursive case
    return 2 * n + sum_even(n - 1)

def sum_odd(n):
    # Base case: the first odd number is 1
    if n == 1:
        return 1
    
    # Recursive case: nth odd number + sum of previous odd numbers
    return (2 * n - 1) + sum_odd(n - 1)

def nCr(n, r):
    # Base cases
    if r == 0 or r == n:
        return 1
    # Pascal's recursive relation
    return nCr(n - 1, r - 1) + nCr(n - 1, r)

## Pattern & Printing Problems

def printstar(n):
    if n == 0:
        return 
    print("*", end = "")
    printstar(n - 1)

def squareofstar(n, current=None):
    if current is None:
        current = n   # initialize
    
    if current == 0:
        return

    printstar(n)
    print()
    squareofstar(n, current - 1)

def triangle(n):
    if n == 0:
        return
    printstar(n)   # print the row of n stars
    print()          # new line
    triangle(n - 1)  # recursive call for next smaller row

def triangleBottomup(n):
    if n == 0:
        return
    
    triangleBottomup(n - 1)
    printstar(n)
    print()

def print_numbers(k):
    if k == 0:
        return
    print_numbers(k - 1)
    print(k, end="")

def print_pattern(n):
    if n == 0:
        return
    print_pattern(n - 1)
    print_numbers(n)
    print()

def table(n, i=1):
    if i > 10:         # stop at 10
        return
    print(f"{n} x {i} = {n * i}")
    table(n, i + 1)    # move to next number

def inc_dec(n, current=1):
    if current > n:
        return
    # Print increasing order
    print(current, end=" ")
    inc_dec(n, current + 1)
    # Print decreasing order
    print(current, end=" ")

def sum_series(n):
    if n <= 0:
        return 0
    if n == 1:
        print("sum(1) = 1")
        return 1

    prev_sum = sum_series(n - 1)
    total = prev_sum + n
    # print the formation step for current n
    print(f"sum({n}) = sum({n-1}) + {n} = {prev_sum} + {n} = {total}")
    return total


import string

def char_pattern(n):
    if n <= 0:
        return
    # first print smaller pattern
    char_pattern(n - 1)

    # build line with first n letters (A, B, C, ...)
    alphabet = string.ascii_uppercase
    # if you want to cap at 26: use min(n, 26)
    line = "".join(alphabet[i % 26] for i in range(n))  # wrap-around if >26
    print(line)


## String Based Recursion 

def reverse(s):
    if len(s) == 0:
        return ""
    return reverse(s[1:]) + s[0]

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

def count_vowels(s):
    if len(s) == 0:
        return 0
    return (1 if s[0].lower() in "aeiou" else 0) + count_vowels(s[1:])

def remove_spaces(s):
    if len(s) == 0:
        return ""
    first = "" if s[0] == " " else s[0]
    return first + remove_spaces(s[1:])

def replace_char(s, old, new):
    if len(s) == 0:
        return ""
    first = new if s[0] == old else s[0]
    return first + replace_char(s[1:], old, new)

def remove_char(s, ch):
    if len(s) == 0:
        return ""
    first = "" if s[0] == ch else s[0]
    return first + remove_char(s[1:], ch)

def print_chars(s, i=0):
    if i == len(s):
        return
    print(s[i])
    print_chars(s, i + 1)

def print_rev(s, i=0):
    if i == len(s):
        return
    print_rev(s, i + 1)
    print(s[i])

def to_upper(s):
    if len(s) == 0:
        return ""
    return s[0].upper() + to_upper(s[1:])

def count_cv(s, i=0):
    if i == len(s):
        return (0, 0)

    vowels = "aeiou"
    v, c = count_cv(s, i + 1)

    if s[i].lower() in vowels:
        return (v + 1, c)
    elif s[i].isalpha():
        return (v, c + 1)
    else:
        return (v, c)
    

## String (Basic Logic Building)

def strinputlen(n):
    count = 0 
    for i in n:
        count += 1
    return count

''' # there is two options
def stringinplen(s):
    strlen = len(s)
    return strlen 
'''

def firstandlast(s):

    first = s[0]
    last = s[-1]

    return first, last

def convstringtoUppercase(s):
    if s == "":
        return
    uppercase = s.upper()
    return uppercase

''' there is 2 options
def convstringtoUppercase(s):
    result = ""

    for ch in s:
        if 'a' <= ch <= 'z':  
            result += chr(ord(ch) - 32)  
        else:
            result += ch
'''

def lowercase(s):
    if s == "":
        return ""
    lowec = s.lower()
    return lowec
'''
def lowercase(s):
    if s == "":
        return ""

    result = ""
    for ch in s:
        if "A" <= ch <= "Z":
            result += chr(ord(ch)+ 32)
        else:
            result += ch 
    return result
'''

def countchaar(s):
    if s == "":
        return 0
    count = 0

    for ch in s:
        if ch != " ":
            count += 1
    
    return count

def wordinsentence(s):
    if s == len(s):
        return 1
    
    count = 0
    isword = False

    for ch in s:
        if ch != " " and not isword:
            count += 1
            isword = True
        elif ch == " ":
            isword = False
    
    return count

def concat(s1, s2):
    result = s1 + s2

    return result

def twostring(s1, s2):

    if s1 == s2:
        return True

def comparetwostr(s1, s2):
    if s1 < s2:
        print("s1 comes first")
    elif s1 > s2:
        print("s2 comes first")
    else:
        print("both are equal")

def asccichar(s):
    if s == "":
        return 0

    res = []
    for ch in s:
        res.append(ord(ch))
    return res

def whetherstringisempty(s):
    strlen = len(s)

    for i in s:
        if s != strlen:
            return True
    
    return False



if __name__ == "__main__":
    #n1 = int(input().strip())
    #n2 = int(input().strip())
    n3 = input().strip()
    #n2 = input().strip()
    print(whetherstringisempty(n3))







if __name__ == "__main__":
    #n1 = int(input().strip())
    #n2 = int(input().strip())
    #n3 = int(input().strip())
    #n2 = input().strip()
    print(count_cv("Bhushan"))






