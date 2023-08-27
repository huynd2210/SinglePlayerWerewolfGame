import PlayerActionList
from PlayerAction import PlayerAction


class Player:
    def __init__(self, name: str):
        self.name = name
        self.actions = []
        self.initAction()
    def initAction(self):
        self.actions.append(PlayerAction("visit", True, PlayerActionList.visitAction))
        self.actions.append(PlayerAction("execute", False, PlayerActionList.visitAction))

    def takeNightActionDialogue(self, gameInfo):
        print("What do you want to do tonight? Possible actions are: ")
        possibleNightActions = [actions for actions in self.actions if actions.isNightAction]
        possibleNightActionsNames = [actions.name for actions in possibleNightActions]
        for action in possibleNightActions:
            print("-- " + action.name)
        actionToTake = input()
        while actionToTake not in possibleNightActionsNames:
            print("Invalid input, try again")
            print("What do you want to do tonight?")
            for action in possibleNightActions:
                print(action.name)
            actionToTake = input()


        npcNames = [npc.name for npc in gameInfo.npcList]
        for action in possibleNightActions:
            if action.name == actionToTake:
                print("Who do you want to " + action.name + "?")
                for npc in gameInfo.npcList:
                    print(npc.name)
                targetNPCName = input()
                while targetNPCName not in npcNames:
                    print("Invalid input, try again")
                    print("Who do you want to " + action.name + "?")
                    for npc in gameInfo.npcList:
                        print(npc.name)
                    targetNPCName = input()
                action.performAction(gameInfo, targetNPCName)