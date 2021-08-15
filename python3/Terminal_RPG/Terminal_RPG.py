#Terminal RPG

from random import randint as ri

#Data
toon_dict = {"fname": "Gene", "hp": 100, "att": 1, "dfen": 2, "dex": 5, "mon": 100}
mob_dict = {"name": "Goblin", "hp": 100, "att": 1, "dfen": 2, "dex": 5}
leather_dict = {"name": "Leather Armor", "dfen": 5, "val": 25}
chain_dict = {"name": "Chain Armor", "dfen": 10, "val": 50}
mace_dict = {"name": "Mace", "att": 10, "val": 25}
sword_dict = {"name": "Sword", "att": 20, "val": 50}
bsword_dict = {"name": "Bastard Sword", "att": 50, "val": 500}
plate_dict = {"name": "Plate Mail", "dfen": 50, "val": 500}
fog_dict = {"name": "Finger of God", "att": 100}
sot_dict = {"name": "The Shroud of Turin", "dfen": 100}
#Data

def main_m():
    print("Welcome traveler to Terminal RPG!!!")
    toon_dict["fname"] = input("What's your name?\n: ")
    _input = input("Are you ready to fight your first opponent?\n(y/n): ")
    if _input == "y":
        action_m()
    elif _input == "n":
        print("Come back when you are ready!!!")
        exit()
    else:
        print("What was that?")
        main_m()

def action_m():
    end()
    print("(" + toon_dict["fname"] + ")" + " Att:" + str(toon_dict["att"]) + " Def:" + str(toon_dict["dfen"]) + " HP:" + str(toon_dict["hp"]))
    print("(" + mob_dict["name"] + ")" + " Att:" + str(mob_dict["att"]) + " Def:" + str(mob_dict["dfen"]) + " HP:" + str(mob_dict["hp"]))
    print("Enter 'a' to Attack")
    print("Enter 'h' to Heal")
    print("Enter 'e' to Equip an item")
    print("Enter 's' for the store")
#    print("Enter 'edit' for edit menu")
    print("Enter 'p' to summon a Thrall")
    print("Enter 'x' to Exit")
    _input = input(": ")
    if _input == "x":
        exit()
    elif _input == "a":
        attack()
        action_m()
    elif _input == "h":
        heal()
        action_m()
    elif _input == "e":
        equip_m()
    elif _input == "edit":
        create_m()
    elif _input == "p":
        pit()
    elif _input == "s":
        storef()
    else:
        print("What was that?")
        action_m()

def equip_m():
    print("Pick your poison")
    print("Enter '1' for " + leather_dict["name"])
    print("Enter '2' for " + chain_dict["name"])
    print("Enter '3' for " + sword_dict["name"])
    print("Enter '4' for " + mace_dict["name"])
#    print("Enter 'FOG' for " + fog_dict["name"])
    print("Enter 'b' to go back")
    _input = input(": ")
    if _input == "b":
        action_m()
    elif _input == "1":
        equip_a(leather_dict)
        action_m()
    elif _input == "2":
        equip_a(chain_dict)
        action_m()
    elif _input == "3":
        equip_w(sword_dict)
        action_m()
    elif _input == "4":
        equip_w(mace_dict)
        action_m()
    elif _input == "FOG":
        equip_w(fog_dict)
        action_m()
    elif _input == "SOT":
        equip_a(sot_dict)
        action_m()
    elif _input == "chuck":
        toon_dict["fname"] = "Chuck Norris"
        toon_dict["hp"] = 10000000
        toon_dict["att"] = 10000000
        toon_dict["dfen"] = 10000000
        toon_dict["dex"] = 10000000
        action_m()
    else:
        print("What was that?")
        equip_m()


def create_m():
    print("Enter 't' to edit Toon")
    print("Enter 'm' to edit Mob")
    print("Enter 'b' to go back")
    _input = input(": ")
    if _input == "t":
        create_toon()
    elif _input == "m":
        create_mob()
    elif _input == "b":
        action_m()
    else:
        print("What was that?")
        create_m()

def create_toon():
    print(toon_dict)
    print("Type the name of the field you want to edit")
    input_key = input(": ")
    input_value = input("Value: ")
    if input_key == "fname":
        toon_dict[input_key] = (input_value)
    else:
        toon_dict[input_key] = int(input_value)
    print(toon_dict)
    create_m()

def create_mob():
    print(mob_dict)
    print("Type the name of the field you want to edit")
    input_key = input(": ")
    input_value = input("Value: ")
    if input_key == "name":
        mob_dict[input_key] = (input_value)
    else:
        mob_dict[input_key] = int(input_value)
    print(mob_dict)
    create_m()

def create_item():
    pass

def e_credit():
    print("Thank you for playing Terminal RPG!!!")
    print("(" + toon_dict["fname"] + ")" + " Att:" + str(toon_dict["att"]) + " Def:" + str(toon_dict["dfen"]) + " HP:" + str(toon_dict["hp"]))
    print("(" + mob_dict["name"] + ")" + " Att:" + str(mob_dict["att"]) + " Def:" + str(mob_dict["dfen"]) + " HP:" + str(mob_dict["hp"]))
    exit()

def attack():
    slap = toon_dict["att"] * (1 - mob_dict["dfen"] * 0.01)
    hit = mob_dict["hp"] - slap
    mob_dict["hp"] = hit
    print(toon_dict["fname"] + " smashes the " + mob_dict["name"] + " about the face!!!\n")
    slap = mob_dict["att"] * (1 - toon_dict["dfen"] * 0.01)
    hit = toon_dict["hp"] - slap
    toon_dict["hp"] = hit
    print("The " + mob_dict["name"] + " just slapped the holy living f*** out of you!!!\n")

def equip_a(armor_dict):
    if toon_dict["dfen"] >2:
        print("You can only equip one item")
    else:
        toon_dict["dfen"] = armor_dict["dfen"]
        print("Done")

def equip_w(weapon_dict):
    if toon_dict["att"] >2:
        print("You can only equip one item")
    else:
        toon_dict["att"] = weapon_dict["att"]
        print("Done")

def heal():
    if toon_dict["hp"] == 100:
        print("Don't waste your time, your health is at MAX")
    else:
        print("Gulp!!!")
        if toon_dict["hp"] >=50:
            toon_dict["hp"] = 100
        else:
            heal = toon_dict["hp"] + 50
            toon_dict["hp"] = heal
def end():
    global mob_dict
    if toon_dict["hp"] <= 0:
        print("You're DEAD!!!")
        e_credit()
    elif mob_dict["hp"] <= 0:
        print("You've killed the " + mob_dict["name"] + "!!!")
        if mob_dict["name"] == "Goblin":
            mob_dict = {"name": "Dragon", "hp": 200, "att": 10, "dfen": 20, "dex": 10}
            action_m()
        elif mob_dict["name"] == "Dragon":
            mob_dict = {"name": "Darkness", "hp": 500, "att": 20, "dfen": 40, "dex": 20}
            action_m()
        elif mob_dict["name"] == "Darkness":
            e_credit()
    elif toon_dict["hp"] >= 1:
        pass

def pit():
    global mob_dict
    print("Welcome to the PIT\nThe next oppenent will have random stats\nGood Luck!!!")
    mob_dict = {"name": "Thrall", "hp": ri(1, 1000), "att": ri(1, 100), "dfen": ri(1, 100), "dex": ri(1, 100)}
    action_m()

def storef():
    print("Welcome to the store\nWhat can I do you for?")
    print("Enter 'b' to buy")
    print("Enter 's' to sell")
    print("Enter 'x' to exit")
    _input = input(": ")
    if _input == "x":
        action_m()
    elif _input == "b":
        storef()
    elif _input == "s":
        storef()
    else:
        print("WTF was that?")
        storef()

main_m()