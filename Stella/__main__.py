import importlib
from os.path import dirname
from sys import platform
import asyncio

from Stella import StellaCli, scheduler
from Stella.plugins import ALL_MODULES

IMPORTED = {}
HELPABLE = {}
SUB_MODE = {}
HIDDEN_MOD = {}

STATS = []
USER_INFO = []

if platform == "linux" or platform == "linux2":
    path_dirSec = '/'
elif platform == "win32":
    path_dirSec = '\\'

cdir = dirname(__file__) 

async def import_modules():
    for mode in ALL_MODULES: 
        module = mode.replace(cdir, '').replace(path_dirSec, '.')
        imported_module = importlib.import_module('Stella' + module)
        if not hasattr(imported_module, "__mod_name__"):
            imported_module.__mod_name__ = imported_module.__name__

        if not imported_module.__mod_name__.lower() in IMPORTED:
            IMPORTED[imported_module.__mod_name__.lower()] = imported_module
        else:
            raise Exception("Can't have two modules with the same name! Please change one")

        if hasattr(imported_module, "__help__") and imported_module.__help__:
            HELPABLE[imported_module.__mod_name__.lower()] = imported_module

        if hasattr(imported_module, "__sub_mod__") and imported_module.__sub_mod__:
            SUB_MODE[imported_module.__mod_name__.lower()] = imported_module

        if hasattr(imported_module, "__hidden__") and imported_module.__hidden__:
            HIDDEN_MOD[imported_module.__mod_name__.lower()] = imported_module.__hidden__

        if hasattr(imported_module, "__stats__"):
            STATS.append(imported_module)

        if hasattr(imported_module, "__user_info__"):
            USER_INFO.append(imported_module)

async def main():
    await import_modules()
    # await scheduler.start()
    StellaCli.run()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
