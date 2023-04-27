import random
from colorama import Fore, Style

class Dungeon:
    def __init__(self, name, difficulty, cost):
        self.name = name
        self.difficulty = difficulty
        self.cost = cost
        self.reward = 0
        self.rare_drop = None

    def enter(self, player):
        player.gold -= self.cost
        print(f'Entering {self.name}...')
        encounter = random.choice(['chest', 'monster'])
        rare_drop_chance = 0  # declare the variable outside of the if block
        if encounter == 'chest':
            self.reward = random.randint(1, 10) * self.difficulty
            player.gold += self.reward # Update the player's gold
            print(f'Found {self.reward} gold in a chest!')
        elif encounter == 'monster':
            monster_health = random.randint(50, 100) * self.difficulty
            print(f'Encountered a monster with {Fore.RED}{monster_health}{Style.RESET_ALL} health!')
            while monster_health > 0 and player.health > 0:
                # Player's turn
                action = input('What do you want to do? (1-Attack / 2-Magic)')
                if action == '1':
                    damage = random.randint(1, 10) * player.skills['attack']
                    monster_health -= damage
                    print(f'You dealt {damage} damage to the monster!')
                    if (monster_health <=0):
                        monster_health = 0
                    print(f"Monster's current health: {Fore.RED}{monster_health}{Style.RESET_ALL}")
                elif action == '2':
                    if player.mana >= 10:
                        damage = random.randint(10, 20) * player.skills['magic']
                        monster_health -= damage
                        player.mana -= 10
                        print(f'You cast a spell and dealt {damage} damage to the monster!')
                    if (monster_health <=0):
                        monster_health = 0
                        print(f"Monster's current health: {Fore.RED}{monster_health}{Style.RESET_ALL}")
                    else:
                        print('Not enough mana!')
                else:
                    print('Invalid action!')
                # Monster's turn
                if monster_health > 0:
                    player_health = player.health
                    monster_damage = random.randint(1, 10) * self.difficulty
                    player_health -= monster_damage
                    player.health = player_health
                    print(f'The monster attacked you and dealt {monster_damage} damage!')
                    print(f"Your current health: {Fore.GREEN}{player_health}{Style.RESET_ALL}")
                # Check if player is dead
                if player.health <= 0:
                    print('You died!')
                    exit()
                # Player defeated the monster
                self.reward = random.randint(10, 20) * self.difficulty
                player.gold += self.reward # Update the player's gold
                print(f'You defeated the monster and found {self.reward} gold!')
                player.experience += 10 * self.difficulty
                rare_drop_chance = random.randint(1, 10)
                if rare_drop_chance == 1:
                    self.rare_drop = 'rare item'
                    print('You found a rare item!')
            else:
                print('Invalid encounter!')
