"""
This program displays mobile money USSD 
"""
account_balance = 100

def display_main():
    print("1. Transfer Money")
    print("2. MomoPay&Pay Bill")
    print("3. Airtime&Bundles")
    print("4. Allow Cash Out")
    print("5. Financial Services")
    print("6. My Wallet")
    print("7. Exit")

def transfer_money_display():
    print("Transfer Money")
    print("1. MOMO User")
    print("2. Non MoMo User")
    print("3. Send with Care")
    print("4. Favorites")
    print("5. Other Networks")
    print("6. Bank Account")
    print("0. Back")


def momo_user(number, repeat, amount):
    if number == repeat:
        global account_balance
        if account_balance >= amount: 
            account_balance -= amount
            print(f"Cash out: {amount} added. Balance: ${account_balance}")
            return account_balance
        else:
            print("Balance insufficient")

def non_momo(number, repeat, amount):
    if number == repeat:
        global account_balance 
        account_balance -= amount
        print(f"Cash out {amount} to other network {number}. Balance: {account_balance}")
        return account_balance

def send_with_care():
    pass
def favorites():
    pass
def other_network():
    pass
def bank_account():
    pass

def momopay_bill_display():
    print("MomoPay&Pay Bill")
    print("1. MoMoPay")
    print("2. Pay Bill")
    print("3. GhQR")
    print("4. Fuels")
    print("5. Ghana.GOV")
    print("0. Back")

def airtime_bundles_display():
    print("Airtime& Bundles")
    print("1. Airtime")
    print("2. Internet Bundles")
    print("3. Fixed Broadband")
    print("4. Schedule Airtime")
    print("5. Just4U")
    print("0. Back")

def allow_cashout_display():
    print("Allow Cash Out")
    print("1. Yes")
    print("2. No")
    print("0. Back")

def financial_service_display():
    print("Financial Services")
    print("1. Bank Services")
    print("2. Savings")
    print("3. Loans")
    print("4. Pensions and Investments")
    print("5. Insurance")
    print("6. Trade Shares")
    print("0. Back")

def my_wallet_display():
    print("My Wallet")
    print("1. Check Balancs")
    print("2. Allow Cash Out")
    print("3. My Approvals")
    print("4. Report Fraud")
    print("5. Statements")
    print("6. Change&Reset PIN")
    print("7. Upgrade Profile Type")
    print("# for next")

def my_wallet_two_display():
    print("8. Reversals")
    print("9. Check Wallet Limits")
    print("10. Favorite")
    print("11. Name&Next of Kin")
    print("0. Back")

def back_or_exit_display():
    print("1. Back to main")
    print("2. Exit")


def main():
    while True:
        display_main()
        input_main = input("")
        match input_main:
            case "1":
                transfer_money_display()
                transfer_money_input = input(":")
                match transfer_money_input:
                    case "1":
                        number = input("Enter number: ")
                        repeat = input("Repeat number: ")
                        amount = int(input("Amount: "))
                        momo_user(number, repeat, amount)
                        back_or_exit_display()
                        back_or_exit_input = input("")
                        match back_or_exit_input:
                            case "1":
                                display_main()
                            case "2":
                                print("Thank you for using the service. Byee")
                                break
            case "2":
                momopay_bill_display()
            case "3":
                airtime_bundles_display()
            case "4":
                allow_cashout_display()
            case "5":
                financial_service_display()
            case "6":
                my_wallet_display()
            case "7":
                print("Thank you for using the service")
                break
                
            case _:
                print("Enter a valid input")
                
main()
