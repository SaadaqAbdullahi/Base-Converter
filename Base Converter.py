#Number conversion calculator (binary,decimal,hexadecimal,octal)
import sys

#create class from decimal base conversions
class conversion_from_decimal:
    
    def __init__(self,number):
        self.decimal=number
        
    #decimal to binary conversion
    def decimal_to_binary(self):
        l=[]
        while self.decimal > 0:
            l.append(self.decimal%2)
            self.decimal=self.decimal//2
        self.binary=""
        l.reverse()
        for i in l:
            self.binary+=str(i)

    #decimal to octal conversion
    def decimal_to_octal(self):
        l=[]
        while self.decimal > 0:
            l.append(self.decimal%8)
            self.decimal = self.decimal//8
        self.octal=""
        l.reverse()
        for i in l:
            self.octal+=str(i)

    #decimal to hexadecimal conversion
    def decimal_to_hexadecimal(self):
        l=[]
        while self.decimal > 0:
            if self.decimal % 16 == 0:
                l.append(0)
            elif self.decimal % 16 != 0:
                remainder = self.decimal % 16
                if remainder > 9 and remainder < 16:
                    letters={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
                    remainder=letters.get(remainder)
                l.append(remainder)
            self.decimal = self.decimal//16
        self.hexa=""
        l.reverse()
        for i in l:
            self.hexa+=str(i)

    #display from decimal to each base        
    def display_conversion(self):
        if conversion_to == 'binary':
            number2.decimal_to_binary()
            print("In binary: {}".format(self.binary))
        elif conversion_to == 'octal':
            number2.decimal_to_octal()
            print("In octal: {}".format(self.octal))
        elif conversion_to == 'hexa' or conversion_to == 'hexadecimal':
            number2.decimal_to_hexadecimal()
            print("In hexadecimal: {}".format(self.hexa))

#create a class from other base numbers, which will convert to decimal 
class from_others:

    def __init__(self, number):
        self.number = number

    #from binary 
    def from_binary(self):
        self.number = str(self.number)
        string = self.number[::-1]
        l2=[]
        count=0
        for char in string:
            if char == '1':
                index = string.index(char,count)
                l2.append(2**index)
                count += 1
            else:
                count += 1
        self.decimal = sum(l2)
        return self.decimal
        
    #from octal
    def from_octal(self):
        l2=[]
        length = len(str(self.number))
        for i in range(length):
            remainder = self.number % 10
            l2.append(remainder)
            self.number//=10
        count=0
        for i in l2:
            index = l2.index(i,count)
            l2[index] = i * (8**index)
            count +=1
        self.decimal = sum(l2)
        return self.decimal
        
    #from hexadecimal
    def from_hexadecimal(self):
        l2=[]
        letters={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        for char in self.number:
            if char.lower() in 'abcdef':
                l2.append(letters.get(char.upper()))
            elif char.isdigit() == True:
                l2.append(int(char))
        l2.reverse()
        count = 0
        for i in l2:
            index = l2.index(i,count)
            l2[index] = i * (16**index)
            count += 1
        self.decimal = sum(l2)
        return self.decimal

    #display if user wants to convert to decimal
    def display_if_decimal(self):
        if conversion_from == 'binary':
            number1.from_binary()
            print("In decimal: {}".format(self.decimal))
        elif conversion_from == 'octal':
            number1.from_octal()
            print("In decimal: {}".format(self.decimal))
        elif conversion_from == 'hexa' or conversion_from == 'hexadecimal':
            number1.from_hexadecimal()
            print("In decimal: {}".format(self.decimal))
            
            
    
#accept user inputs needed to convert
conversion_from = input("What base do you want to convert from? ")
conversion_to = input("What base do you want to convert to? ")

#change inputs to lower which removes case sensitivity
conversion_from = conversion_from.lower()
conversion_to = conversion_to.lower()

try:
    #accept input as string since hexadecimal has letters used as numbers
    if conversion_from == 'hexadecimal' or conversion_from == 'hexa':
        n=input("Enter a number: ")

    #accept input as integer if not hexadecimal
    else:
        n=int(input("Enter a number: "))

#if unexpected user inputs occur, print 'invalid entries' and terminate program
except ValueError:
    print("Invalid Entries")
    sys.exit()

#if not from decimal, use methods from second class
#if desired output is not decimal, use methods from first class as well
#otherwise display output in decimal with only second class
if conversion_from != 'decimal':
    number1 = from_others(n)
    if conversion_to == 'decimal':
        number1.display_if_decimal()
    elif conversion_to != 'decimal':
        if conversion_from == 'binary':
            number2 = conversion_from_decimal(number1.from_binary())
            number2.display_conversion()
        elif conversion_from == 'hexa' or conversion_from == 'hexadecimal':
            number2 = conversion_from_decimal(number1.from_hexadecimal())
            number2.display_conversion()
        elif conversion_from == 'octal':
            number2 = conversion_from_decimal(number1.from_octal())
            number2.display_conversion()

#if its from decimal, just use methods from first class          
elif conversion_from == 'decimal':
    number2 = conversion_from_decimal(n)
    number2.display_conversion()






