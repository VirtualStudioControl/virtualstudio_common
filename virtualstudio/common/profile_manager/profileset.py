from typing import Dict

from ..structs.profile.profile import Profile
from ..structs.profile.profile import fromDict as profileFromDict

class ProfileSet():
    def __init__(self, hardwareFamily: str):
        self.hardwareFamily = hardwareFamily
        self.profiles: Dict[str, Profile] = {}

    def appendProfile(self, profile: Profile):
        self.profiles[profile.name] = profile

    def updateProfile(self, profile: Profile):
        self.profiles[profile.name].update(profile)

    def getProfile(self, name):
        if name in self.profiles:
            return self.profiles[name]
        return None

    def removeProfile(self, profileName: str):
        del self.profiles[profileName]

    def toDict(self):
        result = {"hardwareFamily": self.hardwareFamily}

        profileList = []

        for profile in self.profiles:
            profileList.append(self.profiles[profile].toDict())

        result["profiles"] = profileList

        return result

def fromDict(dict):
        hardwareFamily = dict["hardwareFamily"]
        profileSet = ProfileSet(hardwareFamily)

        for profileDict in dict["profiles"]:
            profileSet.appendProfile(profileFromDict(profileDict))

        return profileSet
