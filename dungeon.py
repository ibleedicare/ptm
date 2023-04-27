import random

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
        if encounter == 'chest':
            self.reward = random.randint(1, 10) * self.difficulty
            player.gold += self.reward # Update the player's gold
            print(f'Found {self.reward} gold in a chest!')
        elif encounter == 'monster':
            monster_health = random.randint(50, 100) * self.difficulty
            print(f'Encountered a monster with {monster_health} health!')
            while monster_health > 0 and player.health > 0:
                action = input('What do you want to do? (attack/magic)')
                if action == 'attack':
                    damage = random.randint(1, 10) * player.skills['attack']
                    monster_health -= damage
                    print(f'You dealt {damage} damage to the monster!')
                elif action == 'magic':
                    if player.mana >= 10:
                        damage = random.randint(10, 20) * player.skills['magic']
                        monster_health -= damage
                        player.mana -= 10
                        print(f'You cast a spell and dealt {damage} damage to the monster!')
                    else:
                        print('Not enough mana!')
                else:
                    print('Invalid action!')
                if monster_health <= 0:
                    self.reward = random.randint(10, 20) * self.difficulty
                    print(f'You defeated the monster and found {self.reward} gold!')
                    player.experience += 10 * self.difficulty
                    rare_drop_chance = random.randint(1, 10)
                    if rare_drop_chance == 1:
                        self.rare_drop = 'rare item'
                        print('You found a rare item!')
                    break
            if player.health <= 0:
                print('You died!')
                exit()
