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


# Counting & Character Analysis

def countvowelsandconsonants(s):
    countVowel = 0
    countConsonent = 0

    vol = 'aeiou'
    for i in s:
        if i.isalpha():
            if i in vol:
                countVowel += 1
            else:
                countConsonent += 1
    
    return countVowel, countConsonent

def counthenumberofdigit(s):
    countdigit = 0
    countletter = 0
    countspecialChar = 0

    for ch in s:
        if ch.isdigit():
            countdigit += 1
        elif ch.isalpha():
            countletter += 1
        elif not ch.isalnum() and not ch.isspace():
            countspecialChar += 1
    
    return countdigit, 


def countUpperCaseAndLowerCase(s):
    countuprcase = 0
    countlowercase = 0

    for ch in s:
        if ch.isupper():
            countuprcase += 1
        elif ch.islower():
            countlowercase += 1

    return countuprcase, countlowercase


def freqWithoutMap(s):
    freq = [0] * 256   # Array for ASCII chars

    for ch in s:
        freq[ord(ch)] += 1

    # Print only characters that appear
    for i in range(256):
        if freq[i] > 0:
            print(chr(i), ":", freq[i])

def countspaces(s):
    cntspaces = 0

    for ch in s:
        if ch == " ":
            cntspaces += 1
    return cntspaces

def countGivenChar(s, char):
    givnchar = 0

    for ch in s:
        if ch == char:
            givnchar += 1
    
    return givnchar

def alphabet(s):
    beforM = 0
    afterM = 0

    for ch in s.lower():
        if 'a' <= ch <= "m":
            beforM += 1
        elif "m" < ch <= "z":
            afterM += 1

    return beforM, afterM

def count_substrings_bruteforce(s):
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                cnt += 1
    return cnt


def countWordsStartWithVowel(s):
    vowels = "aeiouAEIOU"
    words = s.split()     # split sentence into words
    count = 0

    for w in words:
        if w[0] in vowels:    # check first letter of each word
            count += 1

    return count

def countWordsEndWithS(s):
    words = s.split()   # split the sentence into words
    count = 0

    for w in words:
        if w[-1].lower() == 's':   # check last character
            count += 1

    return count



# Reversing & Palindromic Thinking

def revString(s):
    return s[::-1]

def reverse_each_word(sentence):
    words = sentence.split()
    result = []

    for w in words:
        rev = ""
        for ch in w:
            rev = ch + rev
        result.append(rev)

    return " ".join(result)


def reverse_sentence(sentence):
    words = sentence.split()
    return " ".join(words[::-1])

def palindromeString(s):

    orignal = s 
    rev = s[::-1]

    return orignal == rev

def twoStringRev(s1, s2):
    if s1 == s2[::-1]:
        return True
    else:
        return False

def middlechar(s):

    n = len(s)
    mid = n // 2

    if n % 2 == 1:
        return s[mid]
    else:
        return s[mid - 1 : mid + 1]


def secoundhalf(s):
    n = len(s)
    mid = n // 2

    if n % 2 == 1:
        rev = s[mid + 1:]
    else:
        rev = s[mid : ]
    return rev[::-1]

def removefirstandlastchar(s):

    return s[1:-1]

def reverse_only_chars(s):
    s = list(s)  
    left, right = 0, len(s) - 1

    while left < right:
        if s[left].isdigit():
            left += 1
        elif s[right].isdigit():
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)

def reverse_skip_spaces(s):
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == " ":
            left += 1
        elif s[right] == " ":
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)


# Character & Word Manipulations

def removeAllVowels(s):
    vowels = "aeiouAEIOU"
    strvol = ""

    for ch in s:
        if ch not in vowels:
            strvol += ch
    
    return strvol
    
def removealltheSpace(s):
    ans = ""
    for ch in s:
        if ch != " ":
            ans += ch 
        elif ch == " ":
            continue
    return ans

def replaceallVolwels(s):

    replvowels = "aeiouAEIOU"
    ans = ""

    for ch in s:
        if ch in replvowels:
            ans += "*"
        else:
            ans += ch
    return ans

############OR##############
'''
def replaceallVolwels(s):

    replvowels = "aeiouAEIOU"
    ans = ""

    for ch in s:
        if ch in replvowels:
            ans += ch.replace(ch, "*")
        else:
            ans += ch
    return ans
'''

def replaceallSpace(s):
    ans = ""
    for ch in s:
        if ch == " ":
            ans += "_"
        else:
            ans += ch
    return ans

def removedigits(s):
    ans = ""

    for ch in s:
        if ch.islower():
            ans += ch
        elif ch.isdigit():
            continue
    return ans

def removedigits(s):
    ans = ""
    for ch in s:
        if not ch.isdigit(): 
            ans += ch
    return ans

def removeduplicatestr(s):
    ans = ""
    for ch in s:
        if ch not in ans:
            ans += ch
    return ans

def keeponlyFirstchr(s):
    ans = ""
    for ch in s:
        if ch not in ans:
            ans += ch

    return ans

def swaplowertoupper(s):
    ans = ""

    for ch in s:
        if ch.islower():
            ans += ch.upper()
        elif ch.isupper():
            ans += ch.lower()
        else:
            ans += ch
    return ans
    
def shift_by_one(s):
    ans = ""

    for ch in s:
        if 'a' <= ch <= 'z':          # lowercase
            ans += chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
        elif 'A' <= ch <= 'Z':        # uppercase
            ans += chr((ord(ch) - ord('A') + 1) % 26 + ord('A'))
        else:                         # keep other chars same
            ans += ch

    return ans



# Word - Level Thinking

def eachword(s):
    word = s.split()
    for ch in word:
        print(ch)

def wordEvenLength(s):
    cnt = 0
    for ch in s.split():
        if len(ch) % 2 == 0:
            cnt += 1      
    return cnt 


def longestword(s):
    word = s.split()
    longest = ""
    for ch in word:
        if len(ch) >= len(longest):
            longest = ch
    return longest


def shortestword(s):
    word = s.split()
    shortest = word[0]
    for ch in word:
        if len(ch) < len(shortest):
            shortest = ch 

    return shortest


def swapfirstandlast(s):
    word = s.split()

    word[0], word[-1] = word[-1], word[0]

    return " ".join(word)


def printallwordStartandEndwithletter(s):
    words = s.split()
    for ch in words:
        if ch[0] == ch[-1]:
            return ch
    return None

def wordsContaintheletterA(s):
    words = s.split()
    cont = 0

    for ch in words:
        if "a" in ch.lower():
            cont += 1
    return cont


def capitalize_words(s):
    return s.title()


def capitalize_words(s):
    words = s.split()
    result = ""

    for w in words:
        result += w[0].upper() + w[1:].lower() + " "

    return result.strip()


def normalize_spaces(s):
    words = s.split()       # removes all extra spaces
    return " ".join(words)  # joins with single space



# Mixed Logical Challenges

# Category 01 - Number based Logical Combinations

def Print1toN(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)

def sumofdigit(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

def armstrongnumber(n):
    original = n
    sumadd = 0
    digits = len(str(n))
    while n > 0:
        digit = n % 10
        sumadd += digit ** digits
        n //= 10
    return sumadd == original

def printallArmstrongNumber(n):
    for i in range(1, n + 1):
        original = i
        sumadd = 0
        digits = len(str(i))
        temp = i

        while temp > 0:
            digit = temp % 10
            sumadd += digit ** digits
            temp //= 10

        if sumadd == original:
            print(original)

def fact(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac  


def fact(n):
    if n == 0 or n == 1:      # base condition
        return 1
    return n * fact(n - 1)    # recursive call


def countevenDigit(n):
    count = 0
    while n > 0:
        digit = n % 10
        if (digit % 2 == 0):
            count += 1
        n //= 10     
    return count

def printAllPrimes(N):
    for num in range(2, N + 1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
        
def printAllPrimes(N):
    for num in range(2, N + 1):     # start from 2 because 1 is not prime
        isPrime = True

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                isPrime = False
                break
        
        if isPrime:
            print(num)

def reversenumber(n):
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    
    return rev

def checkifPalindrome(n):
    original = n 
    rev = 0

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev == original

def perfectnumber(n):
    sumofdivisior = 0
    for i in range(1, n):
        if (n % i == 0):
            sumofdivisior += i 
    return n == sumofdivisior




# Category 2 - String + Logic Mix

def anagram(s1, s2):

    sort1 = sorted(s1)
    sort2 = sorted(s2)

    return sort1 == sort2

def anagram(s1, s2):
    freq = [0] * 26

    for ch in s1:
        freq[ord(ch) - ord('a')] += 1

    for ch in s2:
        freq[ord(ch) - ord('a')] -= 1

    return all(x == 0 for x in freq)

def countvowel(s):
    vow = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vow:
            count += 1
    return count

def revString(s):

    if len(s) % 2 == 0:
        return s[::-1]

def revString(s):
    rev = ''
    if len(s) % 2 == 0:
        for ch in s:
            rev = ch + rev
    return rev

def replacevowel(s):
    mapping = {
        'a': '1', 'A': '1',
        'e': '2', 'E': '2',
        'i': '3', 'I': '3',
        'o': '4', 'O': '4',
        'u': '5', 'U': '5'
    }
    result = ""
    for ch in s:
        if ch in mapping:
            result += mapping[ch]   # replace vowel with number
        else:
            result += ch           # keep consonants as they are
    return result
            

def printcharappears(s):
    ans = ""
    for ch in s:
        if s.count(ch) > 1 and ch not in ans:
            ans += ch 

    return ans

def startandendwitSameLetter(s):
    word = s.split()
    count = 0

    for ch in word:
        if ch[0] == ch[-1]:
            count += 1
    return count

def toggleAlternateWords(s):
    words = s.split()
    result = []

    for i in range(len(words)):
        if i % 2 == 1:                    # alternate words (2nd, 4th, 6th...)
            result.append(words[i].swapcase())
        else:
            result.append(words[i])       # keep original
    return " ".join(result)

def checkstringrotated(s1, s2):
    if len(s1) != len(s2):
        return False

    return s2 in (s1 + s1)

def countMaximumvowel(s):
    
    vow = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vow:
            count += 1
    return count

def max_vowel_word_simple(sentence):
    vowels = set("aeiouAEIOU")
    words = sentence.split()
    max_word = ""
    max_count = -1

    for w in words:
        count = sum(1 for ch in w if ch in vowels)
        if count > max_count:
            max_count = count
            max_word = w

    return max_word

def duplicateword(s):
    word = s.split()
    ans = []

    for ch in word:
        if ch not in ans:
            ans.append(ch)
    
    return " ".join(ans)


# Array + Looping Logic

def MaxiandMiniele(arr):
    maxi = arr[0]
    mini = arr[0]

    for x in arr:
        if x > maxi:
            maxi = x
        if x < mini:
            mini = x
    return maxi, mini

def positivenegativeandZero(arr):
    pos = 0
    negative = 0
    zeroes = 0

    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            negative += 1
        elif i == 0:
            zeroes += 1
    return pos, negative, zeroes

def uniqueelement(arr):
    ans = []

    for i in arr:
        if i not in ans:
            ans.append(i)
    return ans

def reverseArr(arr):
    return arr[::-1]

def reverseArr(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # swap
        left += 1
        right -= 1

def shiftallzeros(arr):
    ans = []
    zeros = []

    for i in arr:
        if i != 0:
            ans.append(i)
        elif i == 0:
            zeros.append(i)
    
    return ans + zeros

def shiftallzeros(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1


def countelementeven(arr):
    count = []

    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 0:
            count.append(arr[i])
        
    return count

def mergetwoarray(arr1, arr2):
    return arr1 + arr2

def mergeSorted(arr1, arr2):
    i = j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result

def secoundlarele(arr):
    arr = list(set(arr))  
    arry = sorted(arr)

    return arry[-2]

def rotateRightByOne(arr):
    n = len(arr)
    last = arr[-1]

    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last


def sumofallelementatodd(arr):
    count = 0

    for i in range(len(arr)):
        if i % 2 != 0:
            count += arr[i]

    return count




# Category - Nested Logic & Pattern Flow


def table(n=10):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i*j:4}", end="")  # 4-space alignment
        print()

table()

def print_pairs(arr, target):
    seen = set()

    for num in arr:
        diff = target - num
        if diff in seen:
            print(diff, num)
        seen.add(num)

def all_subarrays(arr):
    res = []
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            res.append(arr[i:j+1])
    return res

def check_sorted(arr):
    ascending = True
    descending = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            ascending = False
        if arr[i] < arr[i + 1]:
            descending = False

    if ascending:
        return "Ascending"
    if descending:
        return "Descending"
    return "Not Sorted"

def numberappear(arr):
    count = 0

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            count += 1
    
    return count 

def same_char_pairs(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                print(f"({i}, {j}) -> {s[i]}")

def pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(ord('A') + j), end="")
        print()

def pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    # print in a pretty format
    width = n * 3
    for row in triangle:
        print(" ".join(str(x) for x in row).center(width))


def fib_first_n(n):
    """
    Return a list of the first n Fibonacci numbers using recursion.
    Convention: Fibonacci sequence = 0, 1, 1, 2, 3, ...
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    prev = fib_first_n(n - 1)           # recursive step: list of first n-1 terms
    prev.append(prev[-1] + prev[-2])    # append the next fib number
    return prev

def spiral_matrix(m, n):
    # create empty m x n matrix
    mat = [[0] * n for _ in range(m)]
    top, bottom, left, right = 0, m - 1, 0, n - 1
    num = 1

    while top <= bottom and left <= right:
        # left -> right (top row)
        for col in range(left, right + 1):
            mat[top][col] = num
            num += 1
        top += 1

        # top -> bottom (right column)
        for row in range(top, bottom + 1):
            mat[row][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            # right -> left (bottom row)
            for col in range(right, left - 1, -1):
                mat[bottom][col] = num
                num += 1
            bottom -= 1

        if left <= right:
            # bottom -> top (left column)
            for row in range(bottom, top - 1, -1):
                mat[row][left] = num
                num += 1
            left += 1

    return mat

def print_matrix(mat):
    for row in mat:
        print(" ".join(f"{x:3}" for x in row))


# Category 5 - Applied Reasoning & Real Life Logic

def student(mark):
    count = 0

    for m in mark:
        if m >= 40:
            count += 1
    
    return count

def agecount(age):
    adults = 0
    minors = 0
    seniors = 0

    for a in age:
        if a < 18:
            minors += 1
        elif a < 60:
            adults += 1
        else:
            seniors += 1

    return adults, minors, seniors

def validatepass(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():  # special character
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        return "Valid Password"
    else:
        return "Not Valid"

def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid Operation"


import random

def cointoss(n):
    heads = 0
    tails = 0

    for i in range(n):
        toss = random.choice(["H", "T"])   # H = Heads, T = Tails
        if toss == "H":
            heads += 1
        else:
            tails += 1

    return heads, tails

def digit_frequency(num):
    freq = [0] * 10        # index 0–9 for each digit

    for ch in str(num):    # convert number to string
        freq[int(ch)] += 1

    return freq

def common_unique(a, b):
    # unique intersection
    return list(set(a) & set(b))

def common_chars(s1, s2, case_insensitive=False):
    if case_insensitive:
        s1, s2 = s1.lower(), s2.lower()
    return sorted(set(s1) & set(s2))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(arr):
    return sum(1 for x in arr if is_prime(x))

# Example
arr = [2, 3, 4, 5, 15, 17, 19, 1, 0, -3]
print(count_primes(arr))  # 5  (2,3,5,17,19)


import re

def palindromic_words(sentence):
    # extract words, remove non-alphanumeric from ends
    words = re.findall(r"\b[\w']+\b", sentence)  # keeps letters/digits/underscore/apos
    pals = [w for w in words if w.lower() == w.lower()[::-1] and len(w) > 0]
    return pals

# Example
sent = "Madam Anna and Otto went to level the radar. 'wow'!"
print(palindromic_words(sent))  # ['Madam', 'Anna', 'Otto', 'level', 'radar', 'wow']




if __name__ == "__main__":
    arr = list(map(int, input().strip().split(',')))
    print(sumofallelementatodd(arr))




if __name__ == "__main__":
    #n1 = int(input().strip())
    #n2 = int(input().strip())
    n3 = input().strip()
    #n2 = input().strip()
    print(whetherstringisempty(n3))










