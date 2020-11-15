 
import random
import string
import math

# code to understand accounting
#

#Straightline depreciation method


def straightline(cost, useful, salvaged):
	return (cost - salvaged) / useful

# Units of output method
def unitproduced(cost, salvaged, units, unitsperyear):
	return ((cost - salvaged) / units ) * unitsperyear


#Calculate APR: 

def apr(discount, rate, money, time):
	new_money = 0
	new_rate = 0
	if discount == 0:
		return "APR is: {apr} %".format(apr = ((money * rate) / (money * time)) * 100 )

	else:
		discount_amt = money * discount
		new_money = money - discount_amt  # this is the discounted price
		print("You're only getting ${new_money} out of ${money}. You must return the full amount of ${money}".format(new_money = new_money, money = money))

		new_APR = discount_amt / new_money
		return "APR is {new_APR}%".format(new_APR = round(new_APR * 100, 2))

# calculate straight interest

def straight_interest(principal, rate, time):
	interest_paid = principal * rate * time
	per_month = interest_paid / 12
	return "Interest paid per year: ${interest} or ${amt_month} per month".format(interest = interest_paid, amt_month= per_month)

# Calculate disposal of depreciable assets

def disposal(book_value, residual, acc_dep, sold):
	#accumulated depreciation

	cost = book_value + acc_dep
	print("original cost is ${cost}".format(cost = cost))

	net_book = book_value - acc_dep

	sale = sold - net_book

	if sale < 0:
		return "Loss for {sale}".format(sale=sale)
	else:
		return "Gain for {sale}".format(sale=sale)

# Goodwill
def goodwill(purchase, liabilities, fv_assets):
	fv_net = fv_assets -liabilities
	goodwill = purchase - fv_net
	return "Goodwill is ${gw}".format(gw = goodwill)


#Profit margin 

def profit_margin(gross_profit_ratio, production_cost):
	gpr = gross_profit_ratio / 100

	return "You should sell for ${ans}".format(ans= round(production_cost / (1-gpr), 2))

#double decline rescursion 

def double_recursion(rate, begin_cost, dep_exp, accumulated, ending, years, salvaged, original_cost):
	#Base case: 
	ade = dep_exp
	
	if years > 0: 
		if years == 2:
			prev_accu = accumulated

			accumulated = original_cost - salvaged

			dep_exp = math.ceil(accumulated - prev_accu)

			begin_cost = ending
			ending = begin_cost - dep_exp
			ade = dep_exp + accumulated
			print(begin_cost, rate, dep_exp,accumulated, ending)
			


			#ade = double_recursion(rate, begin_cost,dep_exp,accumulated,ending, years - 1, salvaged, original_cost)
		else: 

			
			begin_cost = ending
			dep_exp = math.ceil(begin_cost * rate)
			accumulated = accumulated + dep_exp
			ending = begin_cost - dep_exp
			ade +=dep_exp 
			print(begin_cost, rate, dep_exp,accumulated, ending)
			
			double_recursion(rate, begin_cost,dep_exp,accumulated,ending, years - 1, salvaged, original_cost)
			


	else:
		print("ADE is: ",ade)


		



#double decline method


def double_decline(cost, useful,salvaged):

	straightline_rate = 1 / useful

	double_rate = round(straightline_rate * 2, 2)

	print("Calculating ADE over the course of {useful} years....".format(useful = useful))

	#calculate first year data to feed in the recursion method

	dep_exp = int(cost * double_rate)
	accumulated= int(dep_exp) + 0
	ending = int(cost) - int(accumulated)
	original_cost = cost
	print("NBV| Factor | dep_exp | accumulated | Ending NBV|")
	print(cost, double_rate, dep_exp,accumulated, ending)

	
	double_recursion(double_rate, cost,dep_exp,accumulated, ending, useful,salvaged,original_cost )



### Main ###-------------------------------------------------------------------------

print("Calculate Annual depreciation expense using different methods")
method = input ("Enter 1 for straightline depreciation method, 2 for units produced, or 3 for Double decline method, 4 for Disposal assets, 5 for APR, 6 for Straight interes, 7 for goodwill, 8 for profit margin>> ")

method = int(method)

if method == 1: 
	print("Using Straightline method......")
	cost = input("Enter asset cost: ")
	salvaged = input("Enter estimated salvaged amount: ")
	useful = input ("Enter estimated usefuul time in year: ")
	cost = float(cost)
	salvaged = float(salvaged)
	useful = float(useful)
	print("ADE is: ", straightline(cost, useful, salvaged))

elif method == 2: 
	print("Using Units Produced method......")
	cost = input("Enter asset cost: ")
	salvaged = input("Enter estimated salvaged amount: ")
	units = input("Enter estimated units of usage for the asset: ")
	unitsperyear = input("Enter total units produced that year: ")

	cost = int(cost)
	salvaged = int(salvaged)
	units = int(units)
	unitsperyear = int(unitsperyear)

	print("ADE is: " , unitproduced(cost, salvaged, units, unitsperyear))


elif method == 3: 
	print("Using Double Decline Balance method .......")

	cost = int(input("Enter cost of asset: "))
	useful = int(input("Enter estimated useful life: "))
	salvaged = int(input("Enter the estimated salvaged amount: "))

	print(double_decline(cost, useful, salvaged))


elif method == 4:
	print("Calculating Disposal of depreciation assets....")

	net_book = int(input("Enter book value: "))
	residual = int(input("Enter residual value: "))

	acc_dep = int(input("Enter accumulated depreciation if applicable. Enter 0 if unknown"))
	sold = int(input("How much was the asset sold for?>>"))

	print(disposal(net_book, residual, acc_dep, sold))

elif method == 5: 
	print("Calculating APR .....")
	money = int(input("Enter the amount borrowed>>"))
	discount = float(input("Enter the discount rate in decimal point (enter 0 if not applicaple) >>"))
	rate= float(input("Enter the interest rate (in decimal points) >>"))

	time = int(input("How long is the money borrowed for(years)? >>"))

	print(apr(discount,rate, money, time))
elif method == 6: 
	print("Calculating Straight Interest......")

	principal = int(input("Enter the amount borrowed>> "))
	rate = float(input("What is the rate? Enter in decimal point >>> "))
	time = int(input("How long do you have to pay? (in years) >> "))

	print(straight_interest(principal, rate, time))
	print("Remember that you still have to book the interest monthly in your account, even if you're paying it in a year")
	print("Book an interst PAYABLE on the CREDIT side with the monthly interest")
	print("Recognize an interest EXPENSE on the DEBIT side, with the same amount")

elif method == 7:
	print("Calculating Goodwill....")
	purchase = int(input("How much did the company was purchased for? >>> "))
	liabilities = int(input("How much liabilities does the company assumed? >>> "))
	fv_assets = int(input("What is the company's fair assets value? >> "))
	print(goodwill(purchase, liabilities, fv_assets))
elif method == 8:
	print("Calculating how much to sell for a product.....")
	gross_profit_ratio = int(input("What's the Gross profit ratio? enter in percentage >>> "))
	production_cost = int(input("How much did it cost to make? >>"))
	print(profit_margin(gross_profit_ratio, production_cost))

     
     
