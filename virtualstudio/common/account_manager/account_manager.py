from typing import Dict, List, Any

from virtualstudio.common.account_manager.account_info import AccountInfo, fromDict
from virtualstudio.common.tools.icontools import readPNGIcon

UUID_COUNTER = 0

CATEGORY_ICONS: Dict[str, str] = {}

ACCOUNT_TYPE_ICONS: Dict[str, str] = {}

ACCOUNTS: Dict[str, AccountInfo] = {}


def generateUUID() -> str:
    global UUID_COUNTER
    res = hex(UUID_COUNTER)
    UUID_COUNTER = UUID_COUNTER +1
    return res


def areAccountsLoaded():
    return True


def registerAccountType(type: str, icon: str):
    if type not in ACCOUNT_TYPE_ICONS:
        ACCOUNT_TYPE_ICONS[type] = readPNGIcon(icon)


def updateAccount(account: Dict[str, Any]) -> (bool, str):
    if account['uuid'] is None:
        # New Account
        account['uuid'] = generateUUID()
        if account['uuid'] in ACCOUNTS:
            return False, account['uuid']
        ACCOUNTS[account['uuid']] = fromDict(account)
        storeAccountData()
        return True, account['uuid']
    if account['uuid'] in ACCOUNTS:
        ACCOUNTS[account['uuid']].update(account)
        storeAccountData()
        return True, account['uuid']
    return False, account['uuid']


def getAccountTypeIcons():
    return ACCOUNT_TYPE_ICONS


def getCategoryIcons():
    return CATEGORY_ICONS


def getAccountByUUID(uuid: str) -> AccountInfo:
    if uuid in ACCOUNTS:
        return ACCOUNTS[uuid]


def getAccountList() -> List[AccountInfo]:
    return list(ACCOUNTS.values())


def storeAccountData() -> None:
    pass