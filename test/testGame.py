import pytest

from src.GameEngine import GameConfig
from src.GameEngine.Game import Game
from src.GameEngine.GameInfo import GameInfo
from src.Player import Player


def setup():
    setupNPCCounts = {
        "villager": 5,
        "seer": 1,
        "doctor": 1,
        "werewolf": 1,
        "trapper": 1,
        "cleaner": 1,
        "deceiver": 1,
        # "serial killer": 1
    }

    player = Player("Player")
    game = Game(player, config=setupNPCCounts)
    return game

def test_when_fullmoon_should_be_normal():
    # Create a sample game instance
    game = setup()
    GameConfig.fullMoonFrequency = 2
    # Set up the game info for a full moon
    game.gameInfo.currentNightType = "full moon"

    # Current game turn is 2, and it is currently a full moon, so when updating for next turn
    # next turn should be 3 % 2 (full moon frequency) != 0 therefore normal night
    game.gameInfo.currentTurn = 2

    # Call the updateGameInfo function
    game.updateGameInfo()

    # Assert that the current night type is updated to "normal"
    assert game.gameInfo.currentNightType.lower() == "normal"

def test_updateGameInfo_normal():
    # Create a sample game instance
    game = setup()
    GameConfig.fullMoonFrequency = 2

    # Set up the game info for a normal night
    game.gameInfo.currentNightType = "normal"
    game.gameInfo.currentTurn = 1

    # Call the updateGameInfo function
    game.updateGameInfo()

    # Assert that the current night type is updated to "full moon" every 3 turns
    assert game.gameInfo.currentNightType == "full moon"