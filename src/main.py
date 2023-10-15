from GameEngine.Game import Game
from Player import Player

if __name__ == '__main__':
    setupNPCCounts = {
        "villager": 5,
        "seer": 1,
        "doctor": 1,
        "werewolf": 1,
        "trapper": 1,
        "cleaner": 1,
        "deceiver": 1,
        "serial killer": 1
    }

    player = Player("Player")
    Game(player, config=setupNPCCounts, isDebug=False).startGame()
