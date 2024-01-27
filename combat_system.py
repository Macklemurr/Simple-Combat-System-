from random import randint

# Dice
d20 = randint(0,20)
d6 = randint(0,6)
d3 = randint(0,3)

player_name = input("Name your adventurer: ")

class Player:
    def __init__(self, name: str, hp=10, dmg=d3, sp=1):
        """
        hp - health point
        dmg - damage
        default dmg is a d3 dice
        sp - speed points
        """
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.sp = sp
    # The player attacks the goblin and reduces the goblin health 
    def attack(self):
        enemy.hp -= self.dmg
        return enemy.hp

        
class Enemy:
    def __init__(self, name="Wild Goblin", hp=5, dmg=d3, sp=2):
        #health is hp
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.sp = sp
    # The goblin attacks the player and reduces the players health
    def attack(self):
        player.hp -= self.dmg 
        return player.hp

# if the players sp is > than the enemy then the player would attack first
# else the enemy would attack first then the player would attack next
    
def turn_order():
    if player.sp > enemy.sp:
        print("You go first !")
        player.attack()
        print(f"Enemy HP Left: {enemy.hp}")
        enemy.attack()
        print(f"Your HP Left: {player.hp}")

    else:
        print("You go second :(")
        enemy.attack()
        print(f"Your HP Left: {player.hp}")
        player.attack()
        print(f"Enemy HP Left: {enemy.hp}")

# Defines the player and goblin

player = Player(player_name)
enemy = Enemy()

# Main Game loop

game_over = False

# Begin combat sequence

print(f"You've encountered a {enemy.name}")

while not game_over:
    # Introduces the enemy
    turn_order()
    # if player's health get less than 0 then game over next turn
    if player.hp <= 0:
        print("Game Over")
        game_over = True
    elif enemy.hp <= 0:
        print("You have defeated the enemy!")
        game_over = True

