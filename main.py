MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


coins={
 'quarter':0.25,
 'dime' : 0.10,
 'nickles':0.05,
 'penny' :0.01
    
}

#ask selecion

turn_off = False


#check what resources are needed.
  #check there is enough

while turn_off==False:

    def start():
        askSelection = input('What would you like? (espresso/latte/cappuccino) ')
        if askSelection == "show report":
            show_report()
        elif askSelection == 'espresso' or askSelection == 'latte' or askSelection == 'cappuccino':
             compareCash(askSelection) 
        elif askSelection =='off':
            turnOff()
        else:
            print('please enter the correct selection') 
            start()   


    def turnOff(turn_off):
          print('end')
          turn_off=True
          
    
    def check_resources(askSelection,change):
        for key,value_list in MENU[askSelection]['ingredients'].items():
                # print(key,value_list) # key will ist the keys eg water, value list - the amount
                # print(resources[key],'res') # show will keys exisit
                if resources[key] > value_list:
                   
                   resources[key] = resources[key] - value_list
                     
                else:
                    print(f'sorry there is not enough {key} ')
               
        print(f'there is your drink change is ,{"{:.2f}".format(change)}')
        
        
    


    def insert_coins():
        newList=[]
    
        for items,value_list in coins.items():
          
          ask_which_coins = int(input(f'how many {items}'))
          
          newList.append(float((ask_which_coins * value_list))) 
        #list full of values - need to add together and compare

        total = sum(newList)
        return total 

    
    def compareCash(askSelection):
        userCoins=insert_coins()
        change=0
        drink = MENU[askSelection]['cost']
        
        if(drink < userCoins):
            change = userCoins - drink
            check_resources(askSelection,change)
            
        else:
            print(f'you dont have enough cash, you only inserted {userCoins}, you need {drink}-refunded.')
        



    
    def show_report():
        for items,value_list in resources.items():
            print(items,value_list)
            
    
    start() 






    

        
    #loop through what there is 
    #if enough deduct it.



    #minus resources needed - user selection









