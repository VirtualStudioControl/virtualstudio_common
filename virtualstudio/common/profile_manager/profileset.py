from typing import Dict

from ..structs.profile.profile import Profile


class ProfileSet():
    def __init__(self, hardwareFamily: str):
        self.hardwareFamily = hardwareFamily
        self.profiles: Dict[str, Profile] = {}

    def appendProfile(self, profile: Profile):
        self.profiles[profile.name] = profile

    def getProfile(self, name):
        return self.profiles[name]

    def toDict(self):
        result = {"hardwareFamily": self.hardwareFamily}

        profileList = []

        for profile in self.profiles:
            profileList.append(self.profiles[profile].toDict())

        result["profiles"] = profileList

        return result
