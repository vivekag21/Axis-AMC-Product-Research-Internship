import matplotlib.pyplot as plt
import numpy as np

def calculate_sip_value(monthly_investment, investment_duration_years, delay_in_months, expected_return_rate):
    # Convert years to months
    total_months = investment_duration_years * 12
    rate_per_month = expected_return_rate / 12 / 100  # Monthly return rate
    
    # SIP value if started immediately
    sip_value_no_delay = 0
    for i in range(1, total_months + 1):
        sip_value_no_delay += monthly_investment * pow(1 + rate_per_month, total_months - i + 1)
    
    # SIP value if delayed
    sip_value_with_delay = 0
    for i in range(1, total_months - delay_in_months + 1):
        sip_value_with_delay += monthly_investment * pow(1 + rate_per_month, total_months - delay_in_months - i + 1)
    
    # Total invested amounts
    total_invested_no_delay = monthly_investment * total_months
    total_invested_with_delay = monthly_investment * (total_months - delay_in_months)
    
    return total_invested_no_delay, sip_value_no_delay, total_invested_with_delay, sip_value_with_delay

# Input parameters
monthly_investment = float(input("Enter the monthly investment amount (₹): "))
investment_duration_years = int(input("Enter the investment duration (years): "))
delay_in_months = int(input("Enter the delay in starting SIP (months): "))
expected_return_rate = float(input("Enter the expected annual return rate (as a percentage): "))

# Calculate SIP values
total_invested_no_delay, sip_value_no_delay, total_invested_with_delay, sip_value_with_delay = calculate_sip_value(
    monthly_investment,
    investment_duration_years,
    delay_in_months,
    expected_return_rate
)

# Data for bar graphs
categories = ['No Delay', f'Delay of {delay_in_months} Months']
invested_amounts = [total_invested_no_delay, total_invested_with_delay]
expected_returns = [sip_value_no_delay - total_invested_no_delay, sip_value_with_delay - total_invested_with_delay]

x = np.arange(len(categories))  # the label locations
width = 0.35  # the width of the bars

# Plotting the bar graphs
fig, ax = plt.subplots(figsize=(10, 6))

bars_invested = ax.bar(x - width/2, invested_amounts, width, label='Invested Amount')
bars_return = ax.bar(x + width/2, expected_returns, width, label='Expected Return')

# Adding text for labels, title, and custom x-axis tick labels
ax.set_xlabel('Scenario')
ax.set_ylabel('Amount (₹)')
ax.set_title('Invested Amount and Expected Return Comparison')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Adding the data values on top of the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:,.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars_invested)
add_labels(bars_return)

# Display the plot
plt.tight_layout()
plt.show()
