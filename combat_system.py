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

    def modifiers():
        if enemy.title == 'wild':
            print('ok')
    # The goblin attacks the player and reduces the players health
    def attack(self):
        damage_dealt = random.randint(1,4)
        enemy.dmg = damage_dealt
        print(f"\nThe {enemy.name} attacked you for {enemy.dmg}\n")
        player.hp -= enemy.dmg 
        return player.hp

# if the players sp is > than the enemy then the player would attack first
# else the enemy would attack first then the player would attack next

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
        selection = input("\nMake a choice (1)-Rest (2)-Battle (3)-Scavenge: ")
        match selection:
            case "1":
                print("You feel well rested...\n",f"\nEntering Battle Mode\n")
                player.hp = 10
                enemy = Enemy(enemies[randint(0,3)], enemy_titles["title"][randint(0,3)])
                diffculty_modifiers()
                print(f"You have encountered a {enemy.title} {enemy.name}")
                choice_made = True
            case "2":
                print("Nothing is here yet....")
            case "3":
                print("Nothing is here yet...")
            case other:
                print("Incorrect input")

def turn_order():
    if player.sp > enemy.sp:
        player.attack()
        check_win_loss()
        if victory == True: 
            pass
        enemy.attack()
        print(f"Enemy HP Left: {enemy.hp}")
        print(f"Your HP Left: {player.hp}\n")
    else:
        enemy.attack()
        check_win_loss()
        player.attack()
        print(f"Your HP Left: {player.hp}")
        print(f"Enemy HP Left: {enemy.hp}")
def check_win_loss():
    if player.hp <= 0:
        print(f"The Brave Adventurer {player.name} has met with a fatal demise")
        game_over = True
        return game_over
    elif enemy.hp <= 0:
        print(f"\nBrave Adventurer {player.name} defeated the {enemy.name}!")
        enemy.hp = 5 
        victory = True
        return victory
# Defines the player and goblin

player = Player(name)
enemy = Enemy(enemies[randint(0,3)], enemy_titles["title"][randint(0,3)])
diffculty_modifiers()

# Main Game loop

game_over = False
victories = 0

# Begin combat sequence
print(f"\nBrave Adventurer {player.name} has set forth on an adventure\n",
    "As the Brave Adventurer set out for their journey\n")
print(f"the Brave Adventurer encountered a {enemy.title} {enemy.name}")
print(f"Your HP Left: {player.hp}")
print(f"Enemy HP Left: {enemy.hp}")
# Infinite while loop bug idk why lol
while not game_over:
    # Determine enemy title and modifies the default corresponding
    # to the enemy title 
    selection = input(f"\nMake a choice (1)-Attack (2)-Defend (3)-View Stats: ")
    match selection:
        case "1":
            # This might not work if 
            turn_order()
            post_battle()
        case "2":
            health_gained = randint(1,3)
            print(f"\nYou gained {health_gained} HP!")
            player.hp += health_gained
            enemy.attack()
            print(f"\nYour Health: {player.hp}")
        case "3":
            print(f"\nHP: {player.hp}")
            print(f"SP: {player.sp}")
        case other:
            print("Incorrect input")
    # if player's health get less than 0 then game over next turn



