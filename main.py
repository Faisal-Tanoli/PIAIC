# print("hello world !")
# favourite_celebrity="Umer"
# favourite_food= "biryani"
favourite_game='football'
favourite_player='ronaldo'
# print(favourite_celebrity)
# print(favourite_food)
# print(favourite_game)
# print(favourite_player)


# F String and arithmatic operators 
name = "Faisal"
age = 25
# print(f"My name is  {name}  and I am {age**2} years old.")

# Write email with DOC STRING and F string in case of using variable in string

# print(f"""Hi 
# my name is {name} ,favourite game is {favourite_game} 
# and favourite player is {favourite_player}
# What about you """)

# # Assignment Operators 
# num1=10
# num2 = 0
# num3 = 5
# num4 = 20

# num1+=10   # num1=20
# num2-=num1 
# num3*=num1
# num4/=num1
# print(num1,num2,num3,num4)

# outpout 20, -20,100,1

# python main.py
# Conditional operator / Conditional Statement if else 
# output is always boolean which is only true and false 
# What is benefit ? 
# after : colon there is BlOCK of code ( multiple statements)
# age=28
# if age >= 18: 
#     print("you are allowed")
# elif age < 18 : print("You are not allowed")

# identation (in python {} is replaced with indentation so that after : all statements will be in BLOCK )

# Marks=80
# CGPA=2.8
# Marks = input("Enter Marks ")
# print(f"Your Marks are {Marks}")
# marks = int(Marks)
# if marks >60 and marks <100:
#     print("you are qualifed")
#     print("Welcome to the show")
# else:
#     print("Better luck next time")

# What is type casting and what is implicit type casting

# AND operatoer follow true and true means all conditions must be true to get end result true
# Make program to ask Marks or CGPA  and Show Grade 

Select = input("Select marks or cgpa: ")

if Select == "marks":
    marks = input("Enter your Marks: ")
    Marks = int(marks)
    if 70 <= Marks < 80:
        print("Your Grade is B")
    elif 80 <= Marks < 90:
        print("Your Grade is A")
    elif 90 <= Marks <= 100:
        print("Your Grade is A-1")
    elif Marks > 100:
        print("You are over Qualified")
    else:
        print("You are FAIL")
elif Select == "cgpa":
    cgpa = input("Enter your CGPA: ")
    CGPA = float(cgpa)
    
    if 2 <= CGPA < 2.5:
        print("Your Grade is B")
    elif 2.5 <= CGPA < 3:
        print("Your Grade is A")
    elif 3 <= CGPA <= 4:
        print("Your Grade is A-1")
    elif CGPA > 4:
        print("You are over Qualified")
    else:
        print("You are FAIL")
else:
    print("Invalid Entry")
    exit()
#Home work Make grading system ---Assignment 1st- Class 3rd