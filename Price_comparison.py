zomato={1:80,2:50,3:45,4:119,5:80,6:159,7:60,8:80,9:40,10:20,11:20,12:20}
swiggy={1:60,2:40,3:55,4:109,5:85,6:149,7:50,8:90,9:60,10:10,11:10,12:10}
menu={1: "Cold Coffee",     2: "Burgur",
      3: "Hot Coffee",      4:"Veg Corn Pizza",
      5: "Chilli Potato",   6: "Paneer Pizza",
      7: "Momos",           8: "Veg Paneer Roll",
      9: "Cold Drink",     10: "Punjabi Tadka",
     11: "Aloo Bhujia",    12: "Chips"}
print('''                     MENU
      1. Cold Coffee     2. Burgur
      3. Hot Coffee      4. Veg Corn Pizza
      5. Chilli Potato   6. Paneer Pizza
      7. Momos           8. Veg Paneer Roll
      9. Cold Drink     10. Punjabi Tadka
     11. Aloo Bhujia    12. Chips
''')

while True:
    item=int(input("Select an item number from menu:"))
    if 1<=item<=12:
        print(f'''         ON Zomato                     On swiggy
              {menu[item]} = {zomato[item]}           {menu[item]} = {swiggy[item]}     ''')
        
        while True:
            order=(int(input("Press 1 for Zomato or 2 for Swiggy:")))
            if order in [1,2]:
              break
            else:
                 print("Invalid choice! Please select 1 for Zomato or 2 for Swiggy.")            
        if order==1:
            print("You are on Zomato.")
            name=input("Enter your name:")
            num=input("Enter contact number:")
            address=input("Enter delivary address:")
            print(f'''Dear {name}, We have noted your order as
            Item name = {menu[item]}  
            Item cost = {zomato[item]}
            Delivary charges = 50
            Total AMT = {zomato[item]+50}''')
        elif order==2:
            print("You are on Swiggy.")
            name=input("Enter your name:")
            num=input("Enter contact number:")
            address=input("Enter delivary address:")
            print(f'''Dear {name}, We have noted your order as
            Item name = {menu[item]}  
            Item cost = {swiggy[item]}
            Delivary charges = 50
            Total AMT = {swiggy[item]+50}''')
    else :
        print("you select wrong item.")
    break
pay={1:"online",2:"cash on delivary"}
payment=int(input('''Select a payment method
              1.Online
              2.Cash on delivary
              '''))
print(f'''Thank you 
      Your payment method is {pay[payment]}
please hang in
We are there with your order in few moments ''')
