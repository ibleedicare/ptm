from player import Player
from dungeon import Dungeon
import random

DAILY_CREDIT = 30
player = Player("John", "Human", "Warrior", 30, DAILY_CREDIT)
# create list of dungeons
dungeons = [Dungeon('Easy Dungeon', 1, 7), Dungeon('Medium Dungeon', 2, 11), Dungeon('Hard Dungeon', 3, 20)]

# game loop
while True:
    # print player stats
    print(f'Gold: {player.gold}, Health: {player.health}, Mana: {player.mana}, Experience: {player.experience}')

    # print available dungeons
    print('Available Dungeons:')
    for i, dungeon in enumerate(dungeons):
        print(f'{i+1}. {dungeon.name} ({dungeon.difficulty} difficulty, {dungeon.cost} gold)')

    # prompt player to choose a dungeon
    dungeon_choice = input('Choose a dungeon to enter (1-3): ')
    if dungeon_choice not in ['1', '2', '3']:
        print('Invalid choice!')
        continue

    # enter chosen dungeon
    dungeon = dungeons[int(dungeon_choice)-1]
    dungeon.enter(player)

    # check if player has enough experience to level up
    if player.experience >= 100:
        player.level_up()

    # check if player has won the game
    if player.gold >= 1000:
        print('Congratulations! You have won the game!')
        break
    player.gold += DAILY_CREDIT
