# Practice Project from Chapter 5: Fantasy Game Inventory

# You are creating a fantasy video game. The data structure to model the
# player’s inventory will be a dictionary where the keys are string values
# describing the item in the inventory and the value is an integer value detailing
# how many of that item the player has. For example, the dictionary value
# {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the
# player has 1 rope, 6 torches, 42 gold coins, and so on.

playerInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    itemCount = 0
    for key,value in inventory.items():
        itemCount += value
        print(str(value) + ' ' + key)
    print('Total number of items: ' + str(itemCount))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory

displayInventory(playerInventory)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print()
print('You slayed a dragon and looted:')
for i in dragonLoot:
    print(i)
print()

playerInventory = addToInventory(playerInventory,dragonLoot)
displayInventory(playerInventory)
