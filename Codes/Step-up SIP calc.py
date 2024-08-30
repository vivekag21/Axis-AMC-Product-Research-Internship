import matplotlib.pyplot as plt

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


def create_doughnut_chart(value1, value2, label1="Invested Amount", label2="Estimated Returns"):
    # Data to plot
    values = [value1, value2]
    labels = [label1, label2]
    colors = ['#1E90FF', '#B0C4DE']  # Custom colors similar to the chart you provided
    
    # Plotting the pie chart
    plt.figure(figsize=(4.5, 4.5))
    plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white'})

    # Draw a white circle at the center to create a doughnut shape
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis('equal')
    
    # Title of the chart
    plt.title('SIP Returns Calculator')
    
    # Show the plot
    plt.show()
# Input parameters

monthly_investment = float(input("Enter the monthly investment amount: "))
annual_increase_rate = float(input("Enter the annual increase rate (in percentage): "))
investment_duration = int(input("Enter the investment duration (in years): "))
annual_return_rate = float(input("Enter the expected annual return on investment (in percentage): "))

# Calculate future value
future_value = future_value_sip(
    monthly_investment,
    annual_increase_rate,
    investment_duration,
    annual_return_rate
)
total_invested_amount = monthly_investment*investment_duration*12
value1 = total_invested_amount
# value2 = float(input("Enter the second value: "))
value2 = future_value-total_invested_amount

print(f"The future value of the SIP investment is: {future_value:.2f}")
create_doughnut_chart(value1, value2)

