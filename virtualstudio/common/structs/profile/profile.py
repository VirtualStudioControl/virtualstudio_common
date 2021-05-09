from typing import List


class Profile:

    def __init__(self, device: str, device_family: str, name: str, category: List[str]):
        self.device: str = device
        self.device_family: str = device_family
        self.name: str = name
        self.category: List[str] = category

        self.actionLaunchers = {}

        self.actions = []