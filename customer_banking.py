# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

def is_float(str):
    str = str.replace(".", "")
    return str.isdigit()        

def pad_left_spaces(str,length):
    num_spaces = length - len(str)
    space_string = " " * num_spaces
    return space_string + str

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    is_valid_input = False
    while is_valid_input == False:
        savings_balance = input("Please enter the initial savings account balance: ")
        if is_float(savings_balance):
            is_valid_input = True
            savings_balance = float(savings_balance)

    is_valid_input = False
    while is_valid_input == False:
        savings_interest = input("Please enter the APR interest rate for the savings account: ")
        if is_float(savings_interest):
            is_valid_input = True
            savings_interest = float(savings_interest)

    is_valid_input = False
    while is_valid_input == False:
        savings_maturity = input("Please enter how many months the money is in the savings account: ")
        if savings_maturity.isdigit():
            is_valid_input = True
            savings_maturity = int(savings_maturity)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    str_savings_interest_earned = "{0:,.2f}".format(savings_interest_earned)
    str_updated_savings_balance = "{0:,.2f}".format(updated_savings_balance)
    print(f"The interest earned on the savings account is: ${pad_left_spaces(str_savings_interest_earned, len(str_updated_savings_balance)+1)}")
    print(f"The current savings account balance is       : ${pad_left_spaces(str_updated_savings_balance, len(str_updated_savings_balance)+1)}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    is_valid_input = False
    while is_valid_input == False:
        cd_balance = input("Please enter the initial CD account balance: ")
        if is_float(cd_balance):
            is_valid_input = True
            cd_balance = float(cd_balance)

    is_valid_input = False
    while is_valid_input == False:
        cd_interest = input("Please enter the APR interest rate for the CD account: ")
        if is_float(cd_interest):
            is_valid_input = True
            cd_interest = float(cd_interest)

    is_valid_input = False
    while is_valid_input == False:
        cd_maturity = input("Please enter maturity length (in months) for the CD account: ")
        if is_float(cd_maturity):
            is_valid_input = True
            cd_maturity = int(cd_maturity)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    str_cd_interest_earned = "{0:,.2f}".format(cd_interest_earned)
    str_updated_cd_balance = "{0:,.2f}".format(updated_cd_balance)
    print(f"The interest earned on the CD account is: ${pad_left_spaces(str_cd_interest_earned,len(str_updated_cd_balance)+1)}")
    print(f"The current CD account balance is       : ${pad_left_spaces(str_updated_cd_balance,len(str_updated_cd_balance)+1)}")

if __name__ == "__main__":
    # Call the main function.
    main()
