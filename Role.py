class Role:
    def __init__(self, roleName : str, faction : str, alignment: str):
        self.roleName = roleName
        self.faction = faction
        self.alignment = alignment

    def __repr__(self):
        return self.roleName + " " + self.faction + " " + self.alignment

    def __str__(self):
        return self.roleName + " " + self.faction + " " + self.alignment