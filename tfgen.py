import json
import random

print('Team Fortress 2 Loadout Generator')
print('by: CommissarCT\n')

# Load the TF.JSON file.
data = None

try:
    with open('tf.json') as d:
        data = json.load(d)
except:
    print('Failed to load the configuration file. File cannot be found or cannot be loaded.')

if (data == None):
    exit()

# If the configuration file gets loaded successfully, continue.

# Select a random class.
classId = random.randint(0, 8)

print('Class: ' + ( data['classes'] )[classId] + '\n')

primaryWeaponArr = data['weapons'][str(classId)]['primary']
secondaryWeaponArr = data['weapons'][str(classId)]['secondary']
meleeWeaponArr = data['weapons'][str(classId)]['melee']

# Select a primary weapon.
pwi = random.randint(0, len(primaryWeaponArr) - 1)
primaryWeapon = primaryWeaponArr[pwi]
print('Primary Weapon: ' + str( primaryWeapon ))

# Select a secondary weapon:
swi = random.randint(0, len(secondaryWeaponArr) - 1)
secondaryWeapon = secondaryWeaponArr[swi]
print('Secondary Weapon: ' + secondaryWeapon)

# Select a melee weapon:
mwi = random.randint(0, len(meleeWeaponArr) - 1)
meleeWeapon = meleeWeaponArr[mwi]
print('Melee Weapon: ' + meleeWeapon)

# If the selected class is Spy, select a sapper:
if (classId == 8):
    sapperArr = data['weapons'][str('8')]['sapper']
    sapperId = random.randint(0, len(sapperArr))
    sapper = sapperArr[sapperId]
    print('Selected Sapper: ' + sapper)

# Finish the program:

print('\nThanks and have fun! ;)')