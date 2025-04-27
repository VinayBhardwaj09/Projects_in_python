print("Welcome to TICKET BOOKING PORTAL")
name=input("Enter your Name:")
movie_seats={1:150, 2:147, 3:170}
movie_price={1:150, 2:190, 3:170}
while True:
    print('''Select a movie of your chhoice  
                1. Fighter      2. SkyForce
                3. Venom''')
    movie=int(input("Select the serial number of that movie:"))
    if 1<=movie<=3: 
        if movie == 1:
            print(f"Dear {name} you choose Fighter. ")   
        elif movie == 2:
            print(f"Dear {name} you choose SkyForce. ")
        elif movie == 3:
            print(f"Dear {name} you choose Venom. ")
        break
    else :
        print("Something went wrong")
        print("Select serial number accordingly")


seats=int(input("How many seats you want to book:"))
price=movie_price[movie]*seats
GST=price*(18/100)

print(f'''Your price of {seats} seats = {price}
        Tax = 18%
        Total = {GST+price} ''')
confirm=input("Do you want to proceed(Y/N)")
if confirm.lower() == 'y':
    print(f"Dear {name} your booking is successful.")
    print("Thank you & visit again")
else:
    print("You choose something wrong")
    
