user_choice = 0
import random
myGro = [] 

def add_item(): 
    n = str(input("Enter the items of your choice: "))
    myGro.append(n) 
    print(f"Item:'{n}' added to the grocery list")
def display_list(): 
    count = 0
    for Gro in myGro:
        count += 1
        print(f"{count}. {Gro}")
    print("-------------------------------------")       
def delete():
    deletion = input("Enter an item you want to remove (Must exist within the list)")
    myGro.remove(f"{deletion}")



while user_choice !=4:
    print("1. Add an item")
    print("2. View the list")
    print("3. Remove an item")
    print("4. Exit")
    user_choice = int(input("Enter your choice:"))

    match user_choice:
        case 1: 
            add_item()
        case 2:
            display_list()
        case 3:
            delete()
        case 4: 
            break


    
            
    
            
    
   

