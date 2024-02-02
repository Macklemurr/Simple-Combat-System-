import random
from random import randint

name = str(input("Name your adventurer: "))

enemy_titles = {
    "title": [ "shy", "wild", "insane", "blood hungry"],
}

enemies = [ 'goblin','orc','kobold','beastman' ]

class Player:
    def __init__(self, name: str, hp=10, sp=1):
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
        self.dmg = damage_dealt
        print(f"You dealt {self.dmg} damage\n")
        enemy.hp -= self.dmg
        return enemy.hp

class Enemy:
    def __init__(self, name: str, title: str, hp=5,sp=2):
        #health is hp
        self.name = name
        self.title = title
        self.hp = hp
        self.sp = sp

    # The goblin attacks the player and reduces the players health
    def attack(self):
        damage_dealt = random.randint(1,4)
        enemy.dmg = damage_dealt
        print(f"\nThe {enemy.name} attacked you for {enemy.dmg}\n")
        player.hp -= enemy.dmg 
        return player.hp
    def reset():
        enemy.hp = 5
        enemy.sp = 2

def player_death_check():
    if player.hp <= 0:
        print("The Brave Adventurer has met with a fatal demise")
        exit()

# Modifies the enemy class stats based on the title of the enemy
def diffculty_modifiers():
    if enemy.title == 'wild':
        enemy.hp += 2
    elif enemy.title == 'insane':
        enemy.sp += 2
        print(enemy.sp)
    elif enemy.title == 'blood hungry':
        enemy.hp += 5
        enemy.sp += 4
        print(enemy.sp)
    
def post_battle():
    choice_made = False
    print(f"Number of battles won: {victories}")
    print(f"After a Long Battle, the Brave Adventurer settles down...\n")
    while choice_made == False:
        selection = input("\nMake a choice (1)-Rest (2)-Battle (3)-Scavenge (4)-View Stats: ")
        match selection:
            case "1":
                print("You feel well rested...\n",f"\nEntering Battle Mode\n")
                player.hp += 5
                print(f"{player.name} gained 5 HP")
                enemy = Enemy(enemies[randint(0,3)], enemy_titles["title"][randint(0,3)], hp=5)
                Enemy.reset()
                diffculty_modifiers()
                if enemy.title == 'wild':
                    enemy.hp += 2
                elif enemy.title == 'insane':
                    enemy.sp += 2
                    print(enemy.sp)
                elif enemy.title == 'blood hungry':
                    enemy.hp += 5
                    enemy.sp += 4
                    print(enemy.sp) 
                print(f"You have encountered a {enemy.title} {enemy.name}")
                choice_made = True
            case "2":
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

    if the enemy health is not less than or equal to 0 it will break out of the loop and 


    WORK ON TURN ORDER DEPENDING ON THE SPEED STAT IT KEEPS LOOPING MAKE IT GO BACK TO THE MAIN GAME LOOP AFTER 
    """
    while victory == False: 
        if player.sp > enemy.sp:
            player.attack()
            if enemy.hp <= 0:
                victory = True
            enemy.attack()
            print(f"Enemy HP Left: {enemy.hp}")
            print(f"Your HP Left: {player.hp}\n")
            if not enemy.hp <= 0:
                print(f"Your HP Left: {player.hp}")
                print(f"Enemy HP Left: {enemy.hp}")
                break
            break
        else:
            enemy.attack()
            if player.hp <= 0: 
                print("The Brave Adventurer has met with a fatal demise")
                exit()
            player.attack()
            if not enemy.hp <= 0:
                print(f"Your HP Left: {player.hp}")
                print(f"Enemy HP Left: {enemy.hp}")
                break
            print(f"Your HP Left: {player.hp}")
            print(f"Enemy HP Left: {enemy.hp}")
            break

# Defines the player and goblin

player = Player(name)
enemy = Enemy(enemies[randint(0,3)], enemy_titles["title"][randint(0,3)])
diffculty_modifiers()

game_over = False
battle_end = False
victory = False
victories = 0

# Begin combat sequence
print(f"\nBrave Adventurer {player.name} has set forth on an adventure\n",
    "As the Brave Adventurer set out for their journey")
print(f"the Brave Adventurer encountered a {enemy.title} {enemy.name}")
print(f"Your HP Left: {player.hp}")
print(f"Enemy HP Left: {enemy.hp}")
# Main Game Loop
while not game_over:
    # Determine enemy title and modifies the default corresponding
    # to the enemy title 
    selection = input(f"\nMake a choice (1)-Attack (2)-Defend (3)-View Stats: ")
    match selection:
        case "1":
            # This might not work if 
            turn_order()
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
            health_gained = randint(1,3)
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