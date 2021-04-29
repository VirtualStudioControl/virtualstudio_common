from typing import List


class Profile:

    def __init__(self, device, name: str, category: List[str]):
        self.device = device
        self.name: str = name
        self.category: List[str] = category
        self.actionMap = {}
