#!/usr/bin/python3
import random

name = input("Name your adventurer: ")

enemy_titles = {
    "title": ["shy", "wild", "insane", "blood hungry"]
}

enemies = ['goblin', 'orc', 'kobold', 'beastman']


class Player:
    def __init__(self, name: str, hp=10, sp=2, bc=0):
        self.name = name
        self.hp = hp
        self.sp = sp
        self.bc = bc

    def attack(self, enemy):
        damage_dealt = random.randint(1, 4)
        print(f"\nYou dealt {damage_dealt} damage\n")
        enemy.receive_damage(damage_dealt)

    def receive_damage(self, damage_dealt):
        self.hp -= damage_dealt

    def death_check(self):
        if self.hp <= 0:
            print("The Brave Adventurer has met with a fatal demise.")
            exit()

    def defend(self):
        if self.bc >= 3:
            print(f"{self.name} can not defend until after a long rest!")
        else:
            self.bc += 1
            healed = random.randint(1, 4)
            self.hp += healed
            print(f"\n{self.name} healed for {healed} HP! Total HP: {self.hp}")


class Enemy:
    def __init__(self, name: str, title: str, hp=5, sp=2, bc=0):
        self.name = name
        self.title = title
        self.hp = hp
        self.sp = sp
        self.bc = bc
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
        print(f"\nThe {self.title} {self.name} attacked you for {damage_dealt}!\n")
        player.receive_damage(damage_dealt)

    def receive_damage(self, damage_dealt):
        self.hp -= damage_dealt

    def death_check(self):
        return self.hp <= 0

    def defend_or_attack(self, player):
        d3 = random.randint(1, 3)
        d20 = random.randint(1, 20)
        if d3 == 3 and self.bc < 3:
            if d20 <= 10:
                self.bc += 1
                print(f"The {self.name} tried to defend but failed!")
            else:
                healed = random.randint(1, 4)
                self.hp += healed
                print(f"The {self.title} {self.name} defended and healed for {healed} HP! Total HP: {self.hp}")
        else:
            self.attack(player)


def create_enemy():
    return Enemy(
        random.choice(enemies),
        random.choice(enemy_titles["title"])
    )


def post_battle(player, victories):
    print(f"Number of battles won: {victories}")
    print("After a Long Battle, the Brave Adventurer settles down...\n")

    while True:
        selection = input("\nMake a choice (1)-Rest (2)-Battle (3)-Scavenge (4)-View Stats: ")
        if selection == "1":
            print("You feel well rested...\nEntering Battle Mode\n")
            player.bc = 0
            player.hp += 5
            print(f"{player.name} gained 5 HP")
            enemy = create_enemy()
            print(f"\nYou have encountered a {enemy.title} {enemy.name} (HP: {enemy.hp}, SP: {enemy.sp})")
            return enemy
        elif selection == "2":
            enemy = create_enemy()
            print(f"\nYou have encountered a {enemy.title} {enemy.name} (HP: {enemy.hp}, SP: {enemy.sp})")
            return enemy
        elif selection == "3":
            print("Nothing is here yet...")
        elif selection == "4":
            print(f"\nHP: {player.hp}\nSP: {player.sp}\nBC: {player.bc}")
        else:
            print("Incorrect input")


def turn_order(player, enemy):
    d3 = random.randint(1, 3)
    d20 = random.randint(1, 20)

    if player.sp > enemy.sp:
        player.attack(enemy)
        if enemy.death_check():
            print(f"You have slain the {enemy.title} {enemy.name}!")
            return True
        enemy.defend_or_attack(player)
        player.death_check()
    elif enemy.sp > player.sp:
        enemy.defend_or_attack(player)
        player.death_check()
        player.attack(enemy)
        if enemy.death_check():
            print(f"You have slain the {enemy.title} {enemy.name}!")
            return True
    else:
        # Speed tie
        player_roll = random.randint(1, 20)
        enemy_roll = random.randint(1, 20)
        if player_roll >= enemy_roll:
            player.attack(enemy)
            if enemy.death_check():
                print(f"You have slain the {enemy.title} {enemy.name}!")
                return True
            enemy.defend_or_attack(player)
            player.death_check()
        else:
            enemy.defend_or_attack(player)
            player.death_check()
            player.attack(enemy)
            if enemy.death_check():
                print(f"You have slain the {enemy.title} {enemy.name}!")
                return True
    return False


# Game Initialization
player = Player(name)
enemy = create_enemy()
victories = 0

print(f"\nBrave Adventurer {player.name} has set forth on an adventure\n")
print(f"The Brave Adventurer encountered a {enemy.title} {enemy.name} (HP: {enemy.hp})")

# Main Game Loop
while True:
    selection = input(f"\nMake a choice (1)-Attack (2)-Defend (3)-View Stats: ")
    if selection == "1":
        victory = turn_order(player, enemy)
        if victory:
            victories += 1
            enemy = post_battle(player, victories)
    elif selection == "2":
        player.defend()
        enemy.defend_or_attack(player)
        player.death_check()
    elif selection == "3":
        print(f"\nPlayer HP: {player.hp}")
        print(f"Player SP: {player.sp}")
        print(f"Player BC: {player.bc}\n")
        print(f"Enemy HP: {enemy.hp}")
        print(f"Enemy SP: {enemy.sp}")
        print(f"Enemy BC: {enemy.bc}\n")
    else:
        print("Incorrect input")
