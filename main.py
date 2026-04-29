#Comment
#Variables - building blocks

#Operators
#Arithmetic Operators
# + - addition
# - - subtraction
# * - multiplication
# / - division
# // floor division 
# ** - exponentation
# % - modulo/modulus

#Comparison/Relational Operators

# > - greater than
# < - less than
# >= - greater than or equal to
# <= - less than or equal to
# == - is equal to
# != - is not equal to

#Conditionals 


#Logical and or not
# and - if both the left-hand an d right-hand side conditions are true it will result as true 
# or - if one side is True, the result True

character_name = "joy"
level = 1
inventory = "bandage"
death_count = 0
hp = 500
mp = 100

# print("Welcome Random Dungeon Crawler")

# choice = input("What would you like to do?")

# if choice == "view":
#     print(character_name,"\n",level,"\n",death_count,"\n",hp,"\n",mp)
#     print(choice)

#Loops 
#while - infinite 
#for - for iterating

#List

stats = [character_name, level, hp, mp]

# for i in stats:
#     print(i)

#Assignment Operator
# =, +=, -=, *=, /=


# while True: 
    
#     choice = input("What do you what to do? 1. View Stats 2. Start Game 3. Exit ")
#     #match-case
#     match choice:
        
#         case "1":
            
#             print(" You have selected 1")
        
#         case "2":
            
#             print("Game Started")
            
#         case "3":
            
#             print("Goodbye!")
#             break

#global scope


#Functions piece of code that needs to be created and called whenever you needed

#String formatting

def display_UI():
    
    print("Welcome to Dungfeon Crawler Game")
    print("1. Play")
    print("2. Exit")






while True:
    
    display_UI()
    choice = input("Select your action: ")
    
    while True:
        if choice == "1":
            
            print("You are now playing the game")
            continue
        else:
            
            print("You've quit the game")
            break
    
    break
