import struct
import os
import shutil
import __main__

class CMap:
    def __init__(self, path):
        # Set variables
        self.Folder = path
        self.Name = os.path.basename(path)
        self.Path = path + "\\Level.dat"

        # Execute variables
        self.File = open(self.Path, "rb")
        self.HLevelType = self.HasLevelType()
        self.OwnerID = self.GetOwnerID()
        self.LevelSize = self.GetLevelSize()
        if self.HasLevelType():
            self.LevelType = self.GetLevelType()
        else:
            self.LevelType = 0

        # Run the code
        self.File.close()

    def HasLevelType(self):
        if not hasattr(self, "HLevelType"):
            return True if int.from_bytes(self.File.read(1), byteorder="big") > 1 else False
        else:
            return self.HLevelType

    def GetOwnerID(self):
        if not hasattr(self, "OwnerID"):
            return struct.unpack("Q", self.File.read(8))[0]
        else:
            return self.OwnerID

    def GetLevelSize(self):
        if not hasattr(self, "LevelSize"):
            return int.from_bytes(self.File.read(1), byteorder="big")
        else:
            return self.LevelSize

    def GetLevelSizeString(self):
        if not hasattr(self, "LevelSize"):
            return "No level size found!"

        if self.LevelSize == 0:
            return "Tiny"
        elif self.LevelSize == 1:
            return "Small"
        elif self.LevelSize == 2:
            return "Medium"
        elif self.LevelSize == 3:
            return "Large"
        elif self.LevelSize == 4:
            return "Insane"
        else:
            return "Invalid level size!"

    def GetLevelType(self):
        if not hasattr(self, "LevelType"):
            return int.from_bytes(self.File.read(1), byteorder="big")
        else:
            return self.LevelType

    def GetLevelTypeString(self):
        if not hasattr(self, "LevelType"):
            return "No level type found!"

        if self.LevelType == 0:
            return "Survival"
        elif self.LevelType == 1:
            return "Horde"
        elif self.LevelType == 2:
            return "Arena"
        else:
            return "Invalid level type!"

    def Save(self):
        if os.path.isdir(__main__.PATH_TO_MAPS + "\\" + self.Name):
            return False
        shutil.copytree(self.Folder, __main__.PATH_TO_MAPS + "\\" + self.Name)

        output = bytearray()
        output = output + int.to_bytes((2 if self.HasLevelType() else 1), 1, byteorder="big")
        output = output + struct.pack("Q", self.GetOwnerID())
        output = output + int.to_bytes(self.GetLevelSize(), 1, byteorder="big")
        if self.HasLevelType():
            output = output + int.to_bytes(self.GetLevelType(), 1, byteorder="big")

        file = open(__main__.PATH_TO_MAPS + "\\" + self.Name + "\\Level.dat", "wb")
        file.write(output)
        file.close()

        return True
