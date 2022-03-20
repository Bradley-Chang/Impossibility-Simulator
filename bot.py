# Work with Python 3.6
import discord
import asyncio
from discord.ext import commands
from status import statusAddAtk, statusAddDef, statusAddSpd, statusMultAtk, statusMultDef, statusMultSpd, statusDoT, statusNames
import creatures
import items
from team import Team
import math


TOKEN = 'NTQ1MDc1MzgzODc2MzIxMjgy.D0VoeQ.RZX5DnefTV5otsBPmQl5z9IGgvQ'

description = "A bunch of mishmashed stuff."
bot = commands.Bot(command_prefix="c!", description=description)
"""
@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    channel = message.channel
    if message.author == bot.user:
        return
# heckingtons: test command that shows a weak creature named Heck
    if message.content.startswith('c!heckingtons'):
        msg = 'Hello {0.author.mention}'.format(message)
        testCreature = Creature("test", 1, 1, 1, 1, 1, "fire", "heck")
        await channel.send(testCreature.toString())
# target <user>: takes 1 argument for a user, if the user speaks the bot will respond
   # if message.content.startswith('c!target'):
   #     global target
    #    target = None
     #   try:
      #      target = grabUser(message.content)
      #  except ValueError:
        #    channel.send("Found an @ in the message but it wasn't a mention")
         #   return

      #  if target is None:
      #      await channel.send("That person doesn't exist!")
      #  else:
      #      await channel.send("I will now notice " + str(target.mention))
# gettarget: bot will state who the target is
    if message.content.startswith('c!gettarget'):
        await channel.send("The target is " + str(target.mention))

# remember: does nothing
    if message.content.startswith('c!remember'):
        await channel.send("")

# members: lists out all members in all servers the bot is in.
    if message.content.startswith('c!members'):
        users = bot.get_all_members()
        memberString = ""
        for i in users:
            memberString += i.name + "\n"
        await channel.send("I can see these members: " + memberString)
# guilds: lists all servers the bot is in.
    if message.content.startswith("c!guilds"):
        guildStr = ""
        for guild in bot.guilds:
            guildStr += guild.name + "\n"
        await channel.send(guild.name + "\n")

    if message.content.startswith("c!testturnorder2"):
        team1 = [WoundedTester(),
                 Creature("Fasty McTenSpd (1)", 3, 10, 1, 1, 10, "None", "Light", 1),
                 Creature("Fasty McTenSpd (1)", 3, 10, 1, 1, 10, "None", "Light", 1)]
        team2 = [Creature("Fasty McTenSpd (2)", 3, 10, 1, 1, 10, "None", "Light", 1),
                 Creature("Fasty McTenSpd (2)", 3, 10, 1, 1, 10, "None", "Light", 1),
                 Creature("Fasty McTenSpd (2)", 3, 10, 1, 1, 10, "None", "Light", 1)]
        order = turnOrder(team1, team2)
        orderStr = ""
        for i in order:
            orderStr += i.name + "\n"
        await channel.send(orderStr)


# notice the Target if they post
    if str(message.author.name) == target.name:
        try:
            await channel.send("owo notices " + str(message.author.mention))
        except NameError:
            pass
# gets all angry if felix talks
    if str(message.author) == ("Felix#4169"):
        await channel.send("There's only room for 1 bot in this server")

"""
@bot.event
async def on_message(message):
    if message.author == target:
        await message.channel.send("owo *notices " + target.name + "*")

    await bot.process_commands(message)


@bot.command()
async def guilds(ctx):
    guildStr = ""
    for guild in bot.guilds:
        guildStr += guild.name + "\n"
    await ctx.send(guild.name + "\n")

@bot.command()
async def target(ctx,user : str):
    global target
    try:
        target = grabUser(user)
    except ValueError:
        await ctx.send("Found an @ in the message but it wasn't a mention")
        return

    if target is None:
        await ctx.send("That person doesn't exist!")
    else:
        await ctx.send("I will now notice " + str(target.mention))
@bot.command()
async def tyler(ctx, amount : int):
    for i in range(amount):
        await ctx.send("<@247149441734279169>")
@bot.command()
async def challenge(ctx, user: str):
    p1: discord.Member = ctx.author
    p2: discord.Member = grabUser(user)
    if p1 == p2:
        await ctx.send(embed=discord.Embed(title="Error",
                                       color=discord.Colour.red(),
                                       description="You can't challenge yourself!"))
        return
    challengeMessage = p1.name + " wants to fight " + p2.name + "!"

    def checkAccept(msg):
        return msg.content == "c!accept" and msg.author == p2

    await ctx.send(embed=discord.Embed(title=challengeMessage,
                                       color=discord.Colour.green(),
                                       description="Type c!accept within 30 seconds to accept!"))
    try:
        await bot.wait_for("message", check=checkAccept, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.send(embed=discord.Embed(title="Challenge expired",
                                           color=discord.Colour.red(),
                                           description=p2.name + " took too long to respond."))
        return
    # Setup teams
    else:
        itemList = [items.BigBomb(), items.BeaconOfRage(), items.CandyCorn(), items.FrozenInTime(), items.Grapes(), items.Feast(), items.WoodSpikes()]
        team1 = Team(p1, makeDeck(), makeReserve(), itemList, p1.name)
        team2 = Team(p2, makeDeck(), makeReserve(), itemList, p2.name)
        team1.enemyTeam = team2
        team2.enemyTeam = team1
        turnNumber = 0
        chapter = 0
        #Team 1's field
        lane11 = []
        lane21 = []
        lane31 = []
        #Team 2's field
        lane12 = []
        lane22 = []
        lane32 = []
        await ctx.send(showInfo(team1,team2))
    # Let the games begin! This is the start of a "chapter" where all creatures get to move.
    while len(team1.reserve) + len(team1.field) > 0 and len(team2.reserve) + len(team2.field) > 0:
        order = turnOrder(team1.field, team2.field)
        chapter += 1
        team1.starPoints = 7
        team2.starPoints = 7
        for i in team1.field + team2.field:
            i.onTurnStart()
        # Start a turn, pick who is going to move
        while len(order) > 0:
            creatureToMove = order[0]
            turnUsed = False
            creatureToMove.remainingTurns -= 1
            while not turnUsed:
                turnDialogue = "`Turn " + str(chapter) + "`\n"
                if creatureToMove.currentHp <= 0:
                    continue
                if turnNumber % 2 == 0:
                    teamToMove = team1
                    targetTeam = team2
                else:
                    teamToMove = team2
                    targetTeam = team1
                # Ask for what the user wants to do
                # There are 5 options by default: Attack, Switch, Item, Defend, Info
                # However, under certain circumstances, such as if the player can pay points to change the creature's
                # attributes, or change its form, or if debuffs prevent the creature from moving, then this will add
                # or remove options.
                # TODO: Add conditions to change the options based on properties of the creature.
                options = ["Attack", "Switch", "Item", "Defend", "Info"]
                # Create menu options. If the creature is unable to attack, then attack will be disabled, etc.
                # Frozen creatures cannot attack or switch, and Frozen In Time creatures cannot do anything at all.
                # Status effects that remove Attack:
                if "frozen" in creatureToMove.status or "timeFreeze" in creatureToMove.status:
                    options.remove("Attack")
                # Status effects that remove Switch:
                # Switch is also disabled if the team to move has 0 creatures in reserve.
                if "frozen" in creatureToMove.status or "timeFreeze" in creatureToMove.status or len(teamToMove.reserve) == 0:
                    options.remove("Switch")
                # Status effects that remove Defend:
                if "timeFreeze" in creatureToMove.status:
                    options.remove("Defend")
                # Do Nothing becomes an option if the creature cannot do anything.
                if not ("Attack" in options and "Switch" in options and "Defend" in options):
                    options.append("Do Nothing")
                #If creature has an ability you can pay for, it enables this option.
                if creatureToMove.ability == "Pay":
                    options.append("Ability")
                # make description based on options:
                description = "Choose an option: "
                for i in range(len(options)):
                    description += "\n" + str(i + 1) + ": " + options[i]

                await ctx.send(embed=discord.Embed(title=teamToMove.name + "'s turn"
                                                         + " (" + str(teamToMove.starPoints) + " + " + str(teamToMove.deathPoints)
                                                         + " - "
                                                         + creatureToMove.name,
                                                   color=discord.Colour.gold(),
                                                   description=description))
                def checkAction(msg):
                    try:
                        return msg.author == teamToMove.id and int(msg.content) - 1 < len(options) and int(msg.content) - 1 >= 0
                    except ValueError:
                        return False
                actionMsg = await bot.wait_for("message",
                                               check=checkAction)
                optionIndex = int(actionMsg.content) - 1
                #1. Attack
                if options[optionIndex] == "Attack":
                    extra = None
                    # Attack prompt for a creature who can target anyone on an attack and has an additional effect.
                    if creatureToMove.ability == "OnAtkAny":
                        await ctx.send(embed=discord.Embed(title="Choose any target",
                                                           color=discord.Colour.gold(),
                                                           description=creatureToMove.abilityPrompt + "\n" + listBothTeams(team1.field,team2.field)))
                        def checkTarget(msg):
                            try:
                                return creatureToMove.abilityCheck(msg.content) and msg.author == teamToMove.id
                            except ValueError:
                                return False
                        targetMsg = await bot.wait_for("message",
                                                       check=checkTarget)
                        extra = creatureToMove.setExtra(targetMsg.content)
                        index = int(targetMsg.content.split()[1]) - 1
                        if index < len(team1.field):
                            targetTeam = teamToMove
                        if index >= len(team1.field):
                            index -= len(team1.field)

                    # Attack prompt for a creature who has the standard form of attack.
                    else:
                        await ctx.send(embed=discord.Embed(title="Choose target",
                                                           color=discord.Colour.gold(),
                                                           description=listTeam(targetTeam.field)))
                        def checkTarget(msg):
                            try:
                                return msg.author == teamToMove.id and int(msg.content) < len(targetTeam.field) + 1
                            except ValueError:
                                return False
                        target = await bot.wait_for("message",
                                                    check=checkTarget)
                        index = int(target.content) - 1
                    # Actual attack
                    turnDialogue += str(creatureToMove.attack(targetTeam, index, extra, False))
                    turnUsed = True

                # Switch

                if options[optionIndex] == "Switch":
                    await ctx.send(embed=discord.Embed(title="Switch",
                                                       color=discord.Colour.gold(),
                                                       description="Who would you like to switch out?\n" + listTeam(teamToMove.field)))
                    def checkTeam(msg):
                        try:
                            return msg.author == teamToMove.id and int(msg.content) < len(teamToMove.field) + 1
                        except ValueError:
                            return False

                    switchIn = await bot.wait_for("message",
                                                   check=checkTeam)
                    switchInCreature = teamToMove.field[int(switchIn.content) - 1]
                    # DM user who to switch to, list the reserve team
                    await ctx.send(embed=discord.Embed(title="To Whom?",
                                                       color=discord.Colour.gold(),
                                                       description="You have been DMed the creatures you have " +
                                                                   "in reserve. Type your choice here."))

                    await teamToMove.id.send(embed=discord.Embed(title="Switch",
                                             color=discord.Colour.gold(),
                                             description=listTeam(teamToMove.reserve)))
                    def checkReserve(msg):
                        try:
                            return msg.author == teamToMove.id and len(teamToMove.reserve) >= int(msg.content) > 0
                        except ValueError:
                            return False

                    # Wait for who to switch to.
                    switchOut = await bot.wait_for("message",
                                                      check=checkReserve)
                    switchOutCreature = teamToMove.reserve[int(switchOut.content) - 1]
                    teamToMove.switch(switchInCreature, switchOutCreature)
                    turnDialogue += teamToMove.name + " has switched in " + teamToMove.reserve[int(switchOut.content) - 1].name + \
                                                      " with " + teamToMove.field[int(switchIn.content) - 1].name + "!\n"
                    # TODO: Swapping out may make the player to move the wrong creature.
                    order = turnOrder(team1.field, team2.field)

                # Item - Allow user to use one of their items.
                if options[optionIndex] == "Item":
                    await ctx.send(embed=discord.Embed(title="Item Choice",
                                                       color=discord.Colour.gold(),
                                                       description="You have been DMed the items you have " +
                                                                   "in reserve. Type your choice here, or type 0" +
                                                                   " to cancel."))
                    await teamToMove.id.send(embed=discord.Embed(title="Item",
                                                                 color=discord.Colour.gold(),
                                                                 description=listItems(teamToMove)))
                    def checkItem(msg):
                        try:
                            return msg.author == teamToMove.id and int(msg.content) <= len(teamToMove.items) and int(msg.content) >= 0
                        except ValueError:
                            return False
                    # Wait for the user to select an item.
                    itemIndex = await bot.wait_for("message",
                                                      check=checkItem)
                    if int(itemIndex.content) == 0:
                        continue
                    itemUsed = teamToMove.items[int(itemIndex.content) - 1]
                    if itemUsed.cost > teamToMove.starPoints:
                        await ctx.send(embed=discord.Embed(title="Insufficient points!",
                                                           color=discord.Colour.red(),
                                                           description="You lack the sufficient points to use this item.\n"))
                        continue
                    # List targets depending on item target
                    if itemUsed.target == "ally":
                        await ctx.send(embed=discord.Embed(title="Target",
                                                           color=discord.Colour.gold(),
                                                           description="Choose a creature to target.\n" +
                                                                   listTeam(teamToMove.field))
                                                                   )
                        itemTargetTeam = teamToMove
                    elif itemUsed.target == "enemy":
                        await ctx.send(embed=discord.Embed(title="Target",
                                                           color=discord.Colour.gold(),
                                                           description="Choose a creature to target.\n" +
                                                                       listTeam(targetTeam.field))
                                       )
                        itemTargetTeam = targetTeam
                    else:
                        await ctx.send(embed=discord.Embed(title="Target",
                                                           color=discord.Colour.gold(),
                                                           description="Choose a creature to target.\n" +
                                                                       listBothTeams(teamToMove, targetTeam))
                                       )
                        itemTargetTeam = [teamToMove, targetTeam]
                        # For all items that can target both teams, the target team is a list of both teams.
                    def checkItemTarget(msg):
                        if itemUsed.target == "ally" or itemUsed.target == "enemy":
                            try:
                                return msg.author == teamToMove.id and int(msg.content) <= len(itemTargetTeam.field) and int(msg.content) > 0
                            except ValueError:
                                return False
                        else:
                            try:
                                return msg.author == teamToMove.id and int(msg.content) <= len(itemTargetTeam[0].field + itemTargetTeam[1].field) and int(msg.content) > 0
                            except ValueError:
                                return False

                    # Wait for the user to select an target.
                    targetIndexMsg = await bot.wait_for("message",
                                                      check=checkItemTarget)
                    # This targets a team and index in order to support stuff like AoE attacks
                    targetIndex = int(targetIndexMsg.content) - 1
                    itemMsg = itemUsed.use(itemTargetTeam, targetIndex)
                    if itemMsg == None:
                        turnDialogue += "Item use failed!\n"
                    else:
                        turnDialogue += itemMsg
                        teamToMove.starPoints -= itemUsed.cost
                        teamToMove.items.remove(itemUsed)

                # Defend - 2x DEF for 1 turn
                if options[optionIndex] == "Defend":
                    turnDialogue += creatureToMove.name + " defended!"
                    addStatus(creatureToMove, "defend", 1)
                    turnUsed = True

                # Info - See stats and status effects
                if options[optionIndex] == "Info":
                    combinedTeam = team1.field + team2.field
                    await ctx.send(embed=discord.Embed(title="Info of who?",
                                                       color=discord.Colour.gold(),
                                                       description="Find the info of which creature?\n" +
                                                                   listBothTeams(team1,team2)
                                                                   ))
                    # Wait for who to get info of
                    def checkInfo(msg):
                        try:
                            return msg.author == teamToMove.id and int(msg.content) <= len(combinedTeam) and int(msg.content) > 0
                        except ValueError:
                            return False
                    infoMessage = await bot.wait_for("message",
                                                      check=checkInfo)
                    infoIndex = int(infoMessage.content) - 1
                    # the creature whose info will be gotten.
                    infoC = combinedTeam[infoIndex]
                    statusStr = ""
                    for i in infoC.status:
                        statusStr += statusNames[i] + " - "
                        if infoC.status[i] == 1:
                            statusStr += str(infoC.status[i]) + " turn\n"
                        elif infoC.status[i] > 900:
                            statusStr += " Infinite Turns\n"
                        elif infoC.status[i] > 1:
                            statusStr += str(infoC.status[i]) + " turns\n"
                    infoStr = ("HP: " + str(infoC.currentHp) + "/" + str(infoC.baseHp) + "\n"
                                + "ATK: " + str(infoC.currentAtk) + " (Base:" + str(infoC.baseAtk) + ")\n"
                                + "DEF: " + str(infoC.currentDef) + " (Base:" + str(infoC.baseDef) + ")\n"
                                + "SPD: " + str(infoC.currentSpd) + " (Base:" + str(infoC.baseSpd) + ")\n"
                                + "Status:\n" + statusStr)

                    print(infoStr)
                    await ctx.send(embed=discord.Embed(title="Info of " + infoC.name,
                                                       color=discord.Colour.gold(),
                                                       description=infoStr
                                                       ))
                # Do nothing
                if options[optionIndex] == "Do Nothing":
                    turnDialogue += creatureToMove.name + " does nothing."
                    turnUsed = True
                # Pay points, which makes the creature do something.
                if options[optionIndex] == "Ability":
                    if teamToMove.starPoints < creatureToMove.abilityCost:
                        await ctx.send(embed=discord.Embed(title="Insufficient points",
                                                           color=discord.Colour.red(),
                                                           description="You cannot pay the ability's cost."))
                    else:
                        await ctx.send(embed=discord.Embed(title=creatureToMove.name + "'s ability",
                                                           color=discord.Colour.gold(),
                                                           description=creatureToMove.abilityPrompt))
                        def checkTarget(msg):
                            try:
                                return creatureToMove.abilityCheck(msg.content) and msg.author == teamToMove.id
                            except ValueError:
                                return False
                        decisionMsg = await bot.wait_for("message",
                                                       check=checkTarget)
                        #payAbilities return true if the person pays for them, and false if they don't.
                        paySuccess = creatureToMove.payAbility(decisionMsg.content)
                        if paySuccess:
                            teamToMove.starPoints -= creatureToMove.abilityCost
                try:
                    turnDialogue += showInfo(team1, team2)
                    await ctx.send(turnDialogue)
                except IndexError:
                    break
            if creatureToMove.remainingTurns <= 0:
                order.pop(0)
            reap(team1.field, team2.field)
            await replaceAfterDeath(ctx, team1, team2)
            try:
                turnDialogue += showInfo(team1, team2)
            except IndexError:
                if len(team1.field + team1.reserve) == 0:
                    await ctx.send(embed=discord.Embed(title=p2.name + " wins!",
                                                       color=discord.Colour.green(),
                                                       description="Congratulations!"))
                    return
                if len(team2.field + team2.reserve) == 0:
                    await ctx.send(embed=discord.Embed(title=p1.name + " wins!",
                                                       color=discord.Colour.green(),
                                                       description="Congratulations!"))
                    return
            turnNumber += 1
        for i in team1.field:
            statusEndTurn(i)
        for i in team2.field:
            statusEndTurn(i)
        await replaceAfterDeath(ctx, team1, team2)





@bot.command()
async def testembed(ctx):
    await ctx.send(embed=discord.Embed(title="Something", color=discord.Colour.blue(), description = "Some more text"))

#accept: does nothing
@bot.command()
async def accept(ctx):
    return



@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



#used to grab a member based on the name.
def grabUser(name):
    if "@" in name:
            if "!" in name:
                targetid = int(name[name.index("!") + 1:name.index(">")])

            else:
                targetid = int(name[name.index("@") + 1:name.index(">")])
            memberList = bot.get_all_members()
            memberNames = ""
            for member in memberList:
                memberNames += member.name + "\n"
                if member.id == targetid:
                    return member

    else:
        memberList = bot.get_all_members()
        memberNames = ""
        for member in memberList:
            memberNames += member.name + "\n"
            if member.name == name:
                return member


# given 2 Lists of creatures, determine turn order. Turn order is decided by total speed of lanes.
# After sorting in this method, go down the line and same speed creatures by % health remaining
def turnOrder(t1, t2):
    order = []



# i think it's pretty obvious what this does
def getSpd(creature):
    return creature.currentSpd

# Makes 3 creatures and puts them in the team.
def makeDeck():
    testcreature1 = creatures.ComputerVirus()
    testcreature2 = creatures.TheMaster()
    testcreature3 = creatures.TheMaster()
    return [testcreature1, testcreature2, testcreature3]

def makeReserve():
    testCreature1 = creatures.Creature("Fasty MctenSpd", 3, 10, 1, 3, 10, "None", "Fire", "No Description", "No Flavor", (255, 255, 255, 255), (0, 0, 0, 0))
    testCreature2 = creatures.Creature("Middy McfiveSpd", 3, 10, 1, 3, 5, "None", "Fire", "No Description", "No Flavor", (255, 255, 255, 255), (0, 0, 0, 0))
    testCreature3 = creatures.Creature("Slowy McthreeSpd", 3, 10, 1, 3, 3, "None", "Fire", "No Description", "No Flavor", (255, 255, 255, 255), (0, 0, 0, 0))
    return [testCreature1, testCreature2, testCreature3]
# returns a string of the 2 teams, in this format:
"""
NAME1       NAME2       NAME3
HP:x        HP:y        HP:z
Status:a    Status:b    Status:c

"""
def showInfo(team1,team2):
    desc = "```diff\n"
    desc += team1.name + ":\n\n"
    desc += "+"
    for i in team1.field:
        desc += "{0:20s}".format(i.name)
    desc += "\n\n "
    for i in team1.field:
        desc += "{0:20s}".format("HP:" + str(i.currentHp))
    desc += "\n\n"
    desc += team2.name + ":\n\n"
    desc += "+"
    for i in team2.field:
        desc += "{0:20s}".format(i.name)
    desc += "\n\n "
    for i in team2.field:
        desc += "{0:20s}".format("HP:" + str(i.currentHp))
    desc += "```"
    return desc

# Lists out the possible choices in a team for attacking in the format:
# Creature - x/y HP
# TODO: This should list the creature and not, say, any minions.
def listTeam(team):
    list = ""
    list += "1. " + team.lanes[0][0].name + " - " + str(team.lanes[0][0].currentHp) + "/" + str(team.field[0][0].baseHp) + " HP" + "\n"
    list += "2. " + team.lanes[1][0].name + " - " + str(team.lanes[1][0].currentHp) + "/" + str(team.lanes[1][0].baseHp) + " HP" + "\n"
    list += "3. " + team.lanes[2][0].name + " - " + str(team.lanes[2][0].currentHp) + "/" + str(team.lanes[2][0].baseHp) + " HP" + "\n"
    return list

# Lists out the possible choices in both teams for attacking in the format:
# team1 and team2 are Team.field
# Creature - x/y HP
def listBothTeams(team1,team2):
    list = ""
    for i in range(len(team1.field)):
        list += str(i + 1) + ". " + team1.field[i].name + " - " + str(team1.field[i].currentHp) + "/" + str(team1.field[i].baseHp) + " HP" + "\n"
    for i in range(len(team2.field)):
        list += str(i + 1 + len(team1.field)) + ". " + team2.field[i].name + " - " + str(team2.field[i].currentHp) + "/" + str(team2.field[i].baseHp) + " HP" + "\n"
    return list

def listItems(team):
    list = ""
    for i in range(len(team.items)):
        list += str(i + 1) + ". " + team.items[i].name + " (" + str(team.items[i].cost) + " points)\n"
    return list

# Kills creatures with 0 HP
# Returns True if at least 1 creature died.
def reap(t1, t2):
    isKilled = False
    team1 = t1.copy()
    team2 = t2.copy()
    for i in range(len(team1)):
        if team1[i].currentHp <= 0:
            team1[i].onDeath()
            t1.pop(i)
            isKilled = True
    for i in range(len(team2)):
        if team2[i].currentHp <= 0:
            team2[i].onDeath()
            t2.pop(i)
            isKilled = True
    return isKilled

# Switches 2 list elements given the objects o1, in list l1, and o2, in list l2
def switch(l1, l2, o1, o2):
    l1[l1.index(o1)] = o2
    l2[l2.index(o2)] = o1

# Adds a status effect onto an enemy. effect is a string, duration is an int.
def addStatus(creature, effect, duration):
    status = {effect: duration}
    creature.status.update(status)
    calculateStatusChanges(creature)

# Handles DoT effects and end of turn effects.
def statusEndTurn(creature):
    for i in list(creature.status):
        creature.currentHp -= statusDoT[i]
        if creature.status[i] == 999:
            pass
        else:
            creature.status[i] -= 1
        # Condemned kills the one afflicted when the duration ends.
        if creature.status[i] <= 0:
            if i == "condemned":
                creature.currentHp = 0
            creature.status.pop(i)
            calculateStatusChanges(creature)
# calculates stat changes from status effects
def calculateStatusChanges(creature):
    atkMult = 1
    atkAdd = 0
    defMult = 1
    defAdd = 0
    spdMult = 1
    spdAdd = 0
    for i in creature.status:
        atkMult *= statusMultAtk[i]
        defMult *= statusMultDef[i]
        spdMult *= statusMultSpd[i]
        atkAdd += statusAddAtk[i]
        defAdd += statusAddDef[i]
        spdAdd += statusAddSpd[i]
    creature.currentAtk = (creature.baseAtk * atkMult) + atkAdd
    creature.currentDef = (creature.baseDef * defMult) + defAdd
    creature.currentSpd = (creature.baseSpd * spdMult) + spdAdd

    # Prompt the sending out of another creature after one is killed.
async def replaceAfterDeath(ctx, team1, team2):
    while len(team1.field) < 3 or len(team2.field) < 3:
        # teamToSwitch is the team that is short 1 creature.
        if len(team1.field) < 3:
            teamToSwitch = team1
        if len(team2.field) < 3:
            teamToSwitch = team2
        await ctx.send(embed=discord.Embed(title="Switch someone in",
                                           color=discord.Colour.red(),
                                           description=teamToSwitch.name + " has been DMed the creatures "
                                                 + "they have in reserve. Type the number of the creature you would "
                                                 + "like to swap in."))

        await teamToSwitch.id.send(embed=discord.Embed(title="Switch",
                                                       color=discord.Colour.gold(),
                                                       description=listTeam(teamToSwitch.reserve)))

        def checkReserve(msg):
            try:
                return msg.author == teamToSwitch.id and int(msg.content) <= len(teamToSwitch.reserve) and int(
                    msg.content) > 0
            except ValueError:
                return False

        # Wait for who to switch to.
        switchOut = await bot.wait_for("message",
                     check=checkReserve)
        switchOutCreature = teamToSwitch.reserve[int(switchOut.content) - 1]
        await ctx.send(embed=discord.Embed(title="Choose Slot",
                                           color=discord.Colour.red(),
                                           description="Choose which slot to put the replacement creature in."
                                                 + " 1 represents the leftmost slot, 2 represents the slot to the"
                                                 + " right of the leftmost, etc."))

        def checkSlot(msg):
            try:
                return msg.author == teamToSwitch.id and int(msg.content) <= len(teamToSwitch.field) and int(
                    msg.content) > 0
            except ValueError:
                return False

        switchSlot = await bot.wait_for("message",
                            check=checkSlot)
        teamToSwitch.field.insert(int(switchSlot.content) - 1, switchOutCreature)
        teamToSwitch.reserve.pop(int(switchOut.content) - 1)
        await ctx.send(showInfo(team1, team2))


bot.run(TOKEN)
