# Simple CHaracter and Enemy Creation
import random

monsters = [
    
    ("Goblin", 5, 20),
    ("Slime", 3, 10),
    ("Troll", 15, 30)
    
]
print(monsters[1])

player = {
    
    "name" : "Player1",
    "atk" : 10,
    "hp" : 20
    
}

def spawn_monster(monsters):
    monster = random.choice(monsters)
    
    return [monster[0], monster[1], monster[2]]
  

    

def player_atk(enemy_hp, atk):
    
    print(f"\033[0;31mYou dealt {atk} damage to the enemy!\033[0m")
    return enemy_hp - atk

def enemy_atk(player_hp, atk):
    
    print(f"The monster dealt {atk} damage to you!")
    
    return player_hp - atk
    
menu = ["Attack", "Change Weapon", "Run", "Exit"]

# while True:
    
#     # print("Welcome to the Game!")
#     # print("Defeat the enemy to win")
#     # print("Choose Action")
#     # for num, choice in enumerate(menu, 1):
        
#     #     print(f"{num}. {choice}")
    
#     # action = input("> ")
    
    
print("Youa re in Dungeon Room 1")
monster_name, monster_atk, monster_hp = spawn_monster(monsters)
print(type(spawn_monster(monsters)))
print(f"You have encountered {monster_name}")
#player attacked the monster

print(monster_hp)

print(f"You attacked the {monster_name} and inflicted 3 damage")
monster_hp -= 3
print(monster_hp)
