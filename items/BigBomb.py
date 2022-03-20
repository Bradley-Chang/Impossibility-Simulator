from items.item import Item

class BigBomb(Item):
    def __init__(self):
        Item.__init__(self, "Big Bomb", 3, "all")

    def use(self, team, index, extra=None):
        # If the item can attack everyone and it targets the enemy then this adjusts the index.
        if index < len(team[0].field):
            target = team[0].field[index]
        # Otherwise the item target list turns into the ally list and nothing else is changed.
        else:
            index -= len(team[0].field)
            target = team.field[index]
        damage = target.takeDamage(9, False)
        msg = target.name + " took " + damage + " damage from the Big Bomb!"
        return msg
