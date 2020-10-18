'''
CommisionRate.py
Oct 16, 2020
to annual pay of an employee
'''

# modules
import time
import sys
import datetime

# functions
def CustomSplit(word):
    return list(word)


def slow_type(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

slow_type("\n---------------------------------------")
slow_type("    welcome to Estimated Salary Machine  ")
slow_type("---------------------------------------\n")

# Constants
BASE_PAY = 500
COMMISSION_RATE = 12.5
INCOME_TAX = 23.7

# Bools
hasInputtedCorrectName = bool(False)
hasInpputedSales = bool(False)
hasInputtedCorrectSin = bool(False)

# GettingEmployeeName
while not hasInputtedCorrectName:
    tempName = input("Please Insert your name!(eg. John F Kennedy)")
    splitNames = str.split(tempName)
    numberOfWords = len(splitNames)
    if numberOfWords == 3 and numberOfWords < 4:
        firstname = splitNames[0]
        middlename = splitNames[1]
        lastname = splitNames[2]
        hasInputtedCorrectName = bool(True)
    else:
        print(
            "You have not Inputed the correct name format! Please remember to put spaces between your first, "
            "middle and last name!\n")

# Getting Sin Number
while not hasInputtedCorrectSin:
    tempSin = input("\nPlease Insert your SIN number!(eg. 123123123)")
    splitSin = CustomSplit(tempSin)
    numberofLetters = len(splitSin)
    if numberofLetters < 10 and numberofLetters > 8:
        try:
            socialinsurancenumber = int(tempSin)
            hasInputtedCorrectSin = bool(True)
        except ValueError:
            print("You didnt input a number!!")
    else:
        print("You Inputed ", numberofLetters, "characters")
        print(
            "You have not Inputed the correct name format! Please remember that sin numbers can only have 9 digits!\n")

# Getting Sales in dollars
while not hasInpputedSales:
    tempSales = input("\nPlease Insert your amount of sales!(eg. 5000)")
    try:
        value = int(tempSales)
        salesamount = tempSales
        hasInpputedSales = bool(True)
    except ValueError:
        print("You didnt input the correct format! please try again. Numbers only")

# Calculations
Commission = value * (COMMISSION_RATE / 100)
grossPay = round(BASE_PAY + Commission, 2)
finalPay = round(grossPay * (INCOME_TAX / 100), 2)
salary = round(finalPay * 12,2)

#formatting
content_format = '%-*s%*s'
header_format = '%-*s%*s'
width = 35
item_width = width - 15

# output

#introduction
slow_type("\n---------------------------------------")
slow_type("       Employees Estimated Salary        ")
slow_type("---------------------------------------\n")

#string output For slowtype
firstNameString = ("First Name: "+ firstname)
middlenameString = ("Middle Name: "+ middlename)
lastnameString = ("Last Name: " + lastname)
socialInsureNumberString = ("SIN number: " + str(socialinsurancenumber) + "\n")

#StringOutput
slow_type(firstNameString)
slow_type(middlenameString)
slow_type(lastnameString)
slow_type(socialInsureNumberString)

#numberOutputs for SlowType
string1 = content_format%(item_width,"Total Amount of Sales In dollars:",25,salesamount)
string2 = content_format % (item_width, "Commission Rate in Percentage:", 29,COMMISSION_RATE)
string3 = content_format % (item_width, "Commission After Calculations in dollars:",20,Commission)
string4 = content_format % (item_width, "grossPay After Calculations in dollars:",17,grossPay)
string5 = content_format % (item_width, "finalPay(Monthly) After Calculations in dollars:",15,finalPay)
string6 = content_format % (item_width, "Estimated Salary After Calculations in dollars:",20,salary)
string7="-"*width*3

#NumberOutputs
slow_type(string7)
slow_type(string1)
slow_type(string2)
slow_type(string3)
slow_type(string4)
slow_type(string5)
slow_type(string6)
print(datetime.datetime.now())


#introduction
slow_type("\n---------------------------------------")
slow_type("     Thank you for using this code       ")
slow_type("---------------------------------------\n")

