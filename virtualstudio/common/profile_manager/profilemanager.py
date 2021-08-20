from typing import Dict

from virtualstudio.common.structs.hardware.hardware_wrapper import HardwareWrapper
from .profileset import ProfileSet, fromDict as profileSetFromDict

from ..structs.profile.profile import Profile
from ..data.constants import PROFILE_NAME_DEFAULT

PROFILE_SETS: Dict[str, ProfileSet] = {}


def createProflieSet(hardware: HardwareWrapper):
    createProflieSetFromFamily(hardware.getHardwareFamily())


def createProflieSetFromFamily(hardwareFamily: str):
    if hardwareFamily not in PROFILE_SETS:
        PROFILE_SETS[hardwareFamily] = ProfileSet(hardwareFamily)
        PROFILE_SETS[hardwareFamily].appendProfile(Profile(hardwareFamily, PROFILE_NAME_DEFAULT, []))


def getProfileSet(hardware: HardwareWrapper):
    return getProfileSetFromFamily(hardware.getHardwareFamily())


def getProfileSetFromFamily(hardwareFamily: str):
    if hardwareFamily in PROFILE_SETS:
        return PROFILE_SETS[hardwareFamily]
    return None


def getOrCreateProfileSetFromFamily(hardwareFamily: str):
    createProflieSetFromFamily(hardwareFamily)
    return getProfileSetFromFamily(hardwareFamily)


def getOrCreateProfileSet(hardware: HardwareWrapper):
    createProflieSet(hardware)
    return getProfileSet(hardware)


def appendProfileSet(profileSet: ProfileSet):
    PROFILE_SETS[profileSet.hardwareFamily] = profileSet


#region Serialisation

def toDict():
    dict = {}
    profilesets = []

    for pset in PROFILE_SETS:
        profilesets.append(PROFILE_SETS[pset].toDict())

    dict["profilesets"] = profilesets

    return dict


def fromDict(values):
    profilesets = values["profilesets"]

    for ps in profilesets:
        pset = profileSetFromDict(ps)
        appendProfileSet(pset)

#endregion