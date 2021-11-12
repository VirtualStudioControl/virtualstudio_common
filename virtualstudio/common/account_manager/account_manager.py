from typing import Dict, List, Any, Callable

from virtualstudio.common.account_manager.account_info import AccountInfo, fromDict
from virtualstudio.common.tools.icontools import readPNGIcon

UUID_COUNTER = 0

CATEGORY_ICONS: Dict[str, str] = {}

ACCOUNT_TYPE_ICONS: Dict[str, str] = {}

ACCOUNTS: Dict[str, AccountInfo] = {}

ACCOUNT_CHANGED_CALLBACKS: List[Callable[[str], None]] = []

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
        onAccountChanged(account['uuid'])
        return True, account['uuid']
    if account['uuid'] in ACCOUNTS:
        ACCOUNTS[account['uuid']].update(account)
        storeAccountData()
        onAccountChanged(account['uuid'])
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

def getAccountListOfTypes(*account_type) -> List[AccountInfo]:
    result = []

    for account in ACCOUNTS.values():
        if account.accountType in account_type:
            result.append(account)

    return result


#region Event Management

def registerAccountChangeCallback(callback: Callable[[str], None]):
    ACCOUNT_CHANGED_CALLBACKS.append(callback)


def unregisterAccountChangeCallback(callback: Callable[[str], None]):
    ACCOUNT_CHANGED_CALLBACKS.remove(callback)


def onAccountChanged(accountUUID: str):
    for cb in ACCOUNT_CHANGED_CALLBACKS:
        cb(accountUUID)

#endregion

# Overridden in Core
def storeAccountData() -> None:
    pass