# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

def enter_parameters(account_type):
    print("-" * 50)
    print(f"Enter the details of the {account_type} account.")
    while True:
        acct_balance = input("Enter the initial balance of the savings account: ")
        if acct_balance.isdigit():
            acct_balance = float(acct_balance)
            break
        else:
            print("Please enter a valid number.")

    while True:
        acct_interest_rate = input("Enter the interest rate of the savings account: ")
        if acct_interest_rate.isdigit():
            acct_interest_rate = float(acct_interest_rate)
            break
        else:
            print("Please enter a valid number.")
    
    while True:
        acct_months = input("Enter the length of months the savings account has been open: ")
        if acct_months.isdigit() and int(acct_months) > 0:
            acct_months = int(acct_months)
            break
        else:
            print("Please enter a valid number.")
    
    return (acct_balance, acct_interest_rate, acct_months)

def display_account_data(account_type, account):
    print("-" * 50)
    print(f"Here are the details of the {account_type} account.")
    print(f"Interest Earned: $", format(account.get_interest(), ',.2f'))
    print(f"Updated Balance: $", format(account.get_balance(), ',.2f'))
    print("-" * 50)
    print("-" * 50)

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    set_parameters = enter_parameters("Savings")
    

    # Call the create_savings_account function and pass the variables from the user.
    my_sav_acct = create_savings_account(set_parameters[0], set_parameters[1], set_parameters[2])

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    display_account_data("Savings", my_sav_acct)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    set_parameters = enter_parameters("CD")

    # Call the create_cd_account function and pass the variables from the user.
    my_cd_acct = create_cd_account(set_parameters[0], set_parameters[1], set_parameters[2])

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    display_account_data("CD", my_cd_acct)
    print("-" * 50 + "\n")

if __name__ == "__main__":
    # Call the main function.
    main()
