from GameEngine.Game import Game
from Player import Player

if __name__ == '__main__':
    player = Player("Player")
    Game(player).startGame()
