from typing import Dict, Any, Optional


class AccountInfo:

    def __init__(self):
        self.uuid: Optional[str] = None

        self.accountType: str = ""
        self.account_category = []

        self.accountTitle: str = ""

        self.server: str = ""
        self.port: int = 4444

        self.username: str = ""
        self.password: str = ""

        self.parameters: Dict[str, str] = {}

    def toDict(self):
        return {
            "uuid": self.uuid,
            "type": self.accountType,
            "category": self.account_category,
            "title": self.accountTitle,
            "server": self.server,
            "port": self.port,
            "username": self.username,
            "password": (self.password != ""),
            "parameters": self.parameters
        }

    def toDictWthPasswd(self):
        params = self.toDict()
        params["password"] = self.password
        return params

    def update(self, dict: Dict[str, Any]):
        self.accountType = dict["type"]
        self.account_category = dict["category"]
        self.accountTitle = dict["title"]
        self.server = dict["server"]
        self.port = dict["port"]
        self.username = dict["username"]

        self.parameters = dict["parameters"]

        if "password" in dict:
            if not isinstance(dict["password"], bool):
                self.password = dict["password"]


def fromDict(dict: Dict[str, Any]):
    account = AccountInfo()
    account.uuid = dict["uuid"]
    account.accountType = dict["type"]
    account.account_category = dict["category"]
    account.accountTitle = dict["title"]
    account.server = dict["server"]
    account.port = dict["port"]
    account.username = dict["username"]

    account.parameters = dict["parameters"]

    if "password" in dict:
        if not isinstance(dict["password"], bool):
            account.password = dict["password"]

    return account