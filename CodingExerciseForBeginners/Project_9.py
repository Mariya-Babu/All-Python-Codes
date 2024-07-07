# Project_9
#Virtual Coffee Machine

def report(profit,ingredients):
    print(f"Water : {ingredients['water']}")
    print(f'Milk : {ingredients["milk"]}')
    print(f"Coffee : {ingredients['coffee']}")
    print(f'Money : {profit}')

def checkResources(coffee,MENU):
    flag = True
    if Ingredients['water'] < MENU[coffee]['ingredients']['water']:
        flag = False
    if Ingredients['milk'] < MENU[coffee]['ingredients']['milk']:
        flag = False
    if Ingredients['coffee'] < MENU[coffee]['ingredients']['coffee']:
        flag = False
    
    return flag

MENU = {
    'expresso' : {
        'ingredients' : {
            'water' : 50,
            'milk' : 0,
            'coffee' : 18,
        },
        'cost' : 100
    },
    'latte' : {
        'ingredients' : {
            'water' : 200,
            'milk' : 150,
            'coffee' : 24,
        },
        'cost' : 100
    },
    'cappuccino' : {
        'ingredients' : {
            'water' : 250,
            'milk' : 100,
            'coffee' : 24,
        },
        'cost' : 200
    }
}

Ingredients = {
    'water' : 1000,
    'milk' : 500,
    'coffee' : 150
} 


print("Virtual Coffee Machine!")
profit = 0
flag = True
while flag :
    coffee_type = input('What would you like to have ? (latte/expresso/cappuccino) : ').lower()
    if coffee_type in MENU:
        resources_avaliable = checkResources(coffee_type,MENU)
        if resources_avaliable:
            cost = MENU[coffee_type]["cost"]
            print(f'Please insert coins Value {cost}')
            R5 = int(input('How many 5Rs. coins : '))
            R10 = int(input("How many 10Rs. coins : "))
            R20 = int(input('How many 20Rs. coins : '))
            user_amount = R5 * 5 + R10 * 10 + R20 * 20
            if user_amount < cost :
                print(f'Sorry that\'s not enought monkey. Money refunded')
            else:
                if user_amount > cost:
                    print(f'Here is your Rs {user_amount - cost} in change.')
                print(f'Here is your {coffee_type}')
                profit += cost
                Ingredients['water'] -= MENU[coffee_type]['ingredients']['water']
                Ingredients['milk'] -= MENU[coffee_type]['ingredients']['milk']
                Ingredients['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
                    
        else:
            print("Sorry there is not enough resources are available ")
    elif coffee_type == 'report':
        report(profit,Ingredients)
    elif coffee_type == 'off':
        flag = False
        print(f"Programme completed successfully and your profit is {profit}")
    else:
        flag = False
        print("Invalid Entry....")
        