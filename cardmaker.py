from __future__ import print_function
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap
import creatures
import math

master = creatures.TheMaster()
virus = creatures.ComputerVirus()

# Makes a card based on the creature.
# creature: Where all the stats come from
def makeCard(creature):
    # Constant for the elements on the card

    # Start with the blank card template
    card = Image.open("images/symbols/blankcard1.png")
    # Take the image of the type and paste it on the card
    for i in range(len(creature.element)):
        regionElement = (0 + (i * 64), 0, 64 + (i * 64), 64)
        elementImage = Image.open("images/symbols/" + creature.element[i] + ".png").convert("RGBA")
        card.paste(elementImage, regionElement, mask=elementImage)
    # Paste the proper number of stars on the upper right corner.
    if creature.stars < 5:
        starImage = Image.open("images/symbols/star3.png").convert("RGBA")
        for i in range(creature.stars):
            regionStars = (444 - (24 * i), 40, 468 - (24 * i), 64)
            card.paste(starImage, regionStars, mask=starImage)
    else:
        regionStars = (370, 6, 468, 64)
        starImage = Image.open("images/symbols/5stars.png").convert("RGBA")
        card.paste(starImage, regionStars, mask=starImage)
    # Paste the card's image on the blank card. The card image is 468x368 px.
    cardImage = Image.open("images/cardimages/" + creature.name + ".png").convert("RGBA")
    regionCardImage = (0, 71, 468, 439)
    card.paste(cardImage, regionCardImage, mask=cardImage)
    # Color the stat bars based on stats and the card's color and paste them in.
    statbar = Image.open("images/symbols/statbar.png").convert("RGBA")
    for i in range(4):
        stat = 0
        if i == 0:
            stat = int(creature.baseHp / 2)
        if i == 1:
            stat = int(creature.baseDef)
        if i == 2:
            stat = int(creature.baseAtk)
        if i == 3:
            stat = int(creature.baseSpd)
        for j in range(stat):
            draw = ImageDraw.Draw(statbar)
            draw.rectangle([2 + (j * 36), 2, 35 + (j * 36), 36], fill=creature.primary)
            del draw
        for j in range(stat, 10):
            draw = ImageDraw.Draw(statbar)
            draw.rectangle([2 + (j * 36), 2, 35 + (j * 36), 36], fill=creature.secondary)
            del draw
        regionBar = (91, 454 + (54 * i), 453, 492 + (54 * i))
        card.paste(statbar, regionBar)
    # Write card name
    cardName = Image.open("images/cardnames/" + creature.name + ".png").convert("RGBA")
    regionName = (234 - (math.floor(cardName.size[0] / 2)), 10,
                  234 - (math.floor(cardName.size[0] / 2)) + cardName.size[0], cardName.size[1] + 10)
    card.paste(cardName, regionName, mask=cardName)
    # Write description and flavor
    descriptionWrapped = textwrap.wrap(creature.description, 45)
    draw = ImageDraw.Draw(card)
    font = ImageFont.truetype("images/fonts/Calibri Regular.ttf",size=24)
    for i in range(len(descriptionWrapped)):
        draw.text((0, 670 + (30 * i)), descriptionWrapped[i], font=font, fill=(0, 0, 0, 0))
    w, h = draw.textsize(creature.flavor, font=font)
    draw.text(((card.size[0] - w) / 2, 900), creature.flavor, font=font, fill=(0, 0, 0, 0))
    card.show()
    return card


monopoly = creatures.Creature("Stoogopoly", 5, 20, 10, 1, 10, "none", ["machine"], "Instead of doing damage, heals everyone on both sides to full hp on attack.  (OYT) Pay 3 points to liquidate your hp and heal another creature for 2x the health lost.","Bad Game", (57, 147, 47, 255), (137, 57, 0, 255))
makeCard(monopoly)