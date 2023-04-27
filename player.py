import random

class Player:
    def __init__(self, name, race, player_class, starting_gold, starting_health, daily_gold):
        self.name = name
        self.race = race
        self.player_class = player_class
        self.max_health = starting_health
        self.max_mana = 50
        self.health = self.max_health
        self.mana = self.max_mana
        self.gold = starting_gold
        self.daily_gold = daily_gold
        self.experience = 0
        self.skills = {
            'attack': 1,
            'defense': 1,
            'magic': 1
        }
    def level_up(self):
        self.skills['attack'] += 1
        self.skills['defense'] += 1
        self.skills['magic'] += 1
        self.max_health += 10
        self.health = self.max_health
        self.max_mana += 10
        self.mana = self.max_mana
