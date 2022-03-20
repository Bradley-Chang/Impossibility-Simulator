class Item(object):
    # name: name of item
    # cost: amount of points it costs to play the card
    # target: "enemy", "ally", "all", defines who can get affected by the item.
    # usage: "once" - consumed after use
    #        "infinite" - not consumed after use.
    #        "equipped" - consumed after use, but can be taken off the creature after it dies
    # option: "none" - There is no choice of how the item can be used.
    #         "choose" - Choose how the item can be used (e.g. pick what status effect to inflict on a target)
    def __init__(self, name, cost, target, usage="once", option="none"):
        self.name = name
        self.cost = cost
        self.target = target
        self.usage = usage
        self.option = option

    def use(self, team, index, extra=None):
        pass