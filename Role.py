class Role:
    def __init__(self, roleName : str, faction : str):
        self.roleName = roleName
        self.faction = faction

    def __repr__(self):
        return self.roleName + " " + self.faction

    def __str__(self):
        return self.roleName + " " + self.faction