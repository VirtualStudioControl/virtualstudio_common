import pkgutil as pkg
import logging

def loadModulesFromPath(path, prefix=""):
    '''
    Loads all Filters in the given Package or its subpackages
    '''
    for importer, modname, ispkg in pkg.walk_packages(path=path,
                                                          prefix=prefix,
                                                          onerror=lambda x: logging.error(x)):
        importer.find_module(modname).load_module(modname)
