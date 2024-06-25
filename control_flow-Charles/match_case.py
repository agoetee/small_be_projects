# This program uses match case to compare the usage of if-else statements

day = input("Enter day of the week: ").lower()

match day:
    case 'monday':
        print("ugh, just another first day")
    case 'tuesday':
        print("Second day init")
    case 'wednesday':
        print('midweek is here for you')
    case 'thursday':
        print("Almost there. hold on tight")
    case 'friday':
        print('we say TGIF  yaaaaay')
    case 'saturday' | 'sunday' :
        print("Weekend vibes")
    case _:
        print('invalid day entered')