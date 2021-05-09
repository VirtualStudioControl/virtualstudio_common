from typing import Dict

from ..structs.profile.profile import Profile


class ProfileSet():

    def __init__(self, deviceID: str):
        self.deviceID = deviceID
        self.profiles: Dict[str, Profile] = {}

    def appendProfile(self, profile: Profile):
        self.profiles[profile.name] = profile

    def getProfile(self, name):
        return self.profiles[name]
