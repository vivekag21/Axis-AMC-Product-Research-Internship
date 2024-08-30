def calculate_lumpsum_growth(initial_investment, annual_return_rate, time_period_years):
    # Calculate the future value
    future_value = initial_investment * ((1 + annual_return_rate / 100) ** time_period_years)
    
    return future_value


def future_value_sip(monthly_investment, annual_increase_rate, years, annual_return_rate):
    total_amount = 0
    months = years * 12
    monthly_return_rate = annual_return_rate / 12 / 100  # Convert annual return rate to monthly
    step_up_months = 12  # SIP step-up occurs annually

    for month in range(1, months + 1):
        # Calculate the number of years that have passed to determine the step-up
        year = (month - 1) // step_up_months + 1
        
        # Update the monthly investment amount for the current year
        current_investment = monthly_investment * (1 + annual_increase_rate / 100) ** (year - 1)
        
        # Calculate the future value of this month's investment
        months_left = months - month + 1
        amount = current_investment * ((1 + monthly_return_rate) ** months_left)
        
        total_amount += amount
    
    return total_amount


# Monthly Expenses on retirement
def calculate_future_expenses(current_expenses, inflation_rate, time_period_years):
    # Calculate the future monthly expenses using the compound interest formula
    future_expenses = current_expenses * ((1 + inflation_rate / 100) ** time_period_years)

    return future_expenses

# The post retirement time period until which the amount invested till retirement lasts 
def calculate_swp_duration(initial_amount, monthly_withdrawal, annual_return_rate, anticipated_retirement_years):
    months = 0
    monthly_return_rate = annual_return_rate / 12 / 100  # Convert annual return rate to monthly

    # The money is withdrawn at the end of each month.
    while initial_amount > 0:
        initial_amount = initial_amount * (1 + monthly_return_rate) - monthly_withdrawal
        months += 1

        # If the balance goes negative, break and adjust the final count
        if initial_amount < 0:
            initial_amount = 0
            break
        
        if months >= anticipated_retirement_years*12:
            print(f"The funds will sustain for over {anticipated_retirement_years} years.") 
            print(f"You'll still have {initial_amount} amount left!")
            return -1
    return months




# Calculating returns on an initial single lumpsum investment 
current_age = int(input("\nWhat is your current age? "))
retirement_age = int(input("At what age do you wish to retire? "))
time_period_years = retirement_age - current_age
initial_investment = float(input("Enter the initial lump sum investment (₹): "))
if initial_investment > 0:
    annual_return_rate = float(input("Enter the expected annual return rate (%): "))

    Lumpsum_future_value = calculate_lumpsum_growth(initial_investment, annual_return_rate, time_period_years)

    print(f"\nThe future value of your investment after {time_period_years} years will be: ₹{Lumpsum_future_value:,.2f}")
else:
    Lumpsum_future_value = 0   # the value of variable 'Lumpsum_future_value' is a must to define for further code


# Inputs required to calculate the final step up SIP amount on termination.
monthly_investment = float(input("\nEnter the monthly investment amount: "))
annual_increase_rate = float(input("Enter the annual top-up rate (in percentage): "))
annual_return_rate = float(input("Enter the expected annual return on investment (in percentage): "))
investment_duration = time_period_years

# Calculate future value of SIPs
SIP_future_value = future_value_sip(monthly_investment, annual_increase_rate, investment_duration, annual_return_rate)

# Prints the future value of the Monthly SIPs made
print(f"\nThe future value of the SIP investment is: {SIP_future_value:.2f}")

# The cumulative value from Lumpsum and SIP investment
total_future_value = Lumpsum_future_value + SIP_future_value
total_future_value = int(round(total_future_value, 0))
print(f"\nThe future value of the total invested corpus is: {total_future_value:.2f}")


# Understanding your monthly expenses post your Retirement life adjusting inflation.
current_expenses = float(input("\nEnter your current monthly expenses (₹): "))
inflation_rate = float(input("Enter the expected annual inflation rate (%): "))
time_period_years = time_period_years


# Calculating monthly future expenses
monthly_future_expenses = calculate_future_expenses(current_expenses, inflation_rate, time_period_years)
monthly_future_expenses = int(round(monthly_future_expenses, 0))
print(f"\nYour expected monthly expenses after {time_period_years} years will be: ₹{monthly_future_expenses:,.2f}")

# Understanding for how long will the invested money last wrt the money grown till retirement.
monthly_expenditure = monthly_future_expenses


# Final SWP withdrawls
initial_amount = total_future_value
monthly_withdrawal = monthly_future_expenses
annual_return_rate = float(input("\nEnter the annual return rate expected post retirement(%): "))
anticipated_retirement_years = int(input("How many years do you expect to spend in retirement? "))


duration_months = calculate_swp_duration(initial_amount, monthly_withdrawal, annual_return_rate, anticipated_retirement_years)
# The loop won't end if the monthly expenses are not huge enough to exhaust the invested amount.
if duration_months != -1:
    print(f"\nThe money will last for approximately {duration_months // 12} years and {duration_months % 12} month, post-retirement age of {retirement_age}.")
