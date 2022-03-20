from items.item import Item
class FrozenInTime(Item):
    def __init__(self):
        Item.__init__(self, "Frozen In Time", 3, "enemy")

    def use(self, team, index, extra=None):
        team.field[index].takeStatus("timeFreeze", 1)
        msg = team.field[index].name + " was frozen in time."
        return msg