from Role import Role


class NPC:
    def __init__(self, role: Role, name: str):
        self.role = role
        self.name = name
        #Journal is a list that contains information that this npc has learned. For example, the seer can learn other villagers roles and note them here.
        self.journal = []
        self.statuses = []
        self.isAlive = True
        self.isBeingKilled = False
        self.isAtHome = True

    def __repr__(self):
        return self.name + ": " + str(self.role)