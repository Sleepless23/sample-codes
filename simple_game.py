# Simple CHaracter and Enemy Creation
import random

#player
player_hp = f"\033[0;32m100\033[0m"
atk = 15
weapons = ["sword", "axe"]
weapon = "sword"
#monster
monster_hp = 30
monster_atk = random.randint(5, 10)
monster_drop = "dagger"

def player_atk(enemy_hp, atk):
    
    print(f"\033[0;31mYou dealt {atk} damage to the enemy!\033[0m")
    return enemy_hp - atk

def enemy_atk(player_hp, atk):
    
    print(f"The monster dealt {atk} damage to you!")
    
    return player_hp - atk

def change_weapon():
    
    for num, weapon in enumerate(weapons, 1):
        
        print(f"{num}. {weapon}")
    
    weapons_choice = int(input("Choose weapon: ")) - 1
    
    return weapons_choice

def display_stats():
    
    print(f"\033[1mHP: {player_hp}")
    print("Available Weapons")
    for weapon in weapons:
        
        print(weapon, "\033[0m")
        
menu = ["Attack", "Change Weapon", "Run", "Exit"]

while True:
    
    display_stats()
    print("Welcome to the Game!")
    print("Defeat the enemy to win")
    print("Choose Action")
    for num, choice in enumerate(menu, 1):
        
        print(f"{num}. {choice}")
    
    action = input("> ")
    
    if action == "1":
        
        monster_hp = player_atk(monster_hp, atk)
        if monster_hp <= 0:
        
            weapons.append(monster_drop)
            print(f"You have defeated the monster and you acquired {monster_drop}")
        
    elif action == "2":
        
        weapon = weapons[change_weapon()]
        
        print(weapon)
        
    else:
        
        print("You ran away!")
    
    
        
    player_hp = enemy_atk(player_hp, monster_atk)
    if player_hp <= 0:
        print("You have defeated")
        break
    
