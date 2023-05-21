amount=int(input("Enter current amount: "))
daily_profit=(amount*2.25)/100
vipcash=((amount*2.25)/100)*0.15
weekly_rebate= 0
for i in range(0,30):
    print("Day ",i,":",amount+daily_profit+vipcash+weekly_rebate)
    amount=amount+daily_profit
    if i%7==0 :
        weeklyrebate=1300
        weekly_rebate=weekly_rebate*1.7