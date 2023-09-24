import logging
from src.GameEngine import GameConfig


def logDebug(message):
    if GameConfig.isDebug:
        # logging.debug(message)
        print(message)