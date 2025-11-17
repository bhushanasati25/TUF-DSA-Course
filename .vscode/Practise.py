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



