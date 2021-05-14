from typing import Dict

from virtualstudio.common.structs.hardware.hardware_wrapper import HardwareWrapper
from .profileset import ProfileSet

from ..structs.profile.profile import Profile

PROFILE_SETS: Dict[str, ProfileSet] = {}


def createProflieSet(hardware: HardwareWrapper):
    if hardware.getHardwareFamily() not in PROFILE_SETS:
        PROFILE_SETS[hardware.getHardwareFamily()] = ProfileSet(hardware.getHardwareFamily())
        PROFILE_SETS[hardware.getHardwareFamily()].appendProfile(Profile(hardware.getHardwareFamily(), "Default", []))


def getProfileSet(hardware: HardwareWrapper):
    if hardware.getHardwareFamily() in PROFILE_SETS:
        return PROFILE_SETS[hardware.getHardwareFamily()]
    return None


def getOrCreateProfileSet(hardware: HardwareWrapper):
    createProflieSet(hardware)
    return getProfileSet(hardware)
