from items.item import Item

class BeaconOfRage(Item):
    def __init__(self):
        Item.__init__(self, "Beacon Of Rage", 3, "ally")
    def use(self, team, index, extra=None):
        team.field[index].takeStatus("rageBeacon", 999)
        for i in team.field:
            i.takeStatus("rage", 1)
        return "Everyone on " + team.field[index].name + "'s team is enraged! (+2 ATK, +25% SPD)"