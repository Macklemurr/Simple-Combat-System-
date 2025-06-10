import random

name = input("Name your adventurer: ")

enemy_titles = {
    "title": ["shy", "wild", "insane", "blood hungry"]
}

enemies = ['goblin', 'orc', 'kobold', 'beastman']


class Player:
    def __init__(self, name: str, hp=10, sp=2):
        self.name = name
        self.hp = hp
        self.sp = sp

    def attack(self, enemy):
        damage_dealt = random.randint(1, 4)
        print(f"\nYou dealt {damage_dealt} damage\n")
        enemy.receive_damage(damage_dealt)

    def receive_damage(self, damage_dealt):
        self.hp -= damage_dealt

    def death_check(self):
        if self.hp <= 0:
            print("The Brave Adventurer has met with a fatal demise")
            exit()


class Enemy:
    def __init__(self, name: str, title: str, hp=5, sp=2):
        self.name = name
        self.title = title
        self.hp = hp
        self.sp = sp
        self.apply_difficulty()

    def apply_difficulty(self):
        if self.title == 'wild':
            self.hp += 2
        elif self.title == 'insane':
            self.sp += 2
        elif self.title == 'blood hungry':
            self.hp += 5
            self.sp += 4

    def attack(self, player):
        damage_dealt = random.randint(1, 4)
        print(f"\nThe {self.title} {self.name} attacked you for {damage_dealt}\n")
        player.receive_damage(damage_dealt)

    def receive_damage(self, damage_dealt):
        self.hp -= damage_dealt


def create_enemy():
    return Enemy(
        enemies[random.randint(0, 3)],
        enemy_titles["title"][random.randint(0, 3)]
    )


def post_battle(player, victories):
    print(f"Number of battles won: {victories}")
    print("After a Long Battle, the Brave Adventurer settles down...\n")

    while True:
        selection = input("\nMake a choice (1)-Rest (2)-Battle (3)-Scavenge (4)-View Stats: ")
        if selection == "1":
            print("You feel well rested...\nEntering Battle Mode\n")
            player.hp += 5
            print(f"{player.name} gained 5 HP")
            enemy = create_enemy()
            print(f"\nEnemy HP: {enemy.hp}, Enemy SP: {enemy.sp}")
            print(f"You have encountered a {enemy.title} {enemy.name}")
            return enemy
        elif selection == "2":
            enemy = create_enemy()
            print(f"\nEnemy HP: {enemy.hp}, Enemy SP: {enemy.sp}")
            print(f"You have encountered a {enemy.title} {enemy.name}")
            return enemy
        elif selection == "3":
            print("Nothing is here yet...")
        elif selection ==  "4":
            print(f"\nHP: {player.hp}\nSP: {player.sp}")
        else:
            print("Incorrect input")


def turn_order(player, enemy):
    # Determine who goes first
    if player.sp > enemy.sp:
        player.attack(enemy)
        if enemy.hp <= 0:
            return True
        enemy.attack(player)
    elif enemy.sp > player.sp:
        enemy.attack(player)
        if player.hp <= 0:
            player.death_check()
        player.attack(enemy)
    else:
        # Speed tie = roll d20
        if random.randint(1, 20) >= random.randint(1, 20):
            player.attack(enemy)
            if enemy.hp <= 0:
                return True
            enemy.attack(player)
        else:
            enemy.attack(player)
            if player.hp <= 0:
                player.death_check()
            player.attack(enemy)

    player.death_check()
    return enemy.hp <= 0


# Game Initialization
player = Player(name)
enemy = create_enemy()
victories = 0

print(f"\nBrave Adventurer {player.name} has set forth on an adventure\n")
print(f"The Brave Adventurer encountered a {enemy.title} {enemy.name}")
print(f"Your HP Left: {player.hp}")
print(f"Enemy HP Left: {enemy.hp}")

# Main Game Loop
while True:
    selection = input(f"\nMake a choice (1)-Attack (2)-Defend (3)-View Stats: ")
    if selection == "1":
        victory = turn_order(player, enemy)
        if victory:
            victories += 1
            enemy = post_battle(player, victories)
    elif selection == "2":
        health_gained = random.randint(1, 6)
        print(f"\nYou gained {health_gained} HP!")
        player.hp += health_gained
        enemy.attack(player)
        player.death_check()
        print(f"\nYour Health: {player.hp}")
    elif selection == "3":
        print(f"\nHP: {player.hp}")
        print(f"SP: {player.sp}")
    else:
        print("Incorrect input")
