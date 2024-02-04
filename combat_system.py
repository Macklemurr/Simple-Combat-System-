import random
from random import randint

name = str(input("Name your adventurer: "))

enemy_titles = {
    "title": [ "shy", "wild", "insane", "blood hungry"],
}

enemies = [ 'goblin','orc','kobold','beastman' ]

class Player:
    def __init__(self, name: str, hp=10, sp=2):
        """
        hp - health point
        dmg - damage
        default dmg is a d3 dice
        sp - speed points
        """
        self.name = name
        self.hp = hp
        self.sp = sp
    
    # The player attacks the goblin and reduces the goblin health 
    def attack(self):
        damage_dealt = random.randint(1,4)
        print(f"\nYou dealt {damage_dealt} damage\n")
        enemy.receive_damage(damage_dealt)
    
    def death_check(self):
        if self.hp <= 0:
            print("The Brave Adventurer has met with a fatal demise")
            exit()
    
    def receive_damage(self, damage_dealt):
        self.hp -= damage_dealt

class Enemy:
    def __init__(self, name: str, title: str, hp=5, sp=2):
        #health is hp
        self.name = name
        self.title = title
        self.hp = hp
        self.sp = sp

    # The goblin attacks the player and reduces the players health
    def attack(self):
        damage_dealt = random.randint(1,4)
        print(f"\nThe {enemy.name} attacked you for {damage_dealt}\n")
        player.receive_damage(damage_dealt) 
    
    def receive_damage(self, damage_dealt):
        self.hp -= damage_dealt
        
    def reset_stats(self):
        self.hp = 5 
        self.sp = 2 

def difficulty_modifiers():
    if enemy.title == 'wild':
        enemy.hp += 2
    elif enemy.title == 'insane':
        enemy.sp += 2
        print(enemy.sp)
    elif enemy.title == 'blood hungry':
        enemy.hp += 5
        enemy.sp += 4
        print(enemy.sp)

def player_death_check():
    if player.hp <= 0:
        print("The Brave Adventurer has met with a fatal demise")
        exit()

def enemy_death_check():
    if enemy.hp <= 0:
        victory = True
        return victory
        
# Modifies the enemy class stats based on the title of the enemy
def post_battle():
    choice_made = False
    
    # Reinitializes the enemy
    enemy = Enemy(enemies[randint(0,3)], enemy_titles["title"][randint(0,3)], hp=5, sp=1)
    enemy.reset_stats()
    difficulty_modifiers()

    print(f"Number of battles won: {victories}")
    print(f"After a Long Battle, the Brave Adventurer settles down...\n")
    while choice_made == False:
        selection = input("\nMake a choice (1)-Rest (2)-Battle (3)-Scavenge (4)-View Stats: ")
        match selection:
            case "1":
                print("You feel well rested...\n",f"\nEntering Battle Mode\n")
                player.hp += 5
                print(f"{player.name} gained 5 HP")
                print(f"\nEnemy HP: {enemy.hp}", f"Enemy SP: {enemy.sp}")
                print(f"You have encountered a {enemy.title} {enemy.name}")
                choice_made = True
            case "2":
                print(f"\nEnemy HP: {enemy.hp}", f"\nEnemy SP: {enemy.sp}")
                print(f"You have encountered a {enemy.title} {enemy.name}")
                choice_made = True
            case "3":
                print("Nothing is here yet...")
            case "4":
                print(f"\nHP: {player.hp}")
                print(f"SP: {player.sp}")
            case other:
                print("Incorrect input")


def turn_order():
    victory = False 
    """   
    if the players sp is > than the enemy then the player would attack first
    else the enemy would attack first then the player would attack next

    if the enemy health is not less than or equal to 0 it will break out of the loop 

    I'm using pokemon rules when it comes to the speed, if the speed equals then a d20 will roll and determine who attacks first, at complete random.
    the higher the speed determines who go first
    """
    while victory == False:
        if player.sp > enemy.sp:
            player.attack()
            enemy_death_check()
            enemy.attack()
            player_death_check()
            if not enemy.hp <= 0:
                print(f"Your HP Left: {player.hp}")
                print(f"Enemy HP Left: {enemy.hp}")
                break
            break
        elif enemy.sp > player.sp:
            enemy.attack()
            player_death_check()
            player.attack()
            enemy_death_check()
            if not enemy.hp <= 0:
                print(f"Your HP Left: {player.hp}")
                print(f"Enemy HP Left: {enemy.hp}")
                break
            break
        elif player.sp == enemy.sp:
            player_d20_roll = random.randint(1,20)
            enemy_d20_roll = random.randint(1,20)
            if player_d20_roll > enemy_d20_roll:
                player.attack()
                enemy_death_check()
                enemy.attack()
                player_death_check()
                if not enemy.hp <= 0:
                    print(f"Your HP Left: {player.hp}")
                    print(f"Enemy HP Left: {enemy.hp}")
                    break
                break
            elif enemy_d20_roll > player_d20_roll:
                enemy.attack()
                player_death_check()
                player.attack()
                enemy_death_check()
                if not enemy.hp <= 0:
                    print(f"Your HP Left: {player.hp}")
                    print(f"Enemy HP Left: {enemy.hp}")
                    break
                break

# Initializes the player and enemy

player = Player(name)
enemy = Enemy(enemies[randint(0,3)], enemy_titles["title"][randint(0,3)])
difficulty_modifiers()

game_over = False
battle_end = False
victory = False
victories = 0

print(f"\nBrave Adventurer {player.name} has set forth on an adventure\n",
    "As the Brave Adventurer set out for their journey")
print(f"the Brave Adventurer encountered a {enemy.title} {enemy.name}")
print(f"Your HP Left: {player.hp}")
print(f"Enemy HP Left: {enemy.hp}")
# Main Game Loop
while not game_over:
    victory = False # I need this here so battles will loop after winning, DO NOT REMOVE
    selection = input(f"\nMake a choice (1)-Attack (2)-Defend (3)-View Stats: ")
    match selection:
        case "1":
            turn_order()
            if victory == True:
                post_battle()
            if enemy.hp <= 0:
                victory = True
                victories += 1
                post_battle()
            elif player.hp <= 0:
                game_over = True
                print(f"\nThe Brave Adventurer has met with a fatal demise")
                break
            elif player.hp <= 0 and enemy.hp <= 0:
                game_over = True
                print(f"\nThe Brave Adventurer has met with a fatal demise")
                break
        case "2":
            health_gained = random.randint(1,6)
            print(f"\nYou gained {health_gained} HP!")
            player.hp += health_gained
            enemy.attack()
            player_death_check()
            print(f"\nYour Health: {player.hp}")
        case "3":
            print(f"\nHP: {player.hp}")
            print(f"SP: {player.sp}")
        case other:
            print("Incorrect input")