#CTI 110
#P1T2 - Salary Calculator
#Carlos Castilla Virelles
#9/15/2021

#Start

#Input the hours
hoursWorked = float(input("How many hours did you work this week?"))
hoursWorked = float((hoursWorked)) # convert to integer

#Input the hourly pay rate
hourlyPay = float(input("What's your hourly pay rate?")) # get and convert

#Calculate gross pay
grossPay = hoursWorked * hourlyPay
#Display the gross pay
print("Your gross pay for the week is: $", grossPay)
#End
