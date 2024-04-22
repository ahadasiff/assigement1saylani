user_salary = int(input("ENTER SALARY::"))
service_time = int(input("HOW MANY YEARS DID YOU SERVE?"))
bouns = (user_salary * 5)/100
if service_time > 5:
    user_salary += bouns
    print("YOUR BOUNS IS RS ",user_salary)
else:
    print("NO BOUNS FOR YOU ",user_salary)
# ENTER SALARY::500
# HOW MANY YEARS DID YOU SERVE?6
# YOUR BOUNS IS RS  525.0
#2
user_input =int(input("ENTER YOUR AGE::"))
if  user_input >17 :
    print("ELIGIBLE")
else:
    print("NOT ELIGIBLE")
# ENTER YOUR AGE::15
# NOT ELIGIBLE
#3
user_number = int(input("ENTER NUMBER::"))
if user_number%2 == 0:
    print("EVEN")
else:
    print("ODD")
# ENTER NUMBER::3
# ODD
#4
user_number = int(input("ENTER NUMBER::"))
if user_number%7 == 0:
    print(user_number ,"is divisible")
else:
    print(user_number ,"is not  divisible")
# ENTER NUMBER::8
# 8 is not  divisible
#5
user_number = int(input("ENTER NUMBER::"))
if user_number%5 == 0:
    print("HELLO")
else:
    print("BYE")
# ENTER NUMBER::3
# BYE
#6
user_electricity_unit = int(input("ENTER ELECTRICITY UNIT::"))
if user_electricity_unit > 0 and user_electricity_unit<= 100:
    unit = 0
    formula = user_electricity_unit * unit
    print("YOUR BILL IS RS ",formula)
elif user_electricity_unit > 100 and user_electricity_unit<= 200:
    unit = 5
    formula = user_electricity_unit * unit
    print("YOUR BILL IS RS ",formula)
elif user_electricity_unit > 200:
    unit = 10
    formula = user_electricity_unit * unit
    print("YOUR BILL IS RS ",formula)
# ENTER ELECTRICITY UNIT::150
# YOUR BILL IS RS  750
#7
user_number = int(input("ENTER NUMBER::"))
user_number = str(user_number)
user_length = len(user_number)
user_last_digit = int(user_number[user_length-1])
print(user_last_digit)
# ENTER NUMBER::143228999
# 9
#8
user_number = int(input("ENTER NUMBER::"))
user_number = str(user_number)
user_length = len(user_number)
user_last_digit = int(user_number[user_length-1])
if user_last_digit%3 == 0:
    print("yes it is .")
else:
    print("no,its not")
# ENTER NUMBER::14329
# yes it is .
#9
length = int(input("ENTER LENGTH::"))
breath = int(input("ENTER BREATH::"))
if length == breath:
    print("SQUARE")
else:
    print("RECTANGLE")
# ENTER LENGTH::78999
# ENTER BREATH::8933753
# RECTANGLE
#10
first_number = int(input("ENTER FIRST NUMBER::"))
second_number =int(input("ENTER SECOND NUMBER::"))
if first_number > second_number:
    print("GREATER NUMBER IS",first_number)
else:
    print("GREATER NUMBER IS",second_number)
# ENTER FIRST NUMBER::45
# ENTER SECOND NUMBER::200
# GREATER NUMBER IS 200
#11
item_quantity =int(input("ENTER QUANTITY::"))
one_item = 100
total_price = item_quantity*100
if total_price >= 1000:
    discount = (total_price*10)/100
    print("AFTER 10% DISCOUNT RS ",discount)
else:
    print("NO DISCOUNT YOUR TOTAL PRICE IS RS ",total_price)
# ENTER QUANTITY::500
# AFTER 10% DISCOUNT RS  5000.0
#12
marks = int(input("ENTER MARKS::"))
if marks < 25:
    print("F")
elif marks > 25 and marks <= 45:
    print("E")
elif marks > 45 and marks <= 50:
    print("D")
elif marks > 50 and marks <= 60:
    print("C")
elif marks > 60 and marks <= 80:
    print("B")
else:
    print("A")
# ENTER MARKS::100
# A
#13
person_1 =int(input("PERSON1 = ENTER AGE::"))
person_2 =int(input("PERSON2 = ENTER AGE::"))
person_3 =int(input("PERSON3 = ENTER AGE::"))
if person_1 > person_2 and person_1 > person_3:
    print("PERSON_1 IS OLDEST")
elif person_2 > person_1 and person_2 > person_3:
    print("PERSON_2 IS OLDEST")
elif person_3 > person_1 and person_3 > person_2:
    print("PERSON_3 IS OLDEST")
if person_1 < person_2 and person_1 < person_3:
    print("PERSON_1 IS YOUNGEST")
elif person_2 < person_1 and person_2 < person_3:
    print("PERSON_2IS YOUNGEST")
elif person_3 < person_1 and person_3 < person_2:
    print("PERSON_3 IS YOUNGEST")
# PERSON1 = ENTER AGE::18
# PERSON2 = ENTER AGE::65
# PERSON3 = ENTER AGE::35
# PERSON_2 IS OLDEST
# PERSON_1 IS YOUNGEST
#14
class_held =int(input("ENTER NUMBER OF CLASSES HELD::"))
class_attend =int(input("ENTER NUMBER OF CLASSES ATTEND::"))
attendence_percentage = (class_attend*100)/class_held
if attendence_percentage >= 75:
    print("allowed")
else:
    print("not allowed")
# ENTER NUMBER OF CLASSES HELD::100
# ENTER NUMBER OF CLASSES ATTEND::50
# not allowed
# #15
class_held =int(input("ENTER NUMBER OF CLASSES HELD::"))
class_attend =int(input("ENTER NUMBER OF CLASSES ATTEND::"))
attendence_percentage = (class_attend*100)/class_held
user_medical_issue = input("MEDICAL CAUSE (Y/N)::")
if attendence_percentage >= 75:
    print("allowed")
elif attendence_percentage <= 75 and user_medical_issue == "Y":
    print("allowed")
elif attendence_percentage <= 75 and user_medical_issue == "N":
    print("NOT allowed")
# ENTER NUMBER OF CLASSES HELD::100
# ENTER NUMBER OF CLASSES ATTEND::50
# MEDICAL CAUSE (Y/N)::Y
# allowed
#16
year = int(input("ENTER YEAR::"))
if year % 4 == 0:
    print("ITS A LEAP YEAR")
else:
    print("ITS NOT A LEAP YEAR")
# ENTER YEAR::2014
# ITS NOT A LEAP YEAR
# #17
user_age = int(input("ENTER AGE::"))
user_gender = input("ENTER GENDER(M/F)::")
user_matrial_status = input("ENTER MATRIAL STATUS(Y/N)::")
if user_gender == "F":
    print("YOU CAN ONLY WORK IN URBAN AREAS")
elif user_gender == "M" and user_age >= 20 and user_age < 40 :
    print("YOU ARE ELIGIBLE FOR WORK FROM ANYWHERE")
elif user_gender == "M" and user_age >=40 and user_age <= 60 :
    print("YOU ARE  ELIGIBLE FOR WORK ONLY IN URBAN AREAS")
else:
    print("ERROR")
# ENTER AGE::40
# ENTER GENDER(M/F)::M
# ENTER MATRIAL STATUS(Y/N)::Y
# YOU ARE  ELIGIBLE FOR WORK ONLY IN URBAN AREAS