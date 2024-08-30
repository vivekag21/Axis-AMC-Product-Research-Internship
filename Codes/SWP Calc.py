# Get inputs from the user
initial_amount = float(input("Enter the initial amount (₹): "))
principal_left = initial_amount
monthly_withdrawal = float(input("Enter the monthly withdrawal amount (₹): "))
duration_years = int(input("Enter the duration (years): "))
duration = duration_years * 12  # Convert years to months
annual_return = float(input("Enter the expected annual return rate (as a percentage): "))
expected_return = annual_return / 12 / 100  # Convert annual return rate to monthly return rate

runway_time = 0

# Loop to simulate the monthly withdrawals and interest compounding
while principal_left > 0 and runway_time < duration:
    # Apply the monthly return on the current principal
    principal_left *= (1 + expected_return)
    
    # Subtract the monthly withdrawal
    principal_left -= monthly_withdrawal
    
    # Check if the principal left goes below zero
    if principal_left < 0:
        principal_left = 0
    
    # Increment the runway time (number of months)
    runway_time += 1

Cumulative_withdrawals = monthly_withdrawal*runway_time
# Print the total time for which withdrawals can be sustained
print(f"Runway Time (in months): {runway_time}")
print(f"Principal left: {principal_left}")
print(f"Cumulative withdrawals to date: {Cumulative_withdrawals}")

