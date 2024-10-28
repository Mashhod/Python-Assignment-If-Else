# If Else

try:            
    date = int(input("Enter Your Birth Date: "))
    month = int(input("Enter Your Birth Month:"))
    if month > 0 and date > 0:
        if (month == 1  and  date <= 19) or (month == 12  and  date >= 22):
            print("Your Zodioc sign is Capricon")

        elif (month == 1  and  date >= 20) or (month == 2  and  date <= 18):
            print("Your Zodioc sign is Aquqrius")
        
        elif (month == 2  and  date >= 19) or (month == 3  and  date <= 20):
            print("Your Zodioc sign is Pisces")    

        elif (month == 3  and  date >= 21) or (month == 4  and  date <= 19):
            print("Your Zodioc sign is Aries")

        elif (month == 4  and  date >= 20) or (month == 5  and  date <= 20):
            print("Your Zodioc sign is Taurus")

        elif (month == 5  and  date >= 21) or (month == 6  and  date <= 21):
            print("Your Zodioc sign is Gemini")

        elif (month == 6  and  date >= 22) or (month == 7  and  date <= 22):
            print("Your Zodioc sign is Cancer")

        elif (month == 7  and  date >= 23) or (month == 8  and  date <= 22):
            print("Your Zodioc sign is Leo")

        elif (month == 8  and  date >= 23) or (month == 9  and  date <= 22):
            print("Your Zodioc sign is Virgo")

        elif (month == 9  and  date >= 23) or (month == 10  and  date <= 23):
            print("Your Zodioc sign is Libra")

        elif (month == 10  and  date >= 24) or (month == 11  and  date <= 21):
            print("Your Zodioc sign is Scorpio")

        elif (month == 11  and  date >= 22) or (month == 12  and  date <= 21):
            print("Your Zodioc sign is Sagittarius")
    else:
        print("Plaease enter month & date greater than 0")

        

except ValueError:
    print('Please enter date and month in numbers')
