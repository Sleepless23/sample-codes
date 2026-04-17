# Simple CHaracter and Enemy Creation
import random

#Player
player_name = "henry"
player_hp = 100
player_mp = 50
player_atk = 10
player_speed = 5

#Enemy
monster = "goblin"
monster_hp = 150
monster_atk = 5
monster_speed = 5

# monster_hp - player_atk

def player_attack():
    
    global monster_hp 
    monster_hp -= player_atk

    print(f"The opponent suffered {player_atk} damage")
    print(f"THe opponent's hp is now {monster_hp}")
    
def monster_attack():
    
    pass

#speed > opponent, high speed = high success,  random number = ?
# if monster_speed == 5, player_speed == 10, >=
# monster_speed - player_speed
# chance of escape is based on the gap of the speed between the player and the monster

def player_escape():
    
    #Luck Chance to Escape 20%
    base_chance = 0.2
    
    bonus_per_gap = (player_speed - monster_speed) * 0.05
    
    escape_chance = base_chance + bonus_per_gap
    
    if escape_chance < 0.1:
        escape_chance = 0.1
    
    if escape_chance > 0.9:
        
        escape_chance = 0.9
    
    chance_number = random.random()
    
    if chance_number < escape_chance:
        print("Successfully Escaped")
    
    else:
        print()


#Social Media

username = "Gayl" #variable
post = "Bundok"
likes = 12

print(likes)

def like_button():
    
    global likes 
    likes += 1
    
    print("You liked this post!")
    
    
like_button()
print(f"Your likes is now {likes}")