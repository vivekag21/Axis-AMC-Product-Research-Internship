def calculate_future_expenses(current_expenses, inflation_rate, time_period_years):
    # Calculate the future monthly expenses using the compound interest formula
    future_expenses = current_expenses * ((1 + inflation_rate / 100) ** time_period_years)

    return future_expenses


def calculate_retirement_value(swp_amount, years, annual_return_rate):
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = annual_return_rate / 12 / 100
    
    # Total number of months
    total_months = years * 12
    
    # Calculate the present value of the investment
    present_value = swp_amount * ((1 - (1 + monthly_interest_rate) ** -total_months) / monthly_interest_rate)
    
    return present_value


def calculate_monthly_sip(retirement_value, years_of_sip, annual_return_rate, annual_step_up):
    
    # Calculate the number of years and months of SIP
    years_of_sip = retirement_age - current_age
    months_of_sip = years_of_sip * 12
    
    # Convert annual return rate to monthly return rate
    monthly_return_rate = (1 + annual_return_rate / 100) ** (1/12) - 1
    
    # Initialize the total future value of SIPs
    total_future_value = 0
    
    # Calculate the monthly SIP required
    for year in range(1, years_of_sip + 1):
        # Calculate the monthly SIP for the current year considering the step-up
        current_sip = 1 * ((1 + annual_step_up / 100) ** (year - 1))
        
        # Add up the future value of SIP contributions for this year
        for month in range(12):
            months_left = months_of_sip - ((year - 1) * 12 + month)
            total_future_value += current_sip * ((1 + monthly_return_rate) ** months_left)
    
    # Calculate the required monthly SIP amount
    required_sip = retirement_value / total_future_value
    
    return required_sip


# Input Basics
current_age = int(input("\nEnter your current age: "))
retirement_age = int(input("Enter your retirement age: "))

# Years left to retire
time_period_years = retirement_age - current_age

print(f"{time_period_years} years left to your retirement ")

# Expected years to live post retirement age
years_after_retirement = int(input("\nEnter the number of years you expect to live after retirement: "))


# Calculate the duration the funds will last
response = input("For manually entering SWP amount, Type 'y' else for calculating Type 'n': ")
if response == 'y':
    swp_amount = float(input("Enter the monthly withdrawal amount (₹): "))
if response == 'n':
    current_expenses = float(input("Enter your total present monthly expenses (₹): "))
    inflation_rate = float(input("Enter the expected annual inflation rate (%): "))
    inflation_adjusted_monthly_expenses = calculate_future_expenses(current_expenses, inflation_rate, time_period_years)
    swp_amount = int(inflation_adjusted_monthly_expenses)

# expected annual return rate on your investments
annual_return_rate = float(input("Enter the expected annual return rate on your investments post-retirement (as a percentage): "))

years = years_after_retirement

# Calculate the value of investments on retirement
retirement_value = calculate_retirement_value(swp_amount, years, annual_return_rate)
retirement_value = int(round(retirement_value, 0))

print(f"\nThe corpus you need to build at the age of {retirement_age} for an expected retirement life is {retirement_value}.")


# Inputs for current investments --> SIP
print("Find out how much you need to invest per month to achieve your goal amount.")
years_of_sip = time_period_years 
annual_return_rate = float(input("\nEnter the expected annual return rate (as a percentage) on your SIP: "))
annual_step_up = float(input("Enter the expected annual top-up in SIP (as a percentage): "))

# Calculate the required monthly SIP
required_monthly_sip = calculate_monthly_sip(retirement_value, years_of_sip, annual_return_rate, annual_step_up)

# Display the results
print(f"\nTo achieve a future value of ₹{retirement_value:,.2f} by the age of {retirement_age},")
print(f"you need to start with a monthly SIP of approximately ₹{required_monthly_sip:,.2f},")
print(f"with an yearly top-up of {annual_step_up}%, assuming your money grows at a rate of {annual_return_rate}% p.a. for the next {time_period_years} years.")