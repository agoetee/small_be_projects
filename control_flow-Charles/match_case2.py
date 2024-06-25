# MAtch case for voter age

age = int(input("Please enter your age: "))

match age:
    case 18 | 19:
        if age >= 18:
            print("You are eligible to vote")
    case _:
        print("You are not yet elligible")