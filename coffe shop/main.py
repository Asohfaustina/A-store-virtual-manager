import functions
import time

print("WELCOME TO ZION'S COFFE SHOP \n BELOW IS THE MENU \n 1. Espresso \n 2. Latte \n 3. cappuccino")

serving = True
while serving==True:
    coffeChoice = input("What would you like to have , type the number: ").lower()
    if coffeChoice=="1":
        functions.check("espresso")
        functions.process_order('espresso')
    elif coffeChoice=="2":
        functions.check("latte")
        functions.process_order("latte")
    elif coffeChoice=="3":
        functions.check("cappuccino")
        functions.process_order("cappuccino")
    elif coffeChoice=="end":
        functions.off_coffe()
    elif coffeChoice=="report":
        functions.report()
    else:
        print("we dont have what you've ordered.. or type the correct number of item you want")
        time.sleep(3)