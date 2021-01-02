#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip claculator")
bill=float(input("Enter the total bill amount :$"))
tip_percent=int(input("Enter the tip percentage 10, 12 or 15: "))
people=int(input("Enter number of people to split: "))
tip_percent/=100
tip_amount=(bill/people)*(tip_percent+1)
print(f"Each person should pay ${round(tip_amount,2)}")
