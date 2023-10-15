from src.Npc.Role import Role


class NPC:
    def __init__(self, role: Role, name: str, actionFunction):
        self.role = role
        self.name = name
        #Journal is a list that contains information that this npc has learned. For example, the seer can learn other villagers roles and note them here.
        self.journal = []
        self.statuses = []
        self.isAlive = True
        self.actionFunction = actionFunction

        #Flag to indicate that this npc is being killed. If this npc is not saved by the end of the night, then he will die.
        self.isBeingKilled = False
        self.isAtHome = True
        self.isAllowedToAct = True
        self.isBeingTrapped = False
        self.isBeingCoveredByDeceiver = False
        self.isCleaned = False
        self.isBeingSuppressed = False
        self.isBeingGuarded = False
        self.guarding = []

    def __repr__(self):
        return self.name + ": " + str(self.role)

    def performAction(self, *args):
        self.actionFunction(*args)

