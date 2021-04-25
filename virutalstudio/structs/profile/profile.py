from typing import List

from ..hardware import Hardware

class Profile:

    def __init__(self, name: str, category: List[str]):
        self.name: str = name
        self.category: List[str] = category
