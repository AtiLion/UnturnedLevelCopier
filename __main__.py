import os
from Map import CMap

# Functions
def IsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Initialization code
PATH_TO_UNTURNED = ""
PATH_TO_WORKSHOP = ""
STEAM64 = ""
while True:
    PATH_TO_UNTURNED = input("Enter path to unturned: ")
    if os.path.isdir(PATH_TO_UNTURNED) and os.path.isdir(PATH_TO_UNTURNED + "\\Maps") and os.path.isdir(PATH_TO_UNTURNED + "\\Bundles\\Workshop\\Maps"):
        break
    else:
        print("Invalid path! Please select a different path")
while True:
    PATH_TO_WORKSHOP = input("Enter path to steam workshop(steamapps/workshop/content): ")
    if os.path.isdir(PATH_TO_WORKSHOP):
        if not os.path.isdir(PATH_TO_WORKSHOP + "\\304930"):
            break
        else:
            if len(os.listdir(PATH_TO_WORKSHOP + "\\304930")) > 0 and os.path.isdir(PATH_TO_WORKSHOP + "\\304930\\" + os.listdir(PATH_TO_WORKSHOP + "\\304930")[0]):
                if os.path.exists((PATH_TO_WORKSHOP + "\\304930\\" + os.listdir(PATH_TO_WORKSHOP + "\\304930")[0]) + "\\Map.meta"):
                    break
                else:
                    print("Invalid path! Please select a different path")
            else:
                print("Invalid path! Please select a different path")
    else:
        print("Invalid path! Please select a different path")
while True:
    STEAM64 = input("Enter your steam64 ID: ")
    if IsInt(STEAM64):
        break

# Set the variables
PATH_TO_MAPS = PATH_TO_UNTURNED + "\\Maps"
PATH_TO_BUNDLES = PATH_TO_UNTURNED + "\\Bundles\\Workshop\\Maps"
PATH_TO_SHOP = PATH_TO_WORKSHOP + "\\304930"
MAPS = []
SELECTED_MAP = None

# Post initialization code
for directory in os.listdir(PATH_TO_MAPS):
    dirPath = PATH_TO_MAPS + "\\" + directory

    if os.path.isdir(dirPath) and os.path.exists(dirPath + "\\Level.dat"):
        MAPS.append(dirPath)
for directory in os.listdir(PATH_TO_BUNDLES):
    dirPath = PATH_TO_BUNDLES + "\\" + directory

    if os.path.isdir(dirPath) and os.path.exists(dirPath + "\\Level.dat"):
        MAPS.append(dirPath)
for directory in os.listdir(PATH_TO_SHOP):
    dirPath = PATH_TO_SHOP + "\\" + directory + "\\" + os.listdir(PATH_TO_SHOP + "\\" + directory)[0]

    if os.path.isdir(dirPath) and os.path.exists(dirPath + "\\Level.dat"):
        MAPS.append(dirPath)
while True:
    print("Select map by typing the ID at the bottom!")
    for lID, level in enumerate(MAPS):
        print(str(lID) + ". " + os.path.basename(level))
    pick = input("Map to copy: ")
    if IsInt(pick) and int(pick) > 0 and int(pick) < len(MAPS):
        SELECTED_MAP = CMap(MAPS[int(pick)])
        break

# Print old info
print("")
print("")
print("Old map information: ")
print("Level name: " + SELECTED_MAP.Name)
print("Level owner ID: " + str(SELECTED_MAP.GetOwnerID()))
print("Has defined level type: " + ("Yes" if SELECTED_MAP.HasLevelType() else "No"))
print("Level type: " + SELECTED_MAP.GetLevelTypeString())
print("Level size: " + SELECTED_MAP.GetLevelSizeString())

# Set new info
SELECTED_MAP.OwnerID = int(STEAM64)
SELECTED_MAP.Name = SELECTED_MAP.Name + " Copy"

# Print new info
print("")
print("")
print("New map information: ")
print("Level name: " + SELECTED_MAP.Name)
print("Level owner ID: " + str(SELECTED_MAP.GetOwnerID()))
print("Has defined level type: " + ("Yes" if SELECTED_MAP.HasLevelType() else "No"))
print("Level type: " + SELECTED_MAP.GetLevelTypeString())
print("Level size: " + SELECTED_MAP.GetLevelSizeString())

# Finish code
print("")
SAVE = input("Save the map(y/n)? ")

if SAVE.lower() == "y":
    print("Saving map...")
    if SELECTED_MAP.Save():
        print("Saved map!")
    else:
        print("Failed to save map!")
else:
    print("Discarded changes!")
