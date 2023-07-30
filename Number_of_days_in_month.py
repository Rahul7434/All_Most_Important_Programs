month=input("Enter month    and check how many Days in that month")

if month=='Jan' or month=='March' or month=='May' or month=='July' or month=='August' or month=='Octomber' or month=='December':
    print('31 days!!!')
elif month=='Feb':
    print('28-29 days')
else:
    print("30 days")
