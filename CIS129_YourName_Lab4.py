# Module 4 Lab-4
# Nelson Sandoval
# 09/24/2024
# Figures out the bonus amount based on store success 

# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase
prompt = 'what are the monthly sales ' # prompt will be a string literal

    

# This code gets the monthly sales

monthlySales = float(input(prompt))

# This code determines the store bonus

if monthlySales >= 110_000:
	storeAmount = 6_000
elif monthlySales >= 100_000:
	storeAmount = 5_000
elif monthlySales >= 90_000:
	storeAmount = 4_000
elif monthlySales >= 80_000:
	storeAmount = 3_000
else:
	storeAmount = 0



# This code gets the percent of increase in sales
salesIncrease = float(input('what is the sales increase '))
salesIncrease = salesIncrease / 100


# This code determines the employee bonus
if salesIncrease >= .05:
	empAmount = 75
elif salesIncrease >= .04:
	empAmount = 50
elif salesIncrease >= .03:
	empAmount = 40
else:
	empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000 ) and (empAmount == 75):
	print('Congrats! You have reached the highest bonus amounts possible! ')
