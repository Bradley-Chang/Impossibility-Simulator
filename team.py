
class Team(object):

    # id: owner of the team
    # name: username of team owner
    # reserve: List of creatures not on the field
    # field: List of creatures on the field
    # items: List of items the player has
    # enemyTeam: Reference to the other team
    # starPoints: points of item usage a team has
    # deathPoints: points gotten by killing creatures.
    # laneL: Left lane of the team
    # laneM: Middle lane of the team
    # laneR: Right lane of the team
    def __init__(self, id, field, reserve, items, name):
        self.makeField(field)
        self.makeReserve(reserve)
        self.items = items
        self.starPoints = 7
        self.deathPoints = 0
        self.id = id
        self.name = name
        self.enemyTeam = None
        self.lanes = [[], [], []]

    # switches swapOut in the field with swapIn in the reserve
    def switch(self, swapOut, swapIn):
        self.field[self.field.index(swapOut)] = swapIn
        self.reserve[self.reserve.index(swapIn)] = swapOut

    # used to initialize the reserve for a team, passes in the team and enemyTeam values into the creatures.
    def makeField(self, creatures):
        self.lanes[0].append(creatures[0])
        self.lanes[1].append(creatures[1])
        self.lanes[2].append(creatures[2])
        for i in creatures:
            i.team = self
        for i in creatures:
            i.enemyTeam = self.enemyTeam

    # used to initialize the reserve for a team, passes in the team and enemyTeam values into the creatures.
    def makeReserve(self, creatures):
        self.reserve = creatures
        for i in creatures:
            i.team = self
        for i in creatures:
            i.enemyTeam = self.enemyTeam
