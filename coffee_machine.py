# current amount of supplies
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550

# display current machine amounts
def display(): 
    print(f"""The coffee machine has:
    {water} of water
    {milk} of milk
    {coffee_beans} of coffee beans
    {disposable_cups} of disposable cups
    {money} of money\n""")

def buy():
    global water, milk, coffee_beans, disposable_cups, money
    purchase = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    if purchase == 'back': return
    if disposable_cups == 0:
        return print("Sorry, not enough disposable cups!")
    if purchase == '1':
        if water < 250:
            return print("Sorry, not enough water!")
        elif coffee_beans < 16:
            return print("Sorry, not enough coffee beans!")
        water -= 250
        coffee_beans -= 16
        money += 4
    elif purchase == '2':
        if water < 350:
            return print("Sorry, not enough water!")
        elif milk < 75:
            return print("Sorry, not enough milk!")
        elif coffee_beans < 20:
            return print("Sorry, not enough coffee beans!")
        water -= 350
        milk -= 75
        coffee_beans -= 20
        money += 7  
    elif purchase == '3':
        if water < 200:
            return print("Sorry, not enough water!")
        elif milk < 100:
            return print("Sorry, not enough milk!")
        elif coffee_beans < 12:
            return print("Sorry, not enough coffee beans!")
        water -= 200
        milk -= 100
        coffee_beans -= 12
        money += 6
    disposable_cups -= 1
    print("I have enough resources, making you coffee!")
        
def fill():
    global water, milk, coffee_beans, disposable_cups
    amount_water = int(input("Write how many ml of water do you want to add:\n"))
    amount_milk = int(input("Write how many ml of milk do you want to add:\n"))
    amount_coffee_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
    amount_disposable_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    
    water += amount_water
    milk += amount_milk
    coffee_beans += amount_coffee_beans
    disposable_cups += amount_disposable_cups
    
def take():
    global money
    print(f"I gave you ${money}\n")
    money -= money
    
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        display()
    elif action == 'exit':
        break
